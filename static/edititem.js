let throw_error = true;
let segments; 
let fabricid;

$(document).ready(function() {
    segments = window.location.href.split( '/' );
    fabricid = segments[4];
    populate_template();

    // submitting edits
    $("#subedit-button").click(function(e) {
        e.preventDefault();
        err_check();
        gather_input();
        edit_fabric(fabrics);
    })

    // discard changes
    $("#dialog-1").dialog({
        autoOpen: false,  
     });
    $("#discard-button").click(function(ev) {
        ev.preventDefault();
        $("#dialog-1").dialog( "open" );
        discard_choices();
    })
})

function discard_choices() {
    $("#yessure").click(function(ev) {
        ev.preventDefault();
        backtoview();
    })

    $("#notsure").click(function(ev) {
        ev.preventDefault();
        $("#dialog-1").dialog( "close" );
    })
}

function populate_template() {
    $.each(fabrics, function (index, value) {
        if(value["id"] == fabricid) {
            $("#editfname").val(value["fabric_name"]);
            $("#editimg-url").val(value["image"]);
            $("#editfab-desc").val(value["summary"]);
            $("#editavg-price").val(value["price_per_yard"]);
            $("#editbuy-site").val(value["purchase_site"]);
            $("#editcomm-clothes").val(value["common_clothes"]);
            $("#editsew-tips").val(value["sewing_tips"]);
            $("#editsim-fabs").val(value["similar_fabrics"]);
        }
    })
}

function err_check() {
    throw_error = true;

    let nameEmpty = $("#editfname").val().replace(/^\s+|\s+$/g, "").length;
    let imageEmpty = $("#editimg-url").val().replace(/^\s+|\s+$/g, "").length;
    let descEmpty = $("#editfab-desc").val().replace(/^\s+|\s+$/g, "").length;
    let priceEmpty = $("#editavg-price").val().replace(/^\s+|\s+$/g, "").length;
    let siteEmpty = $("#editbuy-site").val().replace(/^\s+|\s+$/g, "").length;
    let commEmpty = $("#editcomm-clothes").val().length;
    let sewTipsEmpty = $("#editsew-tips").val().replace(/^\s+|\s+$/g, "").length;
    let simFabsEmpty = $("#editsim-fabs").val().length;

    if(simFabsEmpty == 0) {
        $("#err-sim").show();
        $("#sim-fabs").focus();
    }

    if(sewTipsEmpty == 0) {
        $("#err-tips").show();
        $("#sew-tips").focus();
    }

    if(commEmpty == 0) {
        $("#err-comm").show();
        $("#comm-clothes").focus();
    }

    if(siteEmpty == 0) {
        $("#err-buy").show();
        $("#buy-site").focus();
    }

    if(priceEmpty == 0 || !($.isNumeric($("#editavg-price").val()))) {
        $("#err-price").show();
        $("#avg-price").val("").focus();
    }

    if(descEmpty == 0) {
        $("#err-desc").show();
        $("#fab-desc").focus();
    }

    if(imageEmpty == 0) {
        $("#err-img").show();
        $("#img-url").focus();
    }

    if(nameEmpty == 0) {
        $("#err-name").show();
        $("#fname").focus();
    }

    else if (simFabsEmpty && sewTipsEmpty && commEmpty && siteEmpty && priceEmpty && descEmpty && imageEmpty && nameEmpty && $.isNumeric($("#editavg-price").val())) {
        throw_error = false;
    }
}

function gather_input() {
    let fabricNameIn = jQuery.trim($("#editfname").val());
    let imgUrlIn = jQuery.trim($("#editimg-url").val());
    let fabDescIn = $("#editfab-desc").val();
    let priceIn = jQuery.trim($("#editavg-price").val());
    let buySiteIn = jQuery.trim($("#editbuy-site").val());
    let clothesIn = $("#editcomm-clothes").val();
    clothesIn = clothesIn.split(',');
    let sewTipsIn = $("#editsew-tips").val();
    let simFabsIn = $("#editsim-fabs").val();
    simFabsIn = simFabsIn.split(',');

    fabrics = {"id": fabricid, "fabric_name": fabricNameIn, "image": imgUrlIn, "summary": fabDescIn, "price_per_yard": priceIn, "purchase_site": buySiteIn, "common_clothes": clothesIn, "sewing_tips": sewTipsIn, "similar_fabrics": simFabsIn};
}

function edit_fabric(newfabric) {
    if (throw_error) {
        return;
    }
    $.ajax({
        type: "POST",
        url: "/edit_fab",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(newfabric),
        success: function(result){
            let all_fabrics = result["fabrics"]
            fabrics = all_fabrics
            console.log(fabrics);
            backtoview();
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    }); 
}

function backtoview() {
    window.location.assign("/view/" + fabricid);
}
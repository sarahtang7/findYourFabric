let throw_error = true;

$(document).ready(function() {
    // for search bar
    $("#target").submit(function( event ) {
        event.preventDefault();

        if ($("#search-bar").val().replace(/^\s+|\s+$/g, "").length == 0) {
            $("#search-bar").val('').focus();
        }
        else {
            window.location.assign("/searchresults/" + $("#search-bar").val());
        }
    })
    
    $("#fname").focus();

    // for error messages
    $("#err-sim").hide();
    $("#err-name").hide();
    $("#err-img").hide();
    $("#err-desc").hide();
    $("#err-price").hide();
    $("#err-buy").hide();
    $("#err-comm").hide();
    $("#err-tips").hide();

    // add new entry
    $("#add-button").on('click', function() {
        err_check();
        gather_input();
        add_fabric(fabrics);
        $(window).scrollTop();
    })
})

function err_check() {
    throw_error = true;

    let nameEmpty = $("#fname").val().replace(/^\s+|\s+$/g, "").length;
    let imageEmpty = $("#img-url").val().replace(/^\s+|\s+$/g, "").length;
    let descEmpty = $("#fab-desc").val().replace(/^\s+|\s+$/g, "").length;
    let priceEmpty = $("#avg-price").val().replace(/^\s+|\s+$/g, "").length;
    let siteEmpty = $("#buy-site").val().replace(/^\s+|\s+$/g, "").length;
    let commEmpty = $("#comm-clothes").val().length;
    let sewTipsEmpty = $("#sew-tips").val().replace(/^\s+|\s+$/g, "").length;
    let simFabsEmpty = $("#sim-fabs").val().length;

    $("#err-sim").hide();
    $("#err-name").hide();
    $("#err-img").hide();
    $("#err-desc").hide();
    $("#err-price").hide();
    $("#err-buy").hide();
    $("#err-comm").hide();
    $("#err-tips").hide();

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

    if(priceEmpty == 0 || !($.isNumeric($("#avg-price").val()))) {
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

    else if (simFabsEmpty && sewTipsEmpty && commEmpty && siteEmpty && priceEmpty && descEmpty && imageEmpty && nameEmpty && $.isNumeric($("#avg-price").val())) {
        throw_error = false;
    }
}

function gather_input() {
    let fabricNameIn = jQuery.trim($("#fname").val());
    let imgUrlIn = jQuery.trim($("#img-url").val());
    let fabDescIn = $("#fab-desc").val();
    let priceIn = jQuery.trim($("#avg-price").val());
    let buySiteIn = jQuery.trim($("#buy-site").val());
    let clothesIn = $("#comm-clothes").val();
    clothesIn = clothesIn.split(',');
    let sewTipsIn = $("#sew-tips").val();
    let simFabsIn = $("#sim-fabs").val();
    simFabsIn = simFabsIn.split(',');

    fabrics = {"fabric_name": fabricNameIn, "image": imgUrlIn, "summary": fabDescIn, "price_per_yard": priceIn, "purchase_site": buySiteIn, "common_clothes": clothesIn, "sewing_tips": sewTipsIn, "similar_fabrics": simFabsIn};
}

function add_fabric(newfabric) {
    if (throw_error) {
        return;
    }

    $.ajax({
        type: "POST",
        url: "add_fabric",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(newfabric),
        success: function(result){
            let all_fabrics = result["fabrics"]
            fabrics = all_fabrics
            
            // clear all fields
            $("#fname").val("");
            $("#img-url").val("");
            $("#fab-desc").val("");
            $("#avg-price").val("");
            $("#buy-site").val("");
            $("#comm-clothes").val("");
            $("#sew-tips").val("");
            $("#sim-fabs").val("");

            // view new entry
            view_new(newfabric.fabric_name);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    }); 
}

function view_new(fabricname) {
    let getid = -1;
    // find correlated ID
    $.each(fabrics, function (index, value) {
        if(value["fabric_name"].toLowerCase() == fabricname.toLowerCase()) {
            getid=value["id"];
        }
    })
    $("#success-new").append("<span id='new-item'><br>New item successfully created. <a href= /view/"+getid+">View it here!</a></span>");
}
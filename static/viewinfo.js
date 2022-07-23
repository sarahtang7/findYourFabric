function view_info(id) {
    $.each(fabrics, function (index, value) {
        if(value["id"] == id) {
            $("#name-of-fabric").append(value["fabric_name"]);
            $("#fabric-image").append("<img src="+value["image"]+" alt='image of "+value["fabric_name"]+" fabric' width='200'>");
            $("#fabric-summary").append(value["summary"]);
            $("#price-per-yard").append(value["price_per_yard"]);
            $("#sewing-tips").append(value["sewing_tips"]);
            let buysitesegs = value['purchase_site'].split('/');
            let shorturl = buysitesegs[2];
            $("#purchase-site").append("<a href="+value["purchase_site"]+">"+shorturl+"/...</a>");

            $.each(value["common_clothes"], function (ind, val) {
                $("#common-clothing").append("<span class='searchcomm' onclick='display_search(\""+val+"\")'>"+val+"</span>");
                if(ind != value["common_clothes"].length-1) { 
                    $("#common-clothing").append(", ");
                }
            })
            
            $.each(value["similar_fabrics"], function (ind, val) {
                $("#sim-fabrics").append("<span class='searchcomm' onclick='display_search(\""+val+"\")'>"+val+"</span>");
                if(ind != value["similar_fabrics"].length-1) {
                     $("#sim-fabrics").append(", ");
                }
            })
        }
    });
}

function display_search(searchfor) {
    window.location.assign("/searchresults/" + searchfor);
}

$(document).ready(function() {
    let segments = window.location.href.split( '/' );
    let idcurr = segments[4];

    view_info(idcurr);

    // edit entry
    $("#edit-button").click(function(event) {
        event.preventDefault();
        let segments = window.location.href.split( '/' );
        let fabricid = segments[4];
        window.location.assign("/edit/" + fabricid);
    })
})
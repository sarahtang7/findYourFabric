$(document).ready(function() {
    setup_homepage(1, 4, 5); // change these id numbers to change fabrics on homepage
    $("#search-bar").empty();
    $("#target").submit(function( event ) {
        event.preventDefault();

        if ($("#search-bar").val().replace(/^\s+|\s+$/g, "").length == 0) {
            $("#search-bar").val('').focus();
        }
        else {
            window.location.assign("/searchresults/" + $("#search-bar").val());
        }
    })
})

function setup_homepage(id1, id2, id3) {
    $.each(fabrics, function (index, value) {
        if(value["id"] == id1) {
            $("#pop-fabric-1").append("<img src='"+value["image"]+"' alt='image of "+value["fabric_name"]+" fabric' class='img-fluid'>");
            $("#top_fabric1").append(("<div data-id: '"+id1+"'>" + value["fabric_name"]) + "<br></div>");
            $("#blurb-fabric-1").append(value["summary"].substring(0, 150) + "...");
        }
        if(value["id"] == id2) {
            $("#pop-fabric-2").append("<img src='"+value["image"]+"' alt='image of "+value["fabric_name"]+" fabric' class='img-fluid'>");
            $("#top_fabric2").append(("<div data-id: '"+id2+"'>" + value["fabric_name"]) + "<br></div>");
            $("#blurb-fabric-2").append(value["summary"].substring(0, 150) + "...");
        }
        if(value["id"] == id3) {
            $("#pop-fabric-3").append("<img src='"+value["image"]+"' alt='image of "+value["fabric_name"]+" fabric' class='img-fluid'>");
            $("#top_fabric3").append(("<div data-id: '"+id3+"'>" + value["fabric_name"]) + "<br></div>");
            $("#blurb-fabric-3").append(value["summary"].substring(0, 150) + "...");
        }
    });

    $("#pop-fabric-1").click(function(event) {
        window.location.assign("/view/" + id1);
        event.preventDefault();
    })

    $("#pop-fabric-2").click(function(event) {
        window.location.assign("/view/" + id2);
        event.preventDefault();
    })

    $("#pop-fabric-3").click(function(event) {
        window.location.assign("/view/" + id3);
        event.preventDefault();
    })
}
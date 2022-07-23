$(document).ready(function() {
    let segments = window.location.href.split( '/' );
    let fabricname = segments[4]; // what is searched for
    let spacefabricname = fabricname.replace("%20", " ");

    $("#searchres").append('Search results for "' + spacefabricname + '":');
    
    display_search_res(spacefabricname);
})

function display_search_res(fabric) {
    if(resultfabs.length == 0) {
        $("#searchres").after("<div>No results found</div>")
    }
    $("#searchres").append('<div id="reslength">'+ resultfabs.length + ' results found<br></div>');
    let substring = new RegExp(fabric, "gi");
    $.each(resultfabs, function(index) {
        let boldresfabs = resultfabs[index].replace(substring, "<b><span class='standout'>$&</span></b>");
        let boldressum = resultsum[index].replace(substring, "<b><span class='standout'>$&</span></b>");
        let boldresclothes = [];
        $.each(resultclothes[index], function(ind, val) {
            boldresclothes.push(val.replace(substring, "<b><span class='standout'>$&</span></b>"));
        })
        $("#searchres").after(("<div class='choices' onclick=display_view("+resultids[index]+")>"+boldresfabs+
                                "<br><span class='search-sums'>"+boldressum+
                                "<br><u>Common Clothes</u>: "+boldresclothes+"</span></div><br>"));
    })
}

function display_view(id) {
    window.location.assign("/view/" + id);
}
function fill_search(str) {
    document.getElementById("search-bar").value = str;
}

$("#search-bar").keyup(function () {
    console.log( $(this).val() );
    var str = $(this).val();
    if(str.length>0) {
        $(".dropdown-menu").empty();
        $(".dropdown-menu").css({"display": ""});
        $.ajax({
            type: 'GET',
            url: '/view/search/',
            data: {
                'search_text': str
            },
            dataType: 'json',
            success: function (data) {
                if(data.quote.length>0){
                    $(".dropdown-menu").append("<h6 class=\"dropdown-header\" id=\"quote-header\">Quotes</h6>");
                    for(i=0; i<data.quote.length; i++){
                        $("#quote-header").after("<button class=\"dropdown-item\" type=\"button\" onclick=\"fill_search(this.innerHTML)\">"+data.quote[i]+"</button>")
                    }
                }
                else{
                    $("#quote-header").remove();
                }
                if(data.person.length>0){
                    $(".dropdown-menu").append("<h6 class=\"dropdown-header\" id=\"person-header\">Person</h6>");
                    for(i=0; i<data.person.length; i++){
                        $("#person-header").after("<button class=\"dropdown-item\" type=\"button\" onclick=\"fill_search(this.innerHTML)\">"+data.person[i]+"</button>")
                    }
                }
                else{
                    $("#person-header").remove();
                }
                if(data.place.length>0){
                    $(".dropdown-menu").append("<h6 class=\"dropdown-header\" id=\"place-header\">Place</h6>");
                    for(i=0; i<data.place.length; i++){
                        $("#place-header").after("<button class=\"dropdown-item\" type=\"button\" onclick=\"fill_search(this.innerHTML)\">"+data.place[i]+"</button>")
                    }
                }
                else{
                    $("#place-header").remove();
                }
                if(data.place.length===0 && data.quote.length===0 && data.person.length===0)
                    $(".dropdown-menu").css({"display": "None"});
            }
        });
    }
    else{
        $(".dropdown-menu").css({"display": "None"});
    }
});
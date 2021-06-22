$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.fixed-action-btn').floatingActionButton({direction: 'left'});
    
    // Get length of posts content and hide part of it
    var card_title = $(".card-title").siblings().children("p");
    console.log(card_title);
    $(card_title).each(function(){

        var content = $(this).text().substring(0, 165);
        var content_length = $(this).text().length;

        console.log(content_length);

        if (content_length > 165) {
            $(this).text(content + "...")
        }
    })
});

$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.fixed-action-btn').floatingActionButton({direction: 'left'});


    // Get length of posts content and hide part of it
    var card_title = $(".card-title").siblings().children()[0];

    $(card_title).each(function(){
        $(this).text("aaaaaaa")
    })

    

});


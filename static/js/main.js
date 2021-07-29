$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    if( /Android|webOS|iPhone|iPad|Mac|Macintosh|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) 
    {
        $('.fixed-action-btn').floatingActionButton({direction: 'top'});
    }
    else 
    {
        $('.fixed-action-btn').floatingActionButton({direction: 'left'});
    }
    
    $('select').formSelect();
    $('.modal').modal();
    
    // convert text to html (nl to br) python lines 37, 55
    $(".card-content").children("#text-to-read").each(function(){
        var div = $(this);
        div.html(div.text())
    })

    // If comment/delete aborted, clear textarea and close modal
    $(".comment-btn").click(function(e){
        $("#comment").val("");
        $('.modal').modal("close");
        e.preventDefault();
    })

    // Copy post link to clipboard
    $(".copy-post-link").click(function(){
        value = $(this).attr("value")

        // stackoverflow.com/questions/47207355/copy-to-clipboard-using-jquery/47207504
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val(value).select();
        document.execCommand("copy");
        $temp.remove();
    })

    // My page show/hide sections
    $(".my-page-btn").click(function(){
        var get_id = $(this).attr("id")
        var section = document.getElementsByClassName(get_id)
        $(section).css("display","block")
        // if section is empty
        if($(section).html().length < 1000){
            $(section).html("<h4>Sorry No Results!</h4>")
        }
        $(section).siblings().css("display","none")
    })

    // hide flash message
    setTimeout(function() {
        $('.flash-message').fadeOut('slow');
    }, 1000);
    
    /// allow to use tab in textarea 
    /// code sample https://stackoverflow.com/questions/6140632/how-to-handle-tab-in-textarea

    $("textarea").keydown(function(e) {
        if(e.keyCode === 9) { // tab was pressed
            // get caret position/selection
            var start = this.selectionStart;
            var end = this.selectionEnd;
    
            var $this = $(this);
            var value = $this.val();
    
            // set textarea value to: text before caret + tab + text after caret
            $this.val(value.substring(0, start)
                        + "\t"
                        + value.substring(end));
    
            // put caret at right position again (add one for the tab)
            this.selectionStart = this.selectionEnd = start + 1;
    
            // prevent the focus lose
            e.preventDefault();
        }
    });
    //////////////////////////////////////////////////////


    // Get length of posts content and hide some
    $(".card-content").each(function(){

        var id_atribute = $(this).attr("id")

        // If post is not opened for reading hide text
        if (id_atribute != "read") {

            var content = $(this).text().substring(0, 165);
            var content_length = $(this).text().length;

            if (content_length > 165) {
                $(this).text(content + "...")
        }
        }
    })

    validateMaterializeSelect();
      function validateMaterializeSelect() {
          let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
          let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
          if ($("select.validate").prop("required")) {
              $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
          }
          $(".select-wrapper input.select-dropdown").on("focusin", function () {
              $(this).parent(".select-wrapper").on("change", function () {
                  if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                      $(this).children("input").css(classValid);
                  }
              });
          }).on("click", function () {
              if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                  $(this).parent(".select-wrapper").children("input").css(classValid);
              } else {
                  $(".select-wrapper input.select-dropdown").on("focusout", function () {
                      if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                          if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                              $(this).parent(".select-wrapper").children("input").css(classInvalid);
                          }
                      }
                  });
              }
          });
      }
    
});
$(function(){
    var _window = $(window),
    _header = $('.site_header'),
    imageBottom;
 
    _window.on('scroll',function(){     
        imageBottom = $('.image').height();
        if(_window.scrollTop() > imageBottom){
            _header.addClass('fixed');   
        }
        else{
            _header.removeClass('fixed');   
        }
    });
 
    _window.trigger('scroll');

});

$(function($) {
    $(".history_link").css("cursor","pointer").click(function() {
        location.href = $(this).data("href");
    });
});

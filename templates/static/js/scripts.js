// script suavizar scroll de rolagem com links de navegacao  
$('.scrollll a[href^="#"]').on('click', function(e) {
    e.preventDefault();
    var id = $(this).attr('href'),
        targetOffset = $(id).offset().top;

    $('html, body').animate({
        scrollTop: targetOffset
    }, 1000);
});

 var p = window.location.pathname;
 console.log(p)
 // Adciona classe no header das internas
 if ((p !== "/index") && (p !== "/")){
    $("header").addClass("interna");
 } 

// script carregamento de pagina
$(window).on('load', function() {
    $('#preloader .inner').fadeOut();
    $('#preloader').delay(350).fadeOut('slow');
    $('body').delay(350).css({
        'overflow': 'visible'
    });
});

$('.owl-imoveis').owlCarousel({
    loop:false,
    margin:15,
    nav:true,
    dots:true,
    autoplay:false,
    autoplayTimeout:4000,
    autoplayHoverPause:true,
    navText:["<i class='fas fa-arrow-circle-left'></i>","<i class='fas fa-arrow-circle-right'></i>"],
    responsive:{
        0:{
            items:1
        },
        800:{
            items:2
        },
        1100:{
            items:3
        }
    }
});

$('#owl-corretores').owlCarousel({
    loop:false,
    margin:25,
    nav:false,
    dots:true,
    autoplay:false,
    autoplayTimeout:4000,
    autoplayHoverPause:true,
    responsive:{
        0:{
            items:2
        },
        800:{
            items:3
        },
        1200:{
            items:4
        }
    }
});

$('#owl-banner').owlCarousel({
    loop:true,
    margin:0,
    nav:false,
    animateIn: 'fadeIn',
    dots:true,
    autoplay:true,
    autoplayTimeout:8000,
    items:1
});
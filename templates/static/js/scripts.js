

// script suavizar scroll de rolagem com links de navegacao  
$('.scroll a[href^="#"]').on('click', function(e) {
    e.preventDefault();
    var id = $(this).attr('href'),
        targetOffset = $(id).offset().top;
    $('html, body').animate({
        scrollTop: targetOffset - 60
    }, 600);
    console.log(targetOffset)
});


console.log($( document ).height())
console.log($( window ).height())

var Bottom = $( document ).height() - $( window ).height() 

console.log(Bottom)

$(window).scroll(function() {
    if ($(document).scrollTop() > 800) {
        $('header.imovel').addClass('visible');
    } else {
        $('header.imovel').removeClass('visible');
    }
});

// Adciona classe "interna" no header das internas
var p = window.location.pathname;
if ((p !== "/index") && (p !== "/")){
    $("header.main").addClass("interna");
} 

// script do preloader no carregamento de pagina
$(window).on('load', function() {
    $('#preloader .inner').fadeOut();
    $('#preloader').delay(350).fadeOut('slow');
    $('body').delay(350).css({
        'overflow': 'visible'
    });
});

$('.owl-imoveis').owlCarousel({
    loop:false,
    margin:0,
    nav:true,
    dots:false,
    autoplay:true,
    autoplayTimeout:6000,
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
            items:5
        }
    }
});

$('#owl-imoveis-destaque').owlCarousel({
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
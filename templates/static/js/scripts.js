// script suavizar scroll de rolagem com links de navegacao  
$('.scrollll a[href^="#"]').on('click', function(e) {
    e.preventDefault();
    var id = $(this).attr('href'),
        targetOffset = $(id).offset().top;

    $('html, body').animate({
        scrollTop: targetOffset
    }, 1000);
});

// var p = window.location.pathname;
// console.log(p)
// // Adciona classe no header das internas
// if ((p !== "/imoveis/index.php") && (p !== "/imoveis/") && (p !== "/index.php") && (p !== "/")){
//     $("header").addClass("interna");
// } 

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
    navText:["<img src='./assets/img/icons/prev-btn.svg'>","<img src='./assets/img/icons/next-btn.svg'>"],
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

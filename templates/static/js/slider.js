$(function() {

    // Initiate Slider
    $('#slider-range').slider({
      range: true,
      min: 0,
      max: 18000000,
      step: 100,
      values: [500, 10000000]
    });
  
    // Move the range wrapper into the generated divs
    $('.ui-slider-range').append($('.range-wrapper'));
  
    // Apply initial values to the range container
    $('.range').html('<span class="range-value">$' + $('#slider-range').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value">$' + $("#slider-range").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  
  
    $('#slider-range').slider({
      slide: function(event, ui) {
  
        // Update the range container values upon sliding
  
        $('.range').html('<span class="range-value">$' + ui.values[0].toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value">$' + ui.values[1].toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  
        // Get old value
        var previousVal = parseInt($(this).data('value'));
  
        // Save new value
        $(this).data({
          'value': parseInt(ui.value)
        });
  
        if (ui.values[1] === 110000) {
          if (!$('.range-alert').hasClass('active')) {
            $('.range-alert').addClass('active');
          }
        } else {
          if ($('.range-alert').hasClass('active')) {
            $('.range-alert').removeClass('active');
          }
        }
      }
    });
  
    // Prevent the range container from moving the slider
    $('.range, .range-alert').on('mousedown', function(event) {
      event.stopPropagation();
    });
  
  });
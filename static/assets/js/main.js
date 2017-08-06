// SITE SCRIPTS

// Document Ready
$(function() {

console.log("Document Ready");

//*** Smooth scroll
$('a[href*="#"]:not([href="#"])').click(function() {
if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
  var target = $(this.hash);
  target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
  if (target.length) {
    $('html, body').animate({
      scrollTop: target.offset().top
    }, 1000);
    return false;
  }
}

});
  
$(window).resize(function() {
  //project_container.packery(isotope_properties);
});


}); // End of Document Ready


$(window).on('load', function(){
//*** Packery Layout settings
var project_container = $('.projects-row');
var isotope_properties = {
  itemSelector: '.project-block',
}
project_container.packery(isotope_properties);

//*** Search functionality
var $rows = $('.project-block');
$('.project-search').keyup(function() {

  // Reset tag search to all
  $('.tag-select').val('all');

  var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
  
  $rows.show().filter(function() {
      var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
      return !~text.indexOf(val);
  }).hide();

  if ( $('.project-block:visible').length == 0) {
    // nothing visible
    $('.noresults').show();
  } else {
    // a project is visible
    $('.noresults').hide();
    project_container.packery(isotope_properties);
  }
});

//*** Sorting functionality
$('.tag-select').on('change', function()  {
  var tag_selected = $(this).val();

  if (tag_selected == "all") {
    $('.project-block').each(function(index){
      $(this).show();
      project_container.packery(isotope_properties); // Reinit layout
    });
  } else {
    $('.project-block').each(function(index){
      if ($(this).attr('data-tag') != tag_selected) {
        $(this).hide();
      } else {
        $(this).show();
      }
      //console.log($(this).attr('data-tag'));
      project_container.packery(isotope_properties); // Reinit layout
    });
  }
});

  
  //*** Waves animation
var waves = new SineWaves({
  el: document.getElementById('waves'),
  speed: 1,

  width: function() {
    return $('.waves-overlay').width();
  },

  height: function() {
    return $('.waves-overlay').height();
  },

  ease: 'SineInOut',
  wavesWidth: '100%',

  waves: [
    {
      timeModifier: 4,
      lineWidth: 1,
      amplitude: -5,
      wavelength: 25
    },
    {
      timeModifier: 1,
      lineWidth: 1,
      amplitude: -10,
      wavelength: 100
    },
    {
      timeModifier: 2,
      lineWidth: 2,
      amplitude: -15,
      wavelength: 50
    },
    {
      timeModifier: 1,
      lineWidth: 1,
      amplitude: -20,
      wavelength: 100
    },
  ],

  // Called on window resize
  resizeEvent: function() {
    var gradient = this.ctx.createLinearGradient(0, 0, this.width, 0);
    //gradient.addColorStop(0,"rgba(23, 210, 168, 0.2)"); Old colors
    //gradient.addColorStop(0.5,"rgba(255, 255, 255, 0.5)");
    //gradient.addColorStop(1,"rgba(23, 210, 168, 0.2)");
    gradient.addColorStop(0,"rgba(255, 255, 255, 0)");
    gradient.addColorStop(0.4,"rgba(255, 127, 48, 0.3)");
    gradient.addColorStop(0.7,"rgba(255, 255, 255, 0)");

    var index = -1;
    var length = this.waves.length;
    while(++index < length){
      this.waves[index].strokeStyle = gradient;
    }

    // Clean Up
    index = void 0;
    length = void 0;
    gradient = void 0;
  }
});
  
project_container.packery(isotope_properties);

// Push menu button action
$('.push-menu-button').on("mousedown", function(){
  console.log("Side menu opened")
  $('body').toggleClass('menu-open');
  $('.push-menu').toggleClass('open'); 
})
  
}); // End of window loaded (Comes after Doc ready)

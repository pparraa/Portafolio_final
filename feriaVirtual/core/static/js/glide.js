window.addEventListener('load', function () {
    new Glider(document.querySelector('.slider__lista'), {
      slidesToShow: 1,
      slidesToScroll: 1,
      draggable: true,
      rewind:true,
      //dots: '.slider__indicadores',
      arrows: {
        prev: '.slider__anterior',
        next: '.slider__siguiente'
      },
      responsive: [
        {
          breakpoint: 1224,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3
          }
        }
      ]
    });
  });
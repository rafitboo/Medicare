document.addEventListener('DOMContentLoaded', function() {
  // Initialize category slider
  const categorySlider = document.querySelector('.category-slider');
  let isDown = false;
  let startX;
  let scrollLeft;

  categorySlider.addEventListener('mousedown', (e) => {
      isDown = true;
      startX = e.pageX - categorySlider.offsetLeft;
      scrollLeft = categorySlider.scrollLeft;
      categorySlider.style.cursor = 'grabbing';
  });

  categorySlider.addEventListener('mouseleave', () => {
      isDown = false;
      categorySlider.style.cursor = 'grab';
  });

  categorySlider.addEventListener('mouseup', () => {
      isDown = false;
      categorySlider.style.cursor = 'grab';
  });

  categorySlider.addEventListener('mousemove', (e) => {
      if(!isDown) return;
      e.preventDefault();
      const x = e.pageX - categorySlider.offsetLeft;
      const walk = (x - startX) * 2;
      categorySlider.scrollLeft = scrollLeft - walk;
  });

  // Initialize testimonial slider
  const testimonialSlider = document.querySelector('.testimonial-slider');
  let testimonialIsDown = false;
  let testimonialStartX;
  let testimonialScrollLeft;

  testimonialSlider.addEventListener('mousedown', (e) => {
      testimonialIsDown = true;
      testimonialStartX = e.pageX - testimonialSlider.offsetLeft;
      testimonialScrollLeft = testimonialSlider.scrollLeft;
      testimonialSlider.style.cursor = 'grabbing';
  });

  testimonialSlider.addEventListener('mouseleave', () => {
      testimonialIsDown = false;
      testimonialSlider.style.cursor = 'grab';
  });

  testimonialSlider.addEventListener('mouseup', () => {
      testimonialIsDown = false;
      testimonialSlider.style.cursor = 'grab';
  });

  testimonialSlider.addEventListener('mousemove', (e) => {
      if(!testimonialIsDown) return;
      e.preventDefault();
      const x = e.pageX - testimonialSlider.offsetLeft;
      const walk = (x - testimonialStartX) * 2;
      testimonialSlider.scrollLeft = testimonialScrollLeft - walk;
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
          e.preventDefault();
          document.querySelector(this.getAttribute('href')).scrollIntoView({
              behavior: 'smooth'
          });
      });
  });

  // Animation on scroll
  const animateOnScroll = () => {
      const elements = document.querySelectorAll('.feature-card, .category-card, .testimonial-card');
      
      elements.forEach(element => {
          const elementPosition = element.getBoundingClientRect().top;
          const screenPosition = window.innerHeight / 1.2;
          
          if(elementPosition < screenPosition) {
              element.style.opacity = '1';
              element.style.transform = 'translateY(0)';
          }
      });
  };

  // Set initial state for animation
  const featureCards = document.querySelectorAll('.feature-card, .category-card, .testimonial-card');
  featureCards.forEach(card => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  });

  window.addEventListener('scroll', animateOnScroll);
  animateOnScroll(); // Run once on load
});

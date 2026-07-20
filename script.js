// Theme Toggle Switcher (Dark / Light Mode)
document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide Icons
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }

  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  if (themeToggleBtn) {
    const icon = themeToggleBtn.querySelector('i');
    
    // Check local storage or default to dark
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
      if (theme === 'light') {
        icon.setAttribute('data-lucide', 'sun');
        themeToggleBtn.style.color = '#ffcf40'; // High-pop gold sun
      } else {
        icon.setAttribute('data-lucide', 'moon');
        themeToggleBtn.style.color = '#d4af37'; // Warm gold moon
      }
      if (typeof lucide !== 'undefined') {
        lucide.createIcons();
      }
    }
  }
});

// Sticky Navbar on Scroll
window.addEventListener('scroll', () => {
  const navbar = document.getElementById('navbar');
  if (navbar) {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }
});

// Mobile Navigation Panel Toggle
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const navCollapse = document.getElementById('navbarNav');
const navbar = document.getElementById('navbar');

if (mobileMenuBtn && navCollapse) {
  // Sync hamburger button and navbar backdrop states via Bootstrap collapse events
  navCollapse.addEventListener('show.bs.collapse', () => {
    mobileMenuBtn.classList.add('active');
    if (navbar) {
      navbar.classList.add('menu-open');
    }
  });

  navCollapse.addEventListener('hide.bs.collapse', () => {
    mobileMenuBtn.classList.remove('active');
    if (navbar) {
      navbar.classList.remove('menu-open');
    }
  });

  // Close navigation menu on link click via Bootstrap collapse hide
  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      if (window.bootstrap) {
        const bsCollapse = window.bootstrap.Collapse.getInstance(navCollapse) || new window.bootstrap.Collapse(navCollapse);
        bsCollapse.hide();
      }
    });
  });
}

// 3D Tilt Effect on Hero Bottle
const bottleWrap = document.getElementById('hero-bottle');
if (bottleWrap) {
  const bottleImg = bottleWrap.querySelector('img, video');
  
  bottleWrap.addEventListener('mousemove', (e) => {
    const rect = bottleWrap.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    
    // Normalize coordinates
    const normalizedX = x / (rect.width / 2);
    const normalizedY = y / (rect.height / 2);
    
    // 3D rotation angles
    const rotateY = normalizedX * 10;
    const rotateX = -normalizedY * 10;
    
    bottleImg.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
  });
  
  bottleWrap.addEventListener('mouseleave', () => {
    bottleImg.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
    bottleImg.style.transition = 'transform 0.6s ease';
  });
  
  bottleWrap.addEventListener('mouseenter', () => {
    bottleImg.style.transition = 'none';
  });
}

// 3D Tilt Effect on Mission Pedestal Card
const missionCard = document.getElementById('mission-bottle-card');
if (missionCard) {
  const missionImg = missionCard.querySelector('img');
  
  missionCard.addEventListener('mousemove', (e) => {
    const rect = missionCard.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    
    const normalizedX = x / (rect.width / 2);
    const normalizedY = y / (rect.height / 2);
    
    const rotateY = normalizedX * 8;
    const rotateX = -normalizedY * 8;
    
    missionImg.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
  });
  
  missionCard.addEventListener('mouseleave', () => {
    missionImg.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
    missionImg.style.transition = 'transform 0.6s ease';
  });
  
  missionCard.addEventListener('mouseenter', () => {
    missionImg.style.transition = 'none';
  });
}

// Testimonials Carousel Logic
const track = document.getElementById('testimonials-track');
const dots = document.querySelectorAll('.indicator-dot');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

if (track && dots.length > 0) {
  let currentSlide = 0;
  const maxSlides = dots.length;

  const updateCarousel = (index) => {
    currentSlide = index;
    const isMobile = window.innerWidth <= 768;
    const isTablet = window.innerWidth > 768 && window.innerWidth <= 1024;
    
    if (isMobile) {
      track.style.transform = `translateX(calc(-${currentSlide} * (100% + 1.5rem)))`;
    } else if (isTablet) {
      track.style.transform = `translateX(calc(-${currentSlide} * (50% + 0.75rem)))`;
    } else {
      track.style.transform = 'none'; // reset translation on desktop
    }

    dots.forEach((dot, idx) => {
      if (idx === currentSlide) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  };

  if (prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => {
      let idx = currentSlide - 1;
      if (idx < 0) idx = maxSlides - 1;
      updateCarousel(idx);
    });

    nextBtn.addEventListener('click', () => {
      let idx = currentSlide + 1;
      if (idx >= maxSlides) idx = 0;
      updateCarousel(idx);
    });
  }

  dots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      updateCarousel(idx);
    });
  });

  window.addEventListener('resize', () => {
    updateCarousel(currentSlide);
  });
}



// --- GSAP Premium Animations (ScrollTrigger & Interactive Hover) ---
if (typeof gsap !== 'undefined') {
  // Register ScrollTrigger plugin
  gsap.registerPlugin(ScrollTrigger);

  // Cinematic Hero Scroll-Linked Animations (Video scale up and Content blur out)
  if (window.innerWidth > 991) {
    gsap.to(".hero-bg-video-desktop", {
      scrollTrigger: {
        trigger: "#hero",
        start: "top top",
        end: "bottom 30%",
        scrub: true
      },
      xPercent: -50,
      yPercent: -50,
      left: "50%",
      top: "50%",
      scale: 1,
      opacity: 1,
      borderRadius: 0,
      ease: "none"
    });

    gsap.to(".hero .reveal-left, .hero .reveal-right", {
      scrollTrigger: {
        trigger: "#hero",
        start: "top top",
        end: "bottom 40%",
        scrub: true
      },
      opacity: 0,
      filter: "blur(12px)",
      y: -80,
      ease: "none"
    });
  } else {
    // Mobile layout content blurs and fades out on scroll
    gsap.to(".hero-mobile-layout", {
      scrollTrigger: {
        trigger: "#hero",
        start: "top top",
        end: "bottom 40%",
        scrub: true
      },
      opacity: 0,
      filter: "blur(12px)",
      y: -80,
      ease: "none"
    });
  }

  // 1. Hero Page-Load Animations
  const heroTL = gsap.timeline();
  // Animate left column content elements
  heroTL.fromTo(".hero .reveal-left", {
    x: -50,
    opacity: 0
  }, {
    x: 0,
    opacity: 1,
    duration: 1.2,
    ease: "power4.out"
  });
  // Animate middle mobile video wrapper
  heroTL.from(".hero-col-center", {
    y: 40,
    opacity: 0,
    duration: 1.2,
    ease: "power3.out"
  }, "-=1");
  // Animate right column content elements
  heroTL.fromTo(".hero .reveal-right", {
    x: 50,
    opacity: 0
  }, {
    x: 0,
    opacity: 1,
    duration: 1.2,
    ease: "power4.out"
  }, "-=1.2");
  // Left column small feature icons stagger
  heroTL.from(".hero-feat-icon-box", {
    scale: 0,
    opacity: 0,
    stagger: 0.1,
    duration: 0.6,
    ease: "back.out(2)"
  }, "-=0.8");
  // Right column features stagger
  heroTL.from(".hero-list-icon-box", {
    scale: 0,
    opacity: 0,
    stagger: 0.1,
    duration: 0.6,
    ease: "back.out(2)"
  }, "-=0.8");

  // 2. Ingredients Staggered Entrance Timeline on Scroll
  const ingredientsTL = gsap.timeline({
    scrollTrigger: {
      trigger: "#ingredients",
      start: "top 75%",
      toggleActions: "play none none none"
    }
  });

  // Header animation
  ingredientsTL.fromTo(".ingredients-header", {
    y: 50,
    opacity: 0
  }, {
    y: 0,
    opacity: 1,
    duration: 1,
    ease: "power3.out"
  });

  // Center graphic and orbits pop
  ingredientsTL.fromTo(".luxury-grid-center", {
    scale: 0.9,
    opacity: 0
  }, {
    scale: 1,
    opacity: 1,
    duration: 1.2,
    ease: "back.out(1.5)"
  }, "-=0.6");

  ingredientsTL.from(".orbit-circle", {
    scale: 0,
    opacity: 0,
    stagger: 0.1,
    duration: 1,
    ease: "power2.out"
  }, "-=0.8");

  ingredientsTL.from(".orbit-node", {
    scale: 0,
    opacity: 0,
    stagger: 0.08,
    duration: 0.8,
    ease: "back.out(2)"
  }, "-=0.6");

  // Staggered slide-in from left for left column cards
  ingredientsTL.fromTo(".luxury-ingredients-grid .reveal-left", {
    x: -60,
    opacity: 0
  }, {
    x: 0,
    opacity: 1,
    stagger: 0.12,
    duration: 1,
    ease: "power3.out"
  }, "-=0.8");

  // Staggered slide-in from right for right column cards
  ingredientsTL.fromTo(".luxury-ingredients-grid .reveal-right", {
    x: 60,
    opacity: 0
  }, {
    x: 0,
    opacity: 1,
    stagger: 0.12,
    duration: 1,
    ease: "power3.out"
  }, "-=1");

  // Staggered bottom trust bar reveal
  ingredientsTL.fromTo(".luxury-feature-bar", {
    y: 30,
    opacity: 0
  }, {
    y: 0,
    opacity: 1,
    duration: 0.8,
    ease: "power3.out"
  }, "-=0.6");

  // 3. Mission Section Scroll Trigger (Replaced with Vanilla CSS transitions)


  // 4. Health Crisis Section Scroll Trigger
  const crisisTL = gsap.timeline({
    scrollTrigger: {
      trigger: "#crisis",
      start: "top 75%",
      toggleActions: "play none none none"
    }
  });
  crisisTL.from("#crisis .eyebrow", {
    y: 20,
    opacity: 0,
    duration: 0.6,
    ease: "power2.out"
  });
  crisisTL.from("#crisis .section-title-serif", {
    y: 30,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out"
  }, "-=0.4");
  crisisTL.fromTo("#crisis .bento-card", {
    scale: 0.9,
    opacity: 0
  }, {
    scale: 1,
    opacity: 1,
    stagger: 0.12,
    duration: 1,
    ease: "power3.out"
  }, "-=0.5");
  crisisTL.from(".crisis-callout-banner", {
    y: 30,
    opacity: 0,
    duration: 0.8,
    ease: "power2.out"
  }, "-=0.4");

  // 5. Science Section Scroll Trigger
  const scienceTL = gsap.timeline({
    scrollTrigger: {
      trigger: "#science",
      start: "top 75%",
      toggleActions: "play none none none"
    }
  });
  scienceTL.from("#science .eyebrow", {
    y: 20,
    opacity: 0,
    duration: 0.6,
    ease: "power2.out"
  });
  scienceTL.from("#science .section-title-serif", {
    y: 30,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out"
  }, "-=0.4");
  scienceTL.fromTo("#science .advantage-col", {
    y: 40,
    opacity: 0
  }, {
    y: 0,
    opacity: 1,
    stagger: 0.15,
    duration: 0.9,
    ease: "power3.out"
  }, "-=0.5");

  // 6. How to Use Section Scroll Trigger
  const storyTL = gsap.timeline({
    scrollTrigger: {
      trigger: "#story",
      start: "top 75%",
      toggleActions: "play none none none"
    }
  });
  storyTL.from("#story .section-title-serif", {
    y: 30,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out"
  });
  storyTL.fromTo("#story .step-new-card", {
    y: 45,
    opacity: 0
  }, {
    y: 0,
    opacity: 1,
    stagger: 0.15,
    duration: 0.9,
    ease: "power3.out"
  }, "-=0.5");

  // 7. Reviews & Trust Section Scroll Trigger
  const reviewsTL = gsap.timeline({
    scrollTrigger: {
      trigger: "#reviews",
      start: "top 75%",
      toggleActions: "play none none none"
    }
  });
  reviewsTL.from("#reviews .section-title-serif", {
    y: 30,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out"
  });
  reviewsTL.fromTo("#reviews .testimonial-card-mirror", {
    y: 40,
    opacity: 0
  }, {
    y: 0,
    opacity: 1,
    stagger: 0.15,
    duration: 0.9,
    ease: "power3.out"
  }, "-=0.5");
  reviewsTL.from("#reviews .trust-badge-item", {
    scale: 0.8,
    opacity: 0,
    stagger: 0.1,
    duration: 0.8,
    ease: "power2.out"
  }, "-=0.4");

  // 8. Order CTA Card Scroll Trigger
  gsap.fromTo(".cta-prefooter-card", {
    scale: 0.92,
    opacity: 0
  }, {
    scale: 1,
    opacity: 1,
    duration: 1.2,
    ease: "power3.out",
    scrollTrigger: {
      trigger: "#order",
      start: "top 80%",
      toggleActions: "play none none none"
    }
  });


  // 2. High-performance Smooth Mouse Parallax (deceleration-eased via GSAP)
  const ingredientsSec = document.getElementById('ingredients');
  const luxuryCenterBody = document.querySelector('.luxury-center-body-wrap');
  const luxuryRadialGlow = document.querySelector('.luxury-radial-glow');

  if (ingredientsSec && luxuryCenterBody) {
    ingredientsSec.addEventListener('mousemove', (e) => {
      const rect = ingredientsSec.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      
      const moveX = (x / rect.width) * 22; // max 22px translation
      const moveY = (y / rect.height) * 22;
      
      gsap.to(luxuryCenterBody, {
        x: moveX,
        y: moveY,
        duration: 0.7,
        ease: "power2.out",
        overwrite: "auto"
      });
      
      if (luxuryRadialGlow) {
        gsap.to(luxuryRadialGlow, {
          x: moveX * 0.5,
          y: moveY * 0.5,
          duration: 0.9,
          ease: "power2.out",
          overwrite: "auto"
        });
      }
    });

    ingredientsSec.addEventListener('mouseleave', () => {
      gsap.to(luxuryCenterBody, {
        x: 0,
        y: 0,
        duration: 0.8,
        ease: "power3.out",
        overwrite: "auto"
      });
      if (luxuryRadialGlow) {
        gsap.to(luxuryRadialGlow, {
          x: 0,
          y: 0,
          duration: 1,
          ease: "power3.out",
          overwrite: "auto"
        });
      }
    });
  }

  // 3. Butter-smooth 3D card tilt & hover state timelines via GSAP
  const luxuryCards = document.querySelectorAll('.luxury-ingredient-card');
  const orbitCircles = document.querySelectorAll('.orbit-circle');
  const radialGlowElement = document.querySelector('.luxury-radial-glow');

  luxuryCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      
      const normalizedX = x / (rect.width / 2);
      const normalizedY = y / (rect.height / 2);
      
      const rotateY = normalizedX * 6; // max 6deg Y-rotation
      const rotateX = -normalizedY * 6; // max 6deg X-rotation
      
      gsap.to(card, {
        rotateX: rotateX,
        rotateY: rotateY,
        y: -6,
        duration: 0.3,
        ease: "power1.out",
        transformPerspective: 800,
        overwrite: "auto"
      });
    });

    card.addEventListener('mouseenter', () => {
      // Animate background glow, borders, and box shadows on hover
      gsap.to(card, {
        borderColor: "rgba(212, 175, 55, 0.45)",
        backgroundColor: "rgba(255, 255, 255, 0.05)",
        boxShadow: "0 20px 45px rgba(0, 0, 0, 0.45), 0 0 25px rgba(212, 175, 55, 0.06)",
        duration: 0.3,
        overwrite: "auto"
      });

      // Animate arrow button filling gold
      const arrowBtn = card.querySelector('.card-arrow-btn');
      if (arrowBtn) {
        gsap.to(arrowBtn, {
          backgroundColor: "#D4AF37",
          borderColor: "#D4AF37",
          color: "#000000",
          boxShadow: "0 0 12px rgba(212, 175, 55, 0.4)",
          duration: 0.3
        });
      }

      // Animate card icon container scale
      const cardIcon = card.querySelector('.card-img-wrap');
      if (cardIcon) {
        gsap.to(cardIcon, {
          scale: 1.06,
          borderColor: "#D4AF37",
          boxShadow: "0 0 15px rgba(212, 175, 55, 0.35)",
          duration: 0.3
        });
      }

      // Speed up central orbit circles
      orbitCircles.forEach(circle => {
        circle.classList.add('speed-up');
      });

      // Pulse corresponding center orbit node
      const targetNodeClass = card.getAttribute('data-node');
      if (targetNodeClass) {
        const targetBadge = document.querySelector(`.${targetNodeClass} .orbit-icon-badge`);
        if (targetBadge) {
          gsap.to(targetBadge, {
            scale: 1.2,
            borderColor: "#ffffff",
            color: "#ffffff",
            boxShadow: "0 0 25px rgba(255, 255, 255, 0.5), inset 0 0 12px rgba(255, 255, 255, 0.2)",
            duration: 0.3,
            overwrite: "auto"
          });
        }
      }

      // Shift background radial lighting glow color
      const glowTheme = card.getAttribute('data-glow');
      if (radialGlowElement && glowTheme) {
        radialGlowElement.classList.add(`glow-${glowTheme}`);
      }
    });

    card.addEventListener('mouseleave', () => {
      // Reset card position and style
      gsap.to(card, {
        rotateX: 0,
        rotateY: 0,
        y: 0,
        borderColor: "rgba(255, 255, 255, 0.08)",
        backgroundColor: "rgba(255, 255, 255, 0.02)",
        boxShadow: "0 10px 30px rgba(0, 0, 0, 0.25)",
        duration: 0.5,
        ease: "power2.out",
        overwrite: "auto"
      });

      // Reset arrow button
      const arrowBtn = card.querySelector('.card-arrow-btn');
      if (arrowBtn) {
        gsap.to(arrowBtn, {
          backgroundColor: "transparent",
          borderColor: "rgba(255, 255, 255, 0.12)",
          color: "rgba(255, 255, 255, 0.7)",
          boxShadow: "none",
          duration: 0.4
        });
      }

      // Reset card icon container
      const cardIcon = card.querySelector('.card-img-wrap');
      if (cardIcon) {
        gsap.to(cardIcon, {
          scale: 1,
          borderColor: "rgba(212, 175, 55, 0.45)",
          boxShadow: "0 5px 15px rgba(0,0,0,0.3)",
          duration: 0.4
        });
      }

      // Reset orbit speed ups
      orbitCircles.forEach(circle => {
        circle.classList.remove('speed-up');
      });

      // Reset center orbit node pulse
      const targetNodeClass = card.getAttribute('data-node');
      if (targetNodeClass) {
        const targetBadge = document.querySelector(`.${targetNodeClass} .orbit-icon-badge`);
        if (targetBadge) {
          gsap.to(targetBadge, {
            scale: 1,
            borderColor: targetNodeClass.includes('top') && !targetNodeClass.includes('right') && !targetNodeClass.includes('left') ? "rgba(212, 175, 55, 0.55)" : "rgba(0, 255, 135, 0.45)",
            color: targetNodeClass.includes('top') && !targetNodeClass.includes('right') && !targetNodeClass.includes('left') ? "var(--primary-gold)" : "#00ff87",
            boxShadow: targetNodeClass.includes('top') && !targetNodeClass.includes('right') && !targetNodeClass.includes('left') ? "0 0 15px rgba(212, 175, 55, 0.22)" : "0 0 15px rgba(0, 255, 135, 0.15)",
            duration: 0.4,
            overwrite: "auto"
          });
        }
      }

      // Reset background glow color
      if (radialGlowElement) {
        radialGlowElement.classList.remove('glow-gold', 'glow-green');
      }
    });
  });
}

// Initialize Bootstrap Tooltips for Orbit nodes
if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  [...tooltipTriggerList].forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
}

// Spotlight cursor coordinates tracking for Magic UI / Aceternity UI spotlight cards
document.addEventListener('mousemove', (e) => {
  const spotlightCards = document.querySelectorAll('.spotlight-card');
  spotlightCards.forEach(card => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    // Only update style variables if mouse is near or inside the card to save performance
    if (x >= -100 && x <= rect.width + 100 && y >= -100 && y <= rect.height + 100) {
      card.style.setProperty('--spotlight-x', `${x}px`);
      card.style.setProperty('--spotlight-y', `${y}px`);
    }
  });
});


/* ==========================================================================
   INGREDIENT WHEEL COMPONENT INTERACTION LOGIC (COMPLETELY ISOLATED IIFE)
   ========================================================================== */
(function() {
  document.addEventListener('DOMContentLoaded', () => {
    const wheel = document.querySelector('.ingredient-wheel');
    if (!wheel) return;

    const scaler = document.querySelector('.wheel-scaler');
    const centerDisc = wheel.querySelector('.wheel-center-disc');
    const centerContent = wheel.querySelector('#wheel-center-content');
    const mouseGlow = wheel.querySelector('.center-mouse-glow');
    const items = wheel.querySelectorAll('.wheel-item');
    const itemsOrbit = wheel.querySelector('.wheel-items-orbit');
    const itemsInners = wheel.querySelectorAll('.wheel-item-inner');
    const orbitRadius = 295; // orbit radius in px
    
    let centerTimer = null; // Track text reset timeout

    // Disable CSS animations so our requestAnimationFrame rotation takes control
    if (itemsOrbit) itemsOrbit.style.animation = 'none';
    itemsInners.forEach(inner => inner.style.animation = 'none');

    // 1. Position the 12 circular ingredients along orbit
    items.forEach((item, index) => {
      const styleAttr = item.getAttribute('style') || '';
      const match = styleAttr.match(/--angle:\s*([0-9.]+)deg/);
      if (match) {
        const angleDeg = parseFloat(match[1]);
        const angleRad = angleDeg * (Math.PI / 180);
        
        // Calculate coordinate offsets
        const x = Math.cos(angleRad) * orbitRadius;
        const y = Math.sin(angleRad) * orbitRadius;
        
        item.style.setProperty('--x', `${x.toFixed(2)}px`);
        item.style.setProperty('--y', `${y.toFixed(2)}px`);
      }
      // Add staggered reveal transition delays
      item.style.setProperty('--reveal-delay', `${index * 0.06}s`);
    });

    // 2. High-performance requestAnimationFrame Rotation Loop with smooth deceleration on hover
    let currentAngle = 0;
    let targetSpeed = 0.12; // about 50s per full spin at 60fps
    let currentSpeed = 0.12;
    
    function updateRotation() {
      // Interpolate speed for smooth deceleration/acceleration
      currentSpeed += (targetSpeed - currentSpeed) * 0.08;
      currentAngle += currentSpeed;
      
      // Rotate the orbit container
      if (itemsOrbit) {
        itemsOrbit.style.transform = `rotate(${currentAngle}deg)`;
      }
      
      // Counter-rotate items to keep them upright
      itemsInners.forEach(inner => {
        inner.style.transform = `rotate(${-currentAngle}deg)`;
      });
      
      requestAnimationFrame(updateRotation);
    }
    requestAnimationFrame(updateRotation);

    // 3. Hover state triggers: change target rotation speed and update center text
    items.forEach(item => {
      item.addEventListener('mouseenter', () => {
        targetSpeed = 0.005; // almost pause rotation on hover
        
        const name = item.getAttribute('data-name') || '';
        const benefit = item.getAttribute('data-benefit') || '';
        
        if (centerTimer) clearTimeout(centerTimer);
        
        // Show hovered card detail in center
        if (centerContent) {
          centerContent.style.opacity = '0';
          setTimeout(() => {
            centerContent.innerHTML = `
              <div class="center-hover-name" style="font-family: var(--font-heading); font-size: 1.6rem; color: var(--primary-gold); font-weight: 700; margin-bottom: 0.2rem; filter: drop-shadow(0 0 5px rgba(212, 175, 55, 0.35));">${name}</div>
              <div class="center-divider" style="width: 50px; height: 1.5px; background: var(--primary-gold); margin: 0.4rem auto;"></div>
              <div class="center-hover-benefit" style="font-family: var(--font-sans); font-size: 0.85rem; color: rgba(255,255,255,0.75); text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700;">${benefit}</div>
            `;
            centerContent.style.opacity = '1';
          }, 150);
        }
      });
      
      item.addEventListener('mouseleave', () => {
        targetSpeed = 0.12; // resume full speed
        
        if (centerTimer) clearTimeout(centerTimer);
        centerTimer = setTimeout(resetCenterContent, 2000); // return to default text after 2s
      });
    });

    // Reset center disc back to default state
    function resetCenterContent() {
      if (centerContent) {
        centerContent.style.opacity = '0';
        setTimeout(() => {
          centerContent.innerHTML = `
            <!-- Default State View -->
            <h2 class="center-number">51</h2>
            <div class="center-divider"></div>
            <div class="center-title">Powerful</div>
            <div class="center-subtitle">Ingredients</div>
          `;
          centerContent.style.opacity = '1';
          // Count up the number again!
          animateCountUp();
        }, 150);
      }
    }

    // 4. Vanilla JS Smooth Count-up for the "51" Number
    function animateCountUp() {
      const numEl = wheel.querySelector('.center-number');
      const disc = wheel.querySelector('.wheel-center-disc');
      if (!numEl) return;
      
      let startValue = 0;
      const endValue = 51;
      const duration = 1800; // ms
      const startTime = performance.now();
      
      function updateCount(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Ease out quadratic progress
        const easeProgress = progress * (2 - progress);
        const currentValue = Math.floor(easeProgress * endValue);
        
        numEl.textContent = currentValue;
        
        if (progress < 1) {
          requestAnimationFrame(updateCount);
        } else {
          numEl.textContent = endValue;
        }
      }
      
      requestAnimationFrame(updateCount);
      
      // Disc pop scale transition
      if (disc) {
        disc.style.transform = 'scale(0.92)';
        disc.style.transition = 'none';
        disc.offsetHeight; // force reflow
        disc.style.transition = 'transform 1.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 1.2s, box-shadow 1.2s';
        disc.style.transform = 'scale(1)';
      }
    }

    // 5. Interactive Center mouse glow parallax tracking
    if (centerDisc && mouseGlow) {
      const interactiveWrap = wheel.querySelector('.wheel-interactive-wrap');
      centerDisc.addEventListener('mousemove', (e) => {
        const rect = centerDisc.getBoundingClientRect();
        const x = e.clientX - rect.left - 60; // offset half glow width
        const y = e.clientY - rect.top - 60;
        mouseGlow.style.opacity = '1';
        mouseGlow.style.transform = `translate(${x}px, ${y}px)`;
      });
      centerDisc.addEventListener('mouseleave', () => {
        mouseGlow.style.opacity = '0';
      });
    }

    // 6. Programmatically generate floating gold background particles
    const particlesContainer = wheel.querySelector('.wheel-particles');
    if (particlesContainer) {
      const count = 15;
      for (let i = 0; i < count; i++) {
        const p = document.createElement('div');
        p.className = 'wheel-particle';
        
        const size = Math.random() * 4 + 2; // 2px to 6px
        const x = Math.random() * 100; // %
        const y = Math.random() * 100; // %
        const duration = Math.random() * 8 + 6; // 6s to 14s
        const delay = Math.random() * -10; // offset start
        
        p.style.width = `${size}px`;
        p.style.height = `${size}px`;
        p.style.left = `${x}%`;
        p.style.top = `${y}%`;
        p.style.setProperty('--duration', `${duration}s`);
        p.style.setProperty('--delay', `${delay}s`);
        
        particlesContainer.appendChild(p);
      }
    }

    // 7. Responsive Scaling Calculations
    function resizeIngredientWheel() {
      const parentWidth = scaler.parentElement.clientWidth;
      let scale = 1;
      
      if (parentWidth < 850) {
        scale = parentWidth / 850;
      }
      
      scaler.style.transform = `scale(${scale})`;
    }
    
    window.addEventListener('resize', resizeIngredientWheel);
    setTimeout(resizeIngredientWheel, 300);
    setTimeout(resizeIngredientWheel, 600);

    // 8. Intersection Observer for Scroll Entrance reveals (no GSAP!)
    const missionSection = document.getElementById('mission');
    if (missionSection) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            missionSection.classList.add('section-active');
            wheel.classList.add('wheel-visible');
            animateCountUp();
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12 });
      observer.observe(missionSection);
    }
  });
})();

/* ==========================================================================
   SCIENCE ADVANTAGE SECTION PREMIUM ANIMATIONS MODULE
   ========================================================================== */
(function() {
  document.addEventListener('DOMContentLoaded', () => {
    const scienceSection = document.getElementById('science');
    if (!scienceSection) return;

    // 1. Heading Split-Word Reveal
    const heading = scienceSection.querySelector('.section-title-serif');
    if (heading) {
      const originalText = heading.innerHTML;
      const tempContainer = document.createElement('div');
      tempContainer.innerHTML = originalText;
      
      const processNode = (node) => {
        if (node.nodeType === Node.TEXT_NODE) {
          const words = node.nodeValue.split(/(\s+)/);
          const fragment = document.createDocumentFragment();
          
          words.forEach(word => {
            if (word.trim() === '') {
              fragment.appendChild(document.createTextNode(word));
            } else {
              const outer = document.createElement('span');
              outer.className = 'split-word-wrap';
              
              const inner = document.createElement('span');
              inner.className = 'split-word-inner';
              inner.textContent = word;
              
              outer.appendChild(inner);
              fragment.appendChild(outer);
            }
          });
          
          node.parentNode.replaceChild(fragment, node);
        } else if (node.nodeType === Node.ELEMENT_NODE) {
          Array.from(node.childNodes).forEach(processNode);
        }
      };
      
      Array.from(tempContainer.childNodes).forEach(processNode);
      heading.innerHTML = tempContainer.innerHTML;
      
      const inners = heading.querySelectorAll('.split-word-inner');
      inners.forEach((inner, idx) => {
        inner.style.setProperty('--word-delay', `${idx * 50}ms`);
      });
    }

    // 2. Scroll Entrance Reveal Observer
    const cards = scienceSection.querySelectorAll('.advantage-col');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          scienceSection.classList.add('section-active');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    observer.observe(scienceSection);

    // 3. 3D Tilt, Card Spotlight & Image Parallax Tracking
    cards.forEach(card => {
      const img = card.querySelector('.advantage-image-header img');
      
      card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        // Spotlight glow coordinates
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
        
        // 3D Tilt calculation (max 8 degrees)
        const width = rect.width;
        const height = rect.height;
        const centerX = width / 2;
        const centerY = height / 2;
        const rotateX = ((centerY - y) / centerY) * 8;
        const rotateY = ((x - centerX) / centerX) * 8;
        
        card.style.transform = `perspective(1000px) translateY(-12px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        
        // Image Parallax (max 6px translation opposite to cursor)
        if (img) {
          const px = ((x - centerX) / centerX) * -6;
          const py = ((y - centerY) / centerY) * -6;
          img.style.transform = `scale(1.08) translate(${px}px, ${py}px)`;
        }
      });
      
      card.addEventListener('mouseleave', () => {
        // Reset properties
        card.style.setProperty('--mouse-x', `-999px`);
        card.style.setProperty('--mouse-y', `-999px`);
        card.style.transform = `perspective(1000px) translateY(0) rotateX(0deg) rotateY(0deg)`;
        if (img) {
          img.style.transform = `scale(1) translate(0, 0)`;
        }
      });
    });

    // 4. Section Background Spotlight Tracking
    scienceSection.addEventListener('mousemove', e => {
      const rect = scienceSection.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      scienceSection.style.setProperty('--science-mouse-x', `${x}px`);
      scienceSection.style.setProperty('--science-mouse-y', `${y}px`);
    });

    // 5. High-Performance Canvas Particles
    const canvas = document.createElement('canvas');
    canvas.className = 'science-particles-canvas';
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '0';
    scienceSection.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    let width = canvas.width = scienceSection.offsetWidth;
    let height = canvas.height = scienceSection.offsetHeight;

    window.addEventListener('resize', () => {
      if (scienceSection) {
        width = canvas.width = scienceSection.offsetWidth;
        height = canvas.height = scienceSection.offsetHeight;
      }
    });

    const particles = [];
    const particleCount = 20;
    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 1.2 + 0.6,
        speedX: Math.random() * 0.15 - 0.075,
        speedY: Math.random() * -0.2 - 0.05, // Float upwards
        opacity: Math.random() * 0.35 + 0.1
      });
    }

    let isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change', e => {
      isReducedMotion = e.matches;
    });

    function drawParticles() {
      if (isReducedMotion) return;
      ctx.clearRect(0, 0, width, height);
      ctx.fillStyle = 'rgba(212, 175, 55, 0.45)';
      
      particles.forEach(p => {
        p.x += p.speedX;
        p.y += p.speedY;
        
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;
        
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.globalAlpha = p.opacity;
        ctx.fill();
      });
      
      requestAnimationFrame(drawParticles);
    }
    drawParticles();

    // 6. Magnetic Hover Effect for Buttons/Links
    const magnetics = scienceSection.querySelectorAll('.btn-magnetic, .magnetic-link');
    magnetics.forEach(btn => {
      btn.addEventListener('mousemove', e => {
        if (isReducedMotion) return;
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        btn.style.transform = `translate(${x * 0.35}px, ${y * 0.35}px)`;
      });
      btn.addEventListener('mouseleave', () => {
        btn.style.transform = `translate(0px, 0px)`;
      });
    });
  });
})();

/* ==========================================================================
   2026 FOOTER FIREFLIES PARTICLES & MOUSE PARALLAX MODULE
   ========================================================================== */
(function() {
  document.addEventListener('DOMContentLoaded', () => {
    const footer = document.getElementById('site-footer');
    if (!footer) return;

    // Mouse Parallax & Radial Glow
    footer.addEventListener('mousemove', (e) => {
      const rect = footer.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      footer.style.setProperty('--footer-mouse-x', `${x}px`);
      footer.style.setProperty('--footer-mouse-y', `${y}px`);

      // Mouse Parallax (max 5px shift)
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const shiftX = ((x - centerX) / centerX) * 5;
      const shiftY = ((y - centerY) / centerY) * 5;

      const mainGrid = footer.querySelector('.footer-main-grid');
      if (mainGrid) {
        mainGrid.style.transform = `translate(${shiftX.toFixed(2)}px, ${shiftY.toFixed(2)}px)`;
        mainGrid.style.transition = 'transform 0.2s ease-out';
      }
    });

    footer.addEventListener('mouseleave', () => {
      const mainGrid = footer.querySelector('.footer-main-grid');
      if (mainGrid) {
        mainGrid.style.transform = `translate(0px, 0px)`;
        mainGrid.style.transition = 'transform 0.6s ease';
      }
    });

    // Canvas Fireflies Particles
    const canvas = document.getElementById('footer-fireflies-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width = (canvas.width = footer.offsetWidth);
    let height = (canvas.height = footer.offsetHeight);

    window.addEventListener('resize', () => {
      if (footer) {
        width = canvas.width = footer.offsetWidth;
        height = canvas.height = footer.offsetHeight;
      }
    });

    const fireflies = [];
    const count = 30;

    for (let i = 0; i < count; i++) {
      fireflies.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 1.5 + 0.5,
        speedX: (Math.random() - 0.5) * 0.4,
        speedY: (Math.random() - 0.5) * 0.4,
        alpha: Math.random(),
        alphaSpeed: 0.005 + Math.random() * 0.015,
        color: Math.random() > 0.5 ? '#D4AF37' : '#8BC34A'
      });
    }

    let isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change', e => {
      isReducedMotion = e.matches;
    });

    function drawFireflies() {
      if (isReducedMotion) return;
      ctx.clearRect(0, 0, width, height);

      fireflies.forEach((f) => {
        f.x += f.speedX;
        f.y += f.speedY;
        f.alpha += f.alphaSpeed;

        if (f.alpha >= 1 || f.alpha <= 0.1) {
          f.alphaSpeed = -f.alphaSpeed;
        }

        if (f.x < 0) f.x = width;
        if (f.x > width) f.x = 0;
        if (f.y < 0) f.y = height;
        if (f.y > height) f.y = 0;

        ctx.save();
        ctx.beginPath();
        ctx.arc(f.x, f.y, f.radius, 0, Math.PI * 2);
        ctx.fillStyle = f.color;
        ctx.globalAlpha = Math.max(0, Math.min(1, f.alpha * 0.6));
        ctx.shadowBlur = 8;
        ctx.shadowColor = f.color;
        ctx.fill();
        ctx.restore();
      });

      requestAnimationFrame(drawFireflies);
    }

    drawFireflies();
  });
})();


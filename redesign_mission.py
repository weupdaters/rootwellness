import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Container
html = html.replace(
    '<div class="container-fluid px-4" style="position: relative; z-index: 1; max-width: 1700px; margin: 0 auto;">',
    '<div class="container px-4" style="position: relative; z-index: 1; max-width: 1400px; margin: 0 auto;">'
)

# 2. Update Left Column
old_left_col = r'''<div class="col-xl-4 col-lg-5 mb-5 mb-lg-0 reveal-left">.*?</div>\s*<!-- CENTER COLUMN: Orbit Wheel -->'''
new_left_col = '''<div class="col-xl-4 col-lg-5 mb-5 mb-lg-0">
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <i data-lucide="leaf" style="color: var(--primary-gold); width: 20px; height: 20px;"></i>
            <span style="color: var(--primary-gold); font-size: 0.85rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;">OUR MISSION</span>
          </div>
          <h2 class="mission-anim-heading" style="font-family: var(--font-heading); font-size: 3.2rem; font-weight: 700; color: #fff; line-height: 1.1; margin-bottom: 1.5rem;">
            A better world through <span style="color: var(--primary-gold);">natural wellness</span> solutions.
          </h2>
          <p class="mission-anim-text" style="color: #a0aab2; font-size: 1.05rem; line-height: 1.6; margin-bottom: 3rem;">
            A world where everyone has access to natural, effective and trustworthy wellness solutions for a better, healthier and happier life.
          </p>
          
          <!-- 4 Pillars Grid (1 row on desktop) -->
          <div class="mission-anim-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.8rem; text-align: center;">
            <div style="background: rgba(255,255,255,0.02); padding: 1rem 0.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); transition: all 0.3s ease;">
               <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(212,175,55,0.1); display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem auto; border: 1px solid rgba(212,175,55,0.2);">
                 <i data-lucide="globe-2" style="color: var(--primary-gold); width: 20px; height: 20px;"></i>
               </div>
               <h4 style="color: #fff; font-size: 0.75rem; font-weight: 700; margin-bottom: 0.3rem; text-transform: uppercase; font-family: var(--font-sans);">Global<br>Vision</h4>
            </div>
            <div style="background: rgba(255,255,255,0.02); padding: 1rem 0.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); transition: all 0.3s ease;">
               <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(212,175,55,0.1); display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem auto; border: 1px solid rgba(212,175,55,0.2);">
                 <i data-lucide="users" style="color: var(--primary-gold); width: 20px; height: 20px;"></i>
               </div>
               <h4 style="color: #fff; font-size: 0.75rem; font-weight: 700; margin-bottom: 0.3rem; text-transform: uppercase; font-family: var(--font-sans);">Impacting<br>Millions</h4>
            </div>
            <div style="background: rgba(255,255,255,0.02); padding: 1rem 0.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); transition: all 0.3s ease;">
               <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(212,175,55,0.1); display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem auto; border: 1px solid rgba(212,175,55,0.2);">
                 <i data-lucide="bar-chart-3" style="color: var(--primary-gold); width: 20px; height: 20px;"></i>
               </div>
               <h4 style="color: #fff; font-size: 0.75rem; font-weight: 700; margin-bottom: 0.3rem; text-transform: uppercase; font-family: var(--font-sans);">Building<br>Millions</h4>
            </div>
            <div style="background: rgba(255,255,255,0.02); padding: 1rem 0.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); transition: all 0.3s ease;">
               <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(212,175,55,0.1); display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem auto; border: 1px solid rgba(212,175,55,0.2);">
                 <i data-lucide="sprout" style="color: var(--primary-gold); width: 20px; height: 20px;"></i>
               </div>
               <h4 style="color: #fff; font-size: 0.75rem; font-weight: 700; margin-bottom: 0.3rem; text-transform: uppercase; font-family: var(--font-sans);">Better<br>Tomorrow</h4>
            </div>
          </div>
        </div>
        <!-- CENTER COLUMN: Orbit Wheel -->'''
html = re.sub(old_left_col, new_left_col, html, flags=re.DOTALL)

# 3. Update Button in Center Column
old_btn = r'''<a href="#ingredients" class="btn-explore-formula".*?</a>'''
new_btn = '''<a href="#ingredients" class="btn-explore-formula" style="display: inline-flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
              EXPLORE INGREDIENTS <i data-lucide="arrow-right" style="margin-left: 8px; width: 18px; height: 18px;"></i>
            </a>'''
html = re.sub(old_btn, new_btn, html, flags=re.DOTALL)

# 4. Update Right Column
old_right_col = r'''<!-- RIGHT COLUMN: Stats Blocks -->.*?</div>\s*</div>\s*</div>\s*</section>'''
new_right_col = '''<!-- RIGHT COLUMN: Stats Blocks -->
        <div class="col-xl-4 col-lg-12 right-stats-col">
          <div class="stats-panel mission-anim-panel" style="background: linear-gradient(145deg, rgba(212,175,55,0.06), rgba(0,255,135,0.01)); border: 1px solid rgba(212,175,55,0.2); border-radius: 16px; padding: 2rem 1rem; margin-bottom: 1.2rem; backdrop-filter: blur(15px); display: flex; justify-content: space-around; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.4), inset 0 0 20px rgba(255,255,255,0.02);">
             <div>
                <i data-lucide="brain" style="color: var(--primary-gold); width: 28px; height: 28px; margin-bottom: 0.8rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.8rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="17">0</span>+</h3>
                <p style="color: #a0aab2; font-size: 0.65rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Vitamins &<br>Minerals</p>
             </div>
             <div style="width: 1px; background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.1), transparent);"></div>
             <div>
                <i data-lucide="leaf" style="color: var(--primary-gold); width: 28px; height: 28px; margin-bottom: 0.8rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.8rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="16">0</span>+</h3>
                <p style="color: #a0aab2; font-size: 0.65rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Plant Based<br>Extracts</p>
             </div>
             <div style="width: 1px; background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.1), transparent);"></div>
             <div>
                <i data-lucide="sparkles" style="color: var(--primary-gold); width: 28px; height: 28px; margin-bottom: 0.8rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.8rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="12">0</span>+</h3>
                <p style="color: #a0aab2; font-size: 0.65rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Antioxidant<br>Superfoods</p>
             </div>
          </div>

          <div class="stats-panel mission-anim-panel" style="background: linear-gradient(145deg, rgba(212,175,55,0.06), rgba(0,255,135,0.01)); border: 1px solid rgba(212,175,55,0.2); border-radius: 16px; padding: 2rem 0.5rem; margin-bottom: 1.2rem; backdrop-filter: blur(15px); display: flex; justify-content: space-around; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.4), inset 0 0 20px rgba(255,255,255,0.02);">
             <div>
                <i data-lucide="dna" style="color: var(--primary-gold); width: 24px; height: 24px; margin-bottom: 0.8rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.6rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="6">0</span>+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Amino Acids<br>& Enzymes</p>
             </div>
             <div style="width: 1px; background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.1), transparent);"></div>
             <div>
                <i data-lucide="activity" style="color: var(--primary-gold); width: 24px; height: 24px; margin-bottom: 0.8rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.6rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="8">0</span>+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Digestive<br>Supports</p>
             </div>
             <div style="width: 1px; background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.1), transparent);"></div>
             <div>
                <i data-lucide="dumbbell" style="color: var(--primary-gold); width: 24px; height: 24px; margin-bottom: 0.8rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.6rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="7">0</span>+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Performance<br>Boosters</p>
             </div>
             <div style="width: 1px; background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.1), transparent);"></div>
             <div>
                <i data-lucide="flower2" style="color: var(--primary-gold); width: 24px; height: 24px; margin-bottom: 0.8rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.6rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="3">0</span>+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Specialty<br>Nutrients</p>
             </div>
          </div>

          <div class="stats-panel mission-anim-panel" style="background: linear-gradient(145deg, rgba(212,175,55,0.06), rgba(0,255,135,0.01)); border: 1px solid rgba(212,175,55,0.2); border-radius: 16px; padding: 1.5rem 0.5rem; backdrop-filter: blur(15px); display: flex; justify-content: space-around; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.4), inset 0 0 20px rgba(255,255,255,0.02);">
             <div>
                <i data-lucide="leaf" style="color: var(--primary-gold); width: 20px; height: 20px; margin-bottom: 0.5rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.2rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="100">0</span>%</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Natural</p>
             </div>
             <div>
                <i data-lucide="medal" style="color: var(--primary-gold); width: 20px; height: 20px; margin-bottom: 0.5rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.2rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">1<span style="font-size: 0.7rem; vertical-align: top;">st</span></h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Premium<br>Quality</p>
             </div>
             <div>
                <i data-lucide="flask-conical" style="color: var(--primary-gold); width: 20px; height: 20px; margin-bottom: 0.5rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.2rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);"><span class="mission-stat" data-target="10">0</span>x</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Science<br>Backed</p>
             </div>
             <div>
                <i data-lucide="sprout" style="color: var(--primary-gold); width: 20px; height: 20px; margin-bottom: 0.5rem; filter: drop-shadow(0 0 8px rgba(212,175,55,0.4));"></i>
                <h3 style="color: #fff; font-size: 1.2rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">A+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Nature's<br>Finest</p>
             </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Mission Animations Script -->
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        if(typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
          gsap.registerPlugin(ScrollTrigger);
          
          // Animate left side text
          gsap.from(".mission-anim-heading", {
            scrollTrigger: {
              trigger: "#mission",
              start: "top 70%"
            },
            y: 30,
            opacity: 0,
            duration: 1,
            ease: "power3.out"
          });
          
          gsap.from(".mission-anim-text", {
            scrollTrigger: {
              trigger: "#mission",
              start: "top 65%"
            },
            y: 20,
            opacity: 0,
            duration: 1,
            delay: 0.2,
            ease: "power3.out"
          });
          
          gsap.from(".mission-anim-grid > div", {
            scrollTrigger: {
              trigger: "#mission",
              start: "top 60%"
            },
            y: 20,
            opacity: 0,
            duration: 0.8,
            stagger: 0.1,
            ease: "power2.out"
          });
          
          // Animate right side panels
          gsap.from(".mission-anim-panel", {
            scrollTrigger: {
              trigger: "#mission",
              start: "top 60%"
            },
            x: 30,
            opacity: 0,
            duration: 1,
            stagger: 0.2,
            ease: "power3.out"
          });
          
          // Animate numbers
          const stats = document.querySelectorAll(".mission-stat");
          stats.forEach(stat => {
            const target = parseInt(stat.getAttribute("data-target"));
            ScrollTrigger.create({
              trigger: stat,
              start: "top 80%",
              onEnter: () => {
                let count = 0;
                let duration = 2000; // 2 seconds
                let stepTime = Math.abs(Math.floor(duration / target));
                if(stepTime < 20) stepTime = 20; // max 50fps
                
                let timer = setInterval(() => {
                  count++;
                  stat.innerText = count;
                  if(count >= target) {
                    clearInterval(timer);
                    stat.innerText = target;
                  }
                }, stepTime);
              }
            });
          });
        }
      });
    </script>
  </section>'''
html = re.sub(old_right_col, new_right_col, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("Mission section redesigned!")

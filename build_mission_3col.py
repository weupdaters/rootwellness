import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Extract the wheel HTML
wheel_match = re.search(r'<div class="wheel-scaler">.*?<!-- Closes \.wheel-scaler -->', html, re.DOTALL)
if not wheel_match:
    print("Could not find the wheel HTML!")
    exit(1)
    
wheel_html = wheel_match.group(0)

# 2. Build the new Mission section
new_mission_html = f"""  <!-- Mission Section -->
  <section class="section" id="mission" style="background-color: var(--bg-secondary); overflow: hidden; position: relative; padding: 6rem 0;">
    <!-- Magic UI Dot Background Pattern -->
    <div class="magic-dot-pattern"></div>

    <div class="container-fluid px-4" style="position: relative; z-index: 1; max-width: 1700px; margin: 0 auto;">
      <div class="row align-items-center">
        <!-- LEFT COLUMN: Content -->
        <div class="col-xl-4 col-lg-5 mb-5 mb-lg-0 reveal-left">
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <i data-lucide="leaf" style="color: var(--primary-gold); width: 20px; height: 20px;"></i>
            <span style="color: var(--primary-gold); font-size: 0.85rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;">OUR MISSION</span>
          </div>
          <h2 style="font-family: var(--font-heading); font-size: 3.2rem; font-weight: 700; color: #fff; line-height: 1.1; margin-bottom: 1.5rem;">
            A better world through <span style="color: var(--primary-gold);">natural wellness</span> solutions.
          </h2>
          <p style="color: #a0aab2; font-size: 1.05rem; line-height: 1.6; margin-bottom: 3rem;">
            A world where everyone has access to natural, effective and trustworthy wellness solutions for a better, healthier and happier life.
          </p>
          
          <!-- 4 Pillars Grid (1 row on desktop) -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; text-align: center;">
            <div>
               <i data-lucide="globe-2" style="color: var(--primary-gold); width: 36px; height: 36px; margin-bottom: 0.5rem;"></i>
               <h4 style="color: var(--primary-gold); font-size: 0.75rem; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase; font-family: var(--font-heading);">Global<br>Vision</h4>
               <p style="color: #a0aab2; font-size: 0.7rem; line-height: 1.3; margin: 0;">Think Global<br>Act Local</p>
            </div>
            <div>
               <i data-lucide="users" style="color: var(--primary-gold); width: 36px; height: 36px; margin-bottom: 0.5rem;"></i>
               <h4 style="color: var(--primary-gold); font-size: 0.75rem; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase; font-family: var(--font-heading);">Impacting<br>Millions</h4>
               <p style="color: #a0aab2; font-size: 0.7rem; line-height: 1.3; margin: 0;">Creating Impact<br>That Matters</p>
            </div>
            <div>
               <i data-lucide="bar-chart-3" style="color: var(--primary-gold); width: 36px; height: 36px; margin-bottom: 0.5rem;"></i>
               <h4 style="color: var(--primary-gold); font-size: 0.75rem; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase; font-family: var(--font-heading);">Building<br>Millions</h4>
               <p style="color: #a0aab2; font-size: 0.7rem; line-height: 1.3; margin: 0;">Building Wealth<br>Building Futures</p>
            </div>
            <div>
               <i data-lucide="sprout" style="color: var(--primary-gold); width: 36px; height: 36px; margin-bottom: 0.5rem;"></i>
               <h4 style="color: var(--primary-gold); font-size: 0.75rem; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase; font-family: var(--font-heading);">Building A<br>Better Tomorrow</h4>
               <p style="color: #a0aab2; font-size: 0.7rem; line-height: 1.3; margin: 0;">Together for a<br>Better World</p>
            </div>
          </div>
        </div>

        <!-- CENTER COLUMN: Orbit Wheel -->
        <div class="col-xl-4 col-lg-7 mb-5 mb-lg-0 d-flex justify-content-center align-items-center flex-column position-relative">
          <!-- Inject the Wheel HTML here -->
          <div style="position: absolute; top: -40px; width: 100%; text-align: center; z-index: 10;">
             <div style="display: flex; align-items: center; justify-content: center; gap: 0.5rem; margin-bottom: 0.3rem;">
               <i data-lucide="leaf" style="color: var(--primary-gold); width: 24px; height: 24px;"></i>
               <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin: 0; letter-spacing: 0.05em;">51 POWERFUL INGREDIENTS</h3>
               <i data-lucide="leaf" style="color: var(--primary-gold); width: 24px; height: 24px; transform: scaleX(-1);"></i>
             </div>
             <p style="color: var(--primary-gold); font-size: 0.8rem; letter-spacing: 0.15em; font-weight: 600; text-transform: uppercase; margin: 0;">Nature &bull; Science &bull; Complete Nutrition</p>
          </div>
          
          <div style="transform: scale(0.85); transform-origin: center center; margin-top: 10px;">
             {wheel_html}
          </div>
          
          <div style="margin-top: -30px; text-align: center; z-index: 10;">
            <a href="#ingredients" class="btn-explore-formula" style="display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #4A7A25 0%, #2A4A15 100%); color: white; padding: 12px 30px; border-radius: 50px; font-weight: 600; font-size: 0.9rem; text-decoration: none; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 10px 30px rgba(0,0,0,0.5); transition: all 0.3s ease;">
              EXPLORE INGREDIENTS <i data-lucide="arrow-right" style="margin-left: 8px; width: 18px; height: 18px;"></i>
            </a>
          </div>
        </div>

        <!-- RIGHT COLUMN: Stats Blocks -->
        <div class="col-xl-4 col-lg-12 right-stats-col">
          <div class="stats-panel" style="background: rgba(4,10,6,0.6); border: 1px solid rgba(212,175,55,0.15); border-radius: 12px; padding: 2rem 1rem; margin-bottom: 1.2rem; backdrop-filter: blur(10px); display: flex; justify-content: space-around; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
             <div>
                <i data-lucide="brain" style="color: var(--primary-gold); width: 32px; height: 32px; margin-bottom: 0.8rem;"></i>
                <h3 style="color: #fff; font-size: 1.8rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">17+</h3>
                <p style="color: #a0aab2; font-size: 0.65rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Vitamins &<br>Minerals</p>
             </div>
             <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
             <div>
                <i data-lucide="leaf" style="color: var(--primary-gold); width: 32px; height: 32px; margin-bottom: 0.8rem;"></i>
                <h3 style="color: #fff; font-size: 1.8rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">16+</h3>
                <p style="color: #a0aab2; font-size: 0.65rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Plant Based<br>Extracts</p>
             </div>
             <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
             <div>
                <i data-lucide="sparkles" style="color: var(--primary-gold); width: 32px; height: 32px; margin-bottom: 0.8rem;"></i>
                <h3 style="color: #fff; font-size: 1.8rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">12+</h3>
                <p style="color: #a0aab2; font-size: 0.65rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Antioxidant<br>Superfoods</p>
             </div>
          </div>

          <div class="stats-panel" style="background: rgba(4,10,6,0.6); border: 1px solid rgba(212,175,55,0.15); border-radius: 12px; padding: 2rem 0.5rem; margin-bottom: 1.2rem; backdrop-filter: blur(10px); display: flex; justify-content: space-around; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
             <div>
                <i data-lucide="dna" style="color: var(--primary-gold); width: 28px; height: 28px; margin-bottom: 0.8rem;"></i>
                <h3 style="color: #fff; font-size: 1.6rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">6+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Amino Acids<br>& Enzymes</p>
             </div>
             <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
             <div>
                <i data-lucide="activity" style="color: var(--primary-gold); width: 28px; height: 28px; margin-bottom: 0.8rem;"></i>
                <h3 style="color: #fff; font-size: 1.6rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">8+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Digestive<br>Supports</p>
             </div>
             <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
             <div>
                <i data-lucide="dumbbell" style="color: var(--primary-gold); width: 28px; height: 28px; margin-bottom: 0.8rem;"></i>
                <h3 style="color: #fff; font-size: 1.6rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">7+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Performance<br>Boosters</p>
             </div>
             <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
             <div>
                <i data-lucide="flower2" style="color: var(--primary-gold); width: 28px; height: 28px; margin-bottom: 0.8rem;"></i>
                <h3 style="color: #fff; font-size: 1.6rem; font-weight: 700; margin: 0 0 0.2rem 0; font-family: var(--font-heading);">3+</h3>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Specialty<br>Nutrients</p>
             </div>
          </div>

          <div class="stats-panel" style="background: rgba(4,10,6,0.6); border: 1px solid rgba(212,175,55,0.15); border-radius: 12px; padding: 1.5rem 0.5rem; backdrop-filter: blur(10px); display: flex; justify-content: space-around; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
             <div>
                <i data-lucide="leaf" style="color: var(--primary-gold); width: 24px; height: 24px; margin-bottom: 0.5rem;"></i>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">100%<br>Natural</p>
             </div>
             <div>
                <i data-lucide="medal" style="color: var(--primary-gold); width: 24px; height: 24px; margin-bottom: 0.5rem;"></i>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Premium<br>Quality</p>
             </div>
             <div>
                <i data-lucide="flask-conical" style="color: var(--primary-gold); width: 24px; height: 24px; margin-bottom: 0.5rem;"></i>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Science<br>Backed</p>
             </div>
             <div>
                <i data-lucide="sprout" style="color: var(--primary-gold); width: 24px; height: 24px; margin-bottom: 0.5rem;"></i>
                <p style="color: #a0aab2; font-size: 0.6rem; text-transform: uppercase; font-weight: 600; margin: 0; line-height: 1.3; letter-spacing: 0.5px;">Made With<br>Nature's Finest</p>
             </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""

# Find the boundaries of the old Mission section
start_marker = '<!-- Mission Section -->'
end_marker = '<!-- Closes .wheel-scaler -->'

start_idx = html.find(start_marker)
if start_idx == -1:
    print("Could not find start marker")
    exit(1)

# Find where the section actually closes after wheel-scaler
end_idx = html.find('</section>', start_idx) + len('</section>')

if end_idx < len('</section>'):
    print("Could not find end marker")
    exit(1)
    
updated_html = html[:start_idx] + new_mission_html + html[end_idx:]

with open('index.html', 'w') as f:
    f.write(updated_html)

print("Mission section updated successfully to 3-column layout!")

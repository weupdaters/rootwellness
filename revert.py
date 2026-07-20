import re

# 1. Revert HTML
with open('index.html', 'r') as f:
    content = f.read()

pattern = re.compile(r'<!-- Pure Nutrition\\. Real Results Section \\(Badeyan / Rooton Organics Reference Layout\\) -->\\s*<section class="section" id="crisis".*?</section>', re.DOTALL)
old_html = """<section class="section crisis-section" id="crisis" style="background: #040A06; position: relative; overflow: hidden; padding: 6rem 0; min-height: 800px;">
    
    <!-- Centered Header -->
    <div class="container crisis-header-container" style="position: relative; z-index: 2; text-align: center; max-width: 800px; margin: 0 auto 4rem auto;">
      <div style="color: var(--primary-gold); font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center; justify-content: center; gap: 0.8rem;">
        <span style="display: inline-block; width: 40px; height: 1px; background: var(--primary-gold);"></span> THE MODERN HEALTH CRISIS <span style="display: inline-block; width: 40px; height: 1px; background: var(--primary-gold);"></span>
      </div>
      <h2 class="crisis-hero-title" style="font-family: var(--font-heading); font-size: 3.5rem; margin-top: 0; color: #fff; line-height: 1.1; font-weight: 700;">
        Why Do We Feel <span style="color: var(--primary-gold);">Tired</span> Everyday?
      </h2>
      <p class="crisis-hero-desc" style="color: #a0aab2; font-size: 1.05rem; margin-top: 1.5rem; margin-bottom: 0; line-height: 1.6;">
        Modern lifestyle is silently draining your health.<br>
        Fifty One fills the <span style="color: var(--primary-gold);">nutritional gaps</span> your body needs.
      </p>
    </div>

    <div class="container crisis-content-container" style="position: relative; z-index: 2; display: flex; align-items: center; justify-content: center; max-width: 1400px; width: 95%; gap: 3rem;">
        
        <!-- Right Side Visuals (Tired Man + Cards) -->
        <div class="crisis-visual-area" style="flex: 0 0 100%; position: relative; min-height: 600px; display: flex; align-items: center; justify-content: center; max-width: 650px;">
          
          <!-- The background image of the man (popping out of ring) -->
          <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -45%); width: 110%; height: 120%; z-index: 3; display: flex; align-items: center; justify-content: center; -webkit-mask-image: linear-gradient(to bottom, black 75%, transparent 100%); mask-image: linear-gradient(to bottom, black 75%, transparent 100%);">
              <img src="assets/crisis_bg.png" alt="Tired man background" style="width: 100%; height: 100%; object-fit: contain; filter: brightness(1.25) drop-shadow(0 -10px 40px rgba(212, 175, 55, 0.25));">
          </div>
          
          <!-- Glowing Ring -->
          <div class="glowing-ring" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 75%; aspect-ratio: 1; border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 50%; box-shadow: 0 0 20px rgba(212, 175, 55, 0.2), inset 0 0 20px rgba(212, 175, 55, 0.2); z-index: 2;"></div>

          <!-- Left Side Floating Cards -->
          <!-- Top Left: Poor Sleep -->
          <div class="crisis-circle-card" style="position: absolute; top: 5%; left: 8%; width: 110px; text-align: center; z-index: 5; animation: floatCard 4s ease-in-out infinite;">
            <div style="width: 70px; height: 70px; margin: 0 auto 0.5rem auto; border: 2px solid var(--primary-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.6); box-shadow: 0 0 15px rgba(212, 175, 55, 0.4); backdrop-filter: blur(5px);">
              <i data-lucide="moon" style="width: 32px; height: 32px; color: var(--primary-gold);"></i>
            </div>
            <h4 style="font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; color: #fff; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; line-height: 1.3;">Poor<br>Sleep</h4>
          </div>

          <!-- Middle Left: Low Energy -->
          <div class="crisis-circle-card" style="position: absolute; top: 40%; left: -2%; width: 110px; text-align: center; z-index: 5; animation: floatCard 4s ease-in-out 1s infinite;">
            <div style="width: 70px; height: 70px; margin: 0 auto 0.5rem auto; border: 2px solid var(--primary-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.6); box-shadow: 0 0 15px rgba(212, 175, 55, 0.4); backdrop-filter: blur(5px);">
              <i data-lucide="battery-low" style="width: 32px; height: 32px; color: var(--primary-gold);"></i>
            </div>
            <h4 style="font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; color: #fff; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; line-height: 1.3;">Low<br>Energy</h4>
          </div>

          <!-- Bottom Left: Pollution & Toxins -->
          <div class="crisis-circle-card" style="position: absolute; bottom: 5%; left: 8%; width: 110px; text-align: center; z-index: 5; animation: floatCard 4s ease-in-out 2s infinite;">
            <div style="width: 70px; height: 70px; margin: 0 auto 0.5rem auto; border: 2px solid var(--primary-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.6); box-shadow: 0 0 15px rgba(212, 175, 55, 0.4); backdrop-filter: blur(5px);">
              <i data-lucide="flask-conical" style="width: 32px; height: 32px; color: var(--primary-gold);"></i>
            </div>
            <h4 style="font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; color: #fff; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; line-height: 1.3;">Pollution<br>& Toxins</h4>
          </div>

          <!-- Right Side Floating Cards -->
          <!-- Top Right: Stress & Anxiety -->
          <div class="crisis-circle-card" style="position: absolute; top: 5%; right: 8%; width: 110px; text-align: center; z-index: 5; animation: floatCard 4s ease-in-out 0.5s infinite;">
            <div style="width: 70px; height: 70px; margin: 0 auto 0.5rem auto; border: 2px solid var(--primary-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.6); box-shadow: 0 0 15px rgba(212, 175, 55, 0.4); backdrop-filter: blur(5px);">
              <i data-lucide="brain" style="width: 32px; height: 32px; color: var(--primary-gold);"></i>
            </div>
            <h4 style="font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; color: #fff; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; line-height: 1.3;">Stress &<br>Anxiety</h4>
          </div>

          <!-- Middle Right: Excess Screen Time -->
          <div class="crisis-circle-card" style="position: absolute; top: 40%; right: -2%; width: 110px; text-align: center; z-index: 5; animation: floatCard 4s ease-in-out 1.5s infinite;">
            <div style="width: 70px; height: 70px; margin: 0 auto 0.5rem auto; border: 2px solid var(--primary-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.6); box-shadow: 0 0 15px rgba(212, 175, 55, 0.4); backdrop-filter: blur(5px);">
              <i data-lucide="smartphone" style="width: 32px; height: 32px; color: var(--primary-gold);"></i>
            </div>
            <h4 style="font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; color: #fff; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; line-height: 1.3;">Excess<br>Screen Time</h4>
          </div>

          <!-- Bottom Right: Poor Nutrition -->
          <div class="crisis-circle-card" style="position: absolute; bottom: 5%; right: 8%; width: 110px; text-align: center; z-index: 5; animation: floatCard 4s ease-in-out 2.5s infinite;">
            <div style="width: 70px; height: 70px; margin: 0 auto 0.5rem auto; border: 2px solid var(--primary-gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.6); box-shadow: 0 0 15px rgba(212, 175, 55, 0.4); backdrop-filter: blur(5px);">
              <i data-lucide="cookie" style="width: 32px; height: 32px; color: var(--primary-gold);"></i>
            </div>
            <h4 style="font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; color: #fff; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; line-height: 1.3;">Poor<br>Nutrition</h4>
          </div>
          
        </div>
    </div>
  </section>"""

updated_content = pattern.sub(old_html, content)
with open('index.html', 'w') as f:
    f.write(updated_content)

print("Crisis section restored to new design!")

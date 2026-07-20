import re

with open('index.html', 'r') as f:
    content = f.read()

# We need to replace everything from:
#   <section class="section crisis-section" id="crisis" ...>
# up to:
#   </section>

# Using regex to find the section
pattern = re.compile(r'<section class="section crisis-section" id="crisis"[^>]*>.*?</section>', re.DOTALL)

new_html = """  <!-- 2026 UI/UX Redesign: Modern Health Crisis Section -->
  <section class="cinematic-section" id="crisis">
    <div class="cinematic-ambient-glow"></div>
    
    <div class="cinematic-title-container">
      <div style="color: var(--primary-gold); font-size: 0.85rem; letter-spacing: 0.3em; text-transform: uppercase; font-weight: 700; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center; gap: 1rem;">
        <span style="display: inline-block; width: 60px; height: 1px; background: var(--primary-gold);"></span> THE MODERN HEALTH CRISIS <span style="display: inline-block; width: 60px; height: 1px; background: var(--primary-gold);"></span>
      </div>
      <h2 class="cinematic-title">Why Do We</h2>
      <h2 class="cinematic-title outline">Feel <span style="color: var(--primary-gold); -webkit-text-stroke: 0;">Tired</span></h2>
      <h2 class="cinematic-title">Everyday?</h2>
    </div>

    <div class="cinematic-man-container">
      <img src="assets/crisis_bg.png" alt="Tired man background">
    </div>

    <!-- Floating Glass Orbs -->
    <div class="glass-orb-wrapper" style="top: 20%; left: 15%; animation-delay: 0s;">
      <div class="glass-orb">
        <div class="glass-orb-icon"><i data-lucide="moon" style="width: 32px; height: 32px;"></i></div>
        <div class="glass-orb-content">
          <h4>Poor Sleep</h4>
          <p>Irregular sleep cycles leave you exhausted.</p>
        </div>
      </div>
    </div>

    <div class="glass-orb-wrapper" style="top: 45%; left: 8%; animation-delay: 1.5s;">
      <div class="glass-orb">
        <div class="glass-orb-icon"><i data-lucide="battery-low" style="width: 32px; height: 32px;"></i></div>
        <div class="glass-orb-content">
          <h4>Low Energy</h4>
          <p>Nutrient deficiencies lead to constant tiredness.</p>
        </div>
      </div>
    </div>

    <div class="glass-orb-wrapper" style="top: 70%; left: 15%; animation-delay: 0.8s;">
      <div class="glass-orb">
        <div class="glass-orb-icon"><i data-lucide="flask-conical" style="width: 32px; height: 32px;"></i></div>
        <div class="glass-orb-content">
          <h4>Pollution & Toxins</h4>
          <p>Environmental toxins weaken your immunity.</p>
        </div>
      </div>
    </div>

    <div class="glass-orb-wrapper" style="top: 20%; right: 15%; animation-delay: 0.5s;">
      <div class="glass-orb">
        <div class="glass-orb-icon"><i data-lucide="brain" style="width: 32px; height: 32px;"></i></div>
        <div class="glass-orb-content">
          <h4>Stress & Anxiety</h4>
          <p>Mental fatigue drains your daily energy.</p>
        </div>
      </div>
    </div>

    <div class="glass-orb-wrapper" style="top: 45%; right: 8%; animation-delay: 2s;">
      <div class="glass-orb">
        <div class="glass-orb-icon"><i data-lucide="smartphone" style="width: 32px; height: 32px;"></i></div>
        <div class="glass-orb-content">
          <h4>Excess Screen Time</h4>
          <p>Too much screen time affects your body clock.</p>
        </div>
      </div>
    </div>

    <div class="glass-orb-wrapper" style="top: 70%; right: 15%; animation-delay: 1.2s;">
      <div class="glass-orb">
        <div class="glass-orb-icon"><i data-lucide="cookie" style="width: 32px; height: 32px;"></i></div>
        <div class="glass-orb-content">
          <h4>Poor Nutrition</h4>
          <p>Unbalanced diet leaves your body incomplete.</p>
        </div>
      </div>
    </div>
  </section>"""

updated_content = pattern.sub(new_html, content)

with open('index.html', 'w') as f:
    f.write(updated_content)

print("Updated index.html successfully.")

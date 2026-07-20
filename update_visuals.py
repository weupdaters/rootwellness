import re

with open('index.html', 'r') as f:
    content = f.read()

start_marker = '      <!-- Right Side Visuals (Tired Man + Cards) -->'
end_marker = '    </div>\n  </section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_html = """      <!-- Right Side Visuals (Tired Man + Cards) -->
      <div class="crisis-visual-area" style="flex: 0 0 50%; position: relative; min-height: 600px; display: flex; align-items: center; justify-content: center; max-width: 650px;">
        
        <!-- The background image of the man -->
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; aspect-ratio: 1; border-radius: 50%; overflow: hidden; opacity: 0.95; -webkit-mask-image: radial-gradient(circle at center, black 40%, transparent 68%); mask-image: radial-gradient(circle at center, black 40%, transparent 68%); z-index: 1;">
            <img src="assets/crisis_bg.png" alt="Tired man background" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.15);">
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
"""

    updated_content = content[:start_idx] + new_html + content[end_idx:]
    with open('index.html', 'w') as f:
        f.write(updated_content)
    print("Updated index.html visuals successfully.")
else:
    print("Could not find markers.")

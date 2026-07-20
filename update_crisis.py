import re

with open('index.html', 'r') as f:
    content = f.read()

# We want to replace the inside of the <section id="crisis">...
# from <div class="container crisis-content-container"... to the end of the section.

start_marker = '<div class="container crisis-content-container" style="position: relative; z-index: 2; display: flex; align-items: center; justify-content: space-between; max-width: 1400px; width: 95%;">'
end_marker = '    </div>\n  </section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_html = """    <!-- Centered Header -->
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
      
      <!-- Left side Timeline -->
      <div class="crisis-timeline-area" style="flex: 0 0 45%; max-width: 500px;">
        <div class="crisis-timeline" style="position: relative; padding-left: 24px;">
          <!-- Vertical Line -->
          <div style="position: absolute; left: 6px; top: 16px; bottom: 16px; width: 2px; background: linear-gradient(to bottom, #9C27B0, #FF9800, #4CAF50, #FFEB3B, #2196F3, #9C27B0); opacity: 0.4;"></div>
          
          <!-- Timeline Items -->
          <div class="timeline-item" style="position: relative; margin-bottom: 1.5rem;">
            <div style="position: absolute; left: -22px; top: 12px; width: 10px; height: 10px; border-radius: 50%; background: #9C27B0; box-shadow: 0 0 10px #9C27B0; z-index: 2;"></div>
            <div style="display: flex; gap: 1rem; align-items: center; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 0.8rem; border-radius: 12px; width: 100%;">
              <div style="width: 32px; height: 32px; border-radius: 50%; border: 1px solid rgba(156, 39, 176, 0.4); display: flex; align-items: center; justify-content: center; color: #E040FB;"><i data-lucide="moon" style="width: 16px; height: 16px;"></i></div>
              <div>
                <h4 style="margin: 0; font-size: 0.9rem; color: #fff;">Poor Sleep</h4>
                <p style="margin: 0; font-size: 0.7rem; color: #a0aab2;">Irregular sleep cycles leave you exhausted.</p>
              </div>
            </div>
          </div>
          
          <div class="timeline-item" style="position: relative; margin-bottom: 1.5rem;">
            <div style="position: absolute; left: -22px; top: 12px; width: 10px; height: 10px; border-radius: 50%; background: #FF9800; box-shadow: 0 0 10px #FF9800; z-index: 2;"></div>
            <div style="display: flex; gap: 1rem; align-items: center; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 0.8rem; border-radius: 12px; width: 100%;">
              <div style="width: 32px; height: 32px; border-radius: 50%; border: 1px solid rgba(255, 152, 0, 0.4); display: flex; align-items: center; justify-content: center; color: #FFAB40;"><i data-lucide="brain" style="width: 16px; height: 16px;"></i></div>
              <div>
                <h4 style="margin: 0; font-size: 0.9rem; color: #fff;">Stress & Anxiety</h4>
                <p style="margin: 0; font-size: 0.7rem; color: #a0aab2;">Mental fatigue drains your daily energy.</p>
              </div>
            </div>
          </div>
          
          <div class="timeline-item" style="position: relative; margin-bottom: 1.5rem;">
            <div style="position: absolute; left: -22px; top: 12px; width: 10px; height: 10px; border-radius: 50%; background: #4CAF50; box-shadow: 0 0 10px #4CAF50; z-index: 2;"></div>
            <div style="display: flex; gap: 1rem; align-items: center; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 0.8rem; border-radius: 12px; width: 100%;">
              <div style="width: 32px; height: 32px; border-radius: 50%; border: 1px solid rgba(76, 175, 80, 0.4); display: flex; align-items: center; justify-content: center; color: #69F0AE;"><i data-lucide="battery-low" style="width: 16px; height: 16px;"></i></div>
              <div>
                <h4 style="margin: 0; font-size: 0.9rem; color: #fff;">Low Energy</h4>
                <p style="margin: 0; font-size: 0.7rem; color: #a0aab2;">Nutrient deficiencies lead to constant tiredness.</p>
              </div>
            </div>
          </div>
          
          <div class="timeline-item" style="position: relative; margin-bottom: 1.5rem;">
            <div style="position: absolute; left: -22px; top: 12px; width: 10px; height: 10px; border-radius: 50%; background: #FFEB3B; box-shadow: 0 0 10px #FFEB3B; z-index: 2;"></div>
            <div style="display: flex; gap: 1rem; align-items: center; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 0.8rem; border-radius: 12px; width: 100%;">
              <div style="width: 32px; height: 32px; border-radius: 50%; border: 1px solid rgba(255, 235, 59, 0.4); display: flex; align-items: center; justify-content: center; color: #FFFF00;"><i data-lucide="cookie" style="width: 16px; height: 16px;"></i></div>
              <div>
                <h4 style="margin: 0; font-size: 0.9rem; color: #fff;">Poor Nutrition</h4>
                <p style="margin: 0; font-size: 0.7rem; color: #a0aab2;">Unbalanced diet leaves your body incomplete.</p>
              </div>
            </div>
          </div>
          
          <div class="timeline-item" style="position: relative; margin-bottom: 1.5rem;">
            <div style="position: absolute; left: -22px; top: 12px; width: 10px; height: 10px; border-radius: 50%; background: #2196F3; box-shadow: 0 0 10px #2196F3; z-index: 2;"></div>
            <div style="display: flex; gap: 1rem; align-items: center; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 0.8rem; border-radius: 12px; width: 100%;">
              <div style="width: 32px; height: 32px; border-radius: 50%; border: 1px solid rgba(33, 150, 243, 0.4); display: flex; align-items: center; justify-content: center; color: #40C4FF;"><i data-lucide="smartphone" style="width: 16px; height: 16px;"></i></div>
              <div>
                <h4 style="margin: 0; font-size: 0.9rem; color: #fff;">Excess Screen Time</h4>
                <p style="margin: 0; font-size: 0.7rem; color: #a0aab2;">Too much screen time affects your body clock.</p>
              </div>
            </div>
          </div>
          
          <div class="timeline-item" style="position: relative; margin-bottom: 0;">
            <div style="position: absolute; left: -22px; top: 12px; width: 10px; height: 10px; border-radius: 50%; background: #9C27B0; box-shadow: 0 0 10px #9C27B0; z-index: 2;"></div>
            <div style="display: flex; gap: 1rem; align-items: center; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 0.8rem; border-radius: 12px; width: 100%;">
              <div style="width: 32px; height: 32px; border-radius: 50%; border: 1px solid rgba(156, 39, 176, 0.4); display: flex; align-items: center; justify-content: center; color: #E040FB;"><i data-lucide="flask-conical" style="width: 16px; height: 16px;"></i></div>
              <div>
                <h4 style="margin: 0; font-size: 0.9rem; color: #fff;">Pollution & Toxins</h4>
                <p style="margin: 0; font-size: 0.7rem; color: #a0aab2;">Environmental toxins weaken your immunity.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Right Side Visuals (Tired Man + Cards) -->
      <div class="crisis-visual-area" style="flex: 0 0 50%; position: relative; min-height: 550px; display: flex; align-items: center; justify-content: center; max-width: 650px;">
        
        <!-- The background image of the man -->
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; aspect-ratio: 1; border-radius: 50%; overflow: hidden; opacity: 0.9; -webkit-mask-image: radial-gradient(circle at center, black 45%, transparent 70%); mask-image: radial-gradient(circle at center, black 45%, transparent 70%); z-index: 1;">
            <img src="assets/crisis_bg.jpg" alt="Tired man background" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        
        <!-- Left Side Floating Cards -->
        <div class="crisis-card card-purple" style="position: absolute; top: 10%; left: -2%; width: 220px; background: rgba(10, 10, 15, 0.65); border-radius: 12px; padding: 0.8rem; display: flex; align-items: center; gap: 0.8rem; backdrop-filter: blur(12px); border: 1px solid rgba(156, 39, 176, 0.4); box-shadow: 0 0 20px rgba(156, 39, 176, 0.15); z-index: 5; animation: floatCard 4s ease-in-out infinite;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(156, 39, 176, 0.2); color: #E040FB; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="moon" style="width: 18px; height: 18px;"></i></div>
          <div>
            <h4 style="font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; margin: 0; color: #fff;">Poor Sleep</h4>
            <p style="font-family: var(--font-body); font-size: 0.7rem; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.3;">Irregular sleep cycles leave you exhausted.</p>
          </div>
        </div>

        <div class="crisis-card card-green" style="position: absolute; top: 45%; left: -8%; width: 220px; background: rgba(10, 10, 15, 0.65); border-radius: 12px; padding: 0.8rem; display: flex; align-items: center; gap: 0.8rem; backdrop-filter: blur(12px); border: 1px solid rgba(76, 175, 80, 0.4); box-shadow: 0 0 20px rgba(76, 175, 80, 0.15); z-index: 5; animation: floatCard 4s ease-in-out 1s infinite;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(76, 175, 80, 0.2); color: #69F0AE; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="battery-low" style="width: 18px; height: 18px;"></i></div>
          <div>
            <h4 style="font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; margin: 0; color: #fff;">Low Energy</h4>
            <p style="font-family: var(--font-body); font-size: 0.7rem; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.3;">Nutrient deficiencies lead to constant tiredness.</p>
          </div>
        </div>

        <div class="crisis-card card-blue" style="position: absolute; top: 80%; left: -2%; width: 220px; background: rgba(10, 10, 15, 0.65); border-radius: 12px; padding: 0.8rem; display: flex; align-items: center; gap: 0.8rem; backdrop-filter: blur(12px); border: 1px solid rgba(33, 150, 243, 0.4); box-shadow: 0 0 20px rgba(33, 150, 243, 0.15); z-index: 5; animation: floatCard 4s ease-in-out 2s infinite;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(33, 150, 243, 0.2); color: #40C4FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="smartphone" style="width: 18px; height: 18px;"></i></div>
          <div>
            <h4 style="font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; margin: 0; color: #fff;">Excess Screen Time</h4>
            <p style="font-family: var(--font-body); font-size: 0.7rem; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.3;">Too much screen time affects your body clock.</p>
          </div>
        </div>
        
        <!-- Right Side Floating Cards -->
        <div class="crisis-card card-orange" style="position: absolute; top: 10%; right: -2%; width: 220px; background: rgba(10, 10, 15, 0.65); border-radius: 12px; padding: 0.8rem; display: flex; align-items: center; gap: 0.8rem; backdrop-filter: blur(12px); border: 1px solid rgba(255, 152, 0, 0.4); box-shadow: 0 0 20px rgba(255, 152, 0, 0.15); z-index: 5; animation: floatCard 4s ease-in-out 0.5s infinite;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(255, 152, 0, 0.2); color: #FFAB40; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="brain" style="width: 18px; height: 18px;"></i></div>
          <div>
            <h4 style="font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; margin: 0; color: #fff;">Stress & Anxiety</h4>
            <p style="font-family: var(--font-body); font-size: 0.7rem; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.3;">Mental fatigue drains your daily energy.</p>
          </div>
        </div>

        <div class="crisis-card card-yellow" style="position: absolute; top: 45%; right: -8%; width: 220px; background: rgba(10, 10, 15, 0.65); border-radius: 12px; padding: 0.8rem; display: flex; align-items: center; gap: 0.8rem; backdrop-filter: blur(12px); border: 1px solid rgba(255, 235, 59, 0.4); box-shadow: 0 0 20px rgba(255, 235, 59, 0.15); z-index: 5; animation: floatCard 4s ease-in-out 1.5s infinite;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(255, 235, 59, 0.2); color: #FFFF00; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="cookie" style="width: 18px; height: 18px;"></i></div>
          <div>
            <h4 style="font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; margin: 0; color: #fff;">Poor Nutrition</h4>
            <p style="font-family: var(--font-body); font-size: 0.7rem; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.3;">Unbalanced diet leaves your body incomplete.</p>
          </div>
        </div>

        <div class="crisis-card card-purple" style="position: absolute; top: 80%; right: -2%; width: 220px; background: rgba(10, 10, 15, 0.65); border-radius: 12px; padding: 0.8rem; display: flex; align-items: center; gap: 0.8rem; backdrop-filter: blur(12px); border: 1px solid rgba(156, 39, 176, 0.4); box-shadow: 0 0 20px rgba(156, 39, 176, 0.15); z-index: 5; animation: floatCard 4s ease-in-out 2.5s infinite;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(156, 39, 176, 0.2); color: #E040FB; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><i data-lucide="flask-conical" style="width: 18px; height: 18px;"></i></div>
          <div>
            <h4 style="font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; margin: 0; color: #fff;">Pollution & Toxins</h4>
            <p style="font-family: var(--font-body); font-size: 0.7rem; color: rgba(255,255,255,0.7); margin: 0; line-height: 1.3;">Environmental toxins weaken your immunity.</p>
          </div>
        </div>
        
      </div>
"""

    updated_content = content[:start_idx] + new_html + content[end_idx:]
    with open('index.html', 'w') as f:
        f.write(updated_content)
    print("Updated index.html successfully.")
else:
    print("Could not find markers.")

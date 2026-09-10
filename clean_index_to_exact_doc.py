# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove old unused sections from index.html:
# 1. Old #how
html = re.sub(r'<section class="sec" id="how">.*?</section>', '', html, flags=re.DOTALL)
# 2. Old #kitchen-craft (now on develop-brand.html)
html = re.sub(r'<section class="sec on-dark" id="kitchen-craft">.*?</section>', '', html, flags=re.DOTALL)
# 3. Old #city-sec (now on find-franchise.html)
html = re.sub(r'<section class="sec tight" id="city-sec">.*?</section>', '', html, flags=re.DOTALL)
# 4. Old #quiz (now on find-franchise.html)
html = re.sub(r'<section class="wrap sec tight" id="quiz">.*?</section>', '', html, flags=re.DOTALL)
# 5. Old voices/franchisees
html = re.sub(r'<section class="sec tight">\s*<div class="wrap">\s*<div class="sec-head">\s*<p class="eyebrow">Franchisees</p>.*?</section>', '', html, flags=re.DOTALL)
# 6. Old brackets/budget
html = re.sub(r'<section class="brackets" id="budget">.*?</section>', '', html, flags=re.DOTALL)
# 7. Old metrics
html = re.sub(r'<section class="sec">\s*<div class="wrap">\s*<div class="sec-head">\s*<p class="eyebrow">Since 2019</p>.*?</section>', '', html, flags=re.DOTALL)
# 8. Old brand-services
html = re.sub(r'<section class="sec on-dark" id="brand-services">.*?</section>', '', html, flags=re.DOTALL)
# 9. Old about
html = re.sub(r'<section class="sec" id="about">.*?</section>', '', html, flags=re.DOTALL)
# 10. Old apply
html = re.sub(r'<section class="sec tight" id="apply">.*?</section>', '', html, flags=re.DOTALL)
# 11. Old duplicate faqs
html = re.sub(r'<section class="sec tight" id="faq">\s*<div class="wrap">\s*<div class="sec-head">\s*<p class="eyebrow">Before you apply</p>.*?</section>', '', html, flags=re.DOTALL)

# Ensure the find-match-teaser is placed right after how-it-works
FIND_MATCH_TEASER = """<!-- ============ FIND YOUR RIGHT FRANCHISE (MATCH TEASER) ============ -->
<section class="sec" id="find-match-teaser" style="background:var(--paper);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:clamp(24px, 4vw, 36px);padding:clamp(32px, 5vw, 56px);display:grid;grid-template-columns:1.2fr 1fr;gap:36px;align-items:center;box-shadow:0 16px 45px -15px rgba(14,18,26,0.08)" class="rv">
      <div>
        <span class="tag gold" style="margin-bottom:12px">Intelligent Matcher</span>
        <h2 style="font-size:clamp(26px, 3.4vw, 42px);color:var(--ink);margin:0 0 14px;line-height:1.2">
          Let's Find What Fits You.
        </h2>
        <p style="font-size:16px;color:var(--ink-80);line-height:1.65;margin:0 0 24px">
          Every investor is different. Tell us a little about your goals, preferences and investment capacity, and our team will use this information to understand what opportunities may be worth exploring with you.
        </p>
        <div style="display:flex;gap:12px;flex-wrap:wrap">
          <a class="btn btn--kesar" href="find-franchise.html">Take Matching Questionnaire &rarr;</a>
          <a class="btn btn--ghost" href="contact.html">Speak With a Consultant</a>
        </div>
      </div>
      <div style="background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:24px;display:flex;flex-direction:column;gap:12px">
        <span style="font-family:var(--font-mono);font-size:12px;color:var(--kesar-hot);font-weight:700;text-transform:uppercase">Interactive 5-Point Profile Check</span>
        <div style="display:flex;gap:10px;align-items:center;font-size:14.5px;color:var(--ink)">
          <span style="color:var(--pista-dark);font-weight:800">&check;</span> <span>Investment Budget Calibration (₹8L to ₹50L+)</span>
        </div>
        <div style="display:flex;gap:10px;align-items:center;font-size:14.5px;color:var(--ink)">
          <span style="color:var(--pista-dark);font-weight:800">&check;</span> <span>City &amp; Commercial High-Street Territory</span>
        </div>
        <div style="display:flex;gap:10px;align-items:center;font-size:14.5px;color:var(--ink)">
          <span style="color:var(--pista-dark);font-weight:800">&check;</span> <span>Food Category (Cafe, Desserts, QSR, Subs)</span>
        </div>
        <div style="display:flex;gap:10px;align-items:center;font-size:14.5px;color:var(--ink)">
          <span style="color:var(--pista-dark);font-weight:800">&check;</span> <span>Operational Model (Hands-on FOFO vs Passive FOCO)</span>
        </div>
      </div>
    </div>
  </div>
</section>"""

if 'id="find-match-teaser"' not in html:
    html = html.replace('<!-- ============ OFFICIAL FAQ ============ -->', f"{FIND_MATCH_TEASER}\n\n<!-- ============ OFFICIAL FAQ ============ -->")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html and franq-franchise-website.html cleaned and formatted perfectly!")

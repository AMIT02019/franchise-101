# -*- coding: utf-8 -*-
import os, re
from bs4 import BeautifulSoup

print("Starting homepage streamlining and section relocation...")

# 1. READ index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# 2. Extract sections to relocate
# Extract #budget
budget_match = re.search(r'(<!-- ============ BUDGET RAIL.*?<!-- ============ METRICS)', index_html, re.DOTALL)
budget_section_html = budget_match.group(1).replace('<!-- ============ METRICS', '').strip() if budget_match else ""

# Extract #kitchen-craft
kitchen_match = re.search(r'(<!-- ============ BEHIND THE COUNTER.*?<!-- ============ BRAND MATRIX)', index_html, re.DOTALL)
kitchen_section_html = kitchen_match.group(1).replace('<!-- ============ BRAND MATRIX', '').strip() if kitchen_match else ""

# Extract #calculator
calc_match = re.search(r'(<!-- ============ INTERACTIVE FORMAT & BRAND ROI CALCULATOR.*?<!-- ============ WHY FRANCHISE 101)', index_html, re.DOTALL)
calc_section_html = calc_match.group(1).replace('<!-- ============ WHY FRANCHISE 101', '').strip() if calc_match else ""

# Extract #city-sec
city_match = re.search(r'(<!-- ============ CITY AVAILABILITY CHECKER.*?<!-- ============ FIND THE RIGHT FRANCHISE)', index_html, re.DOTALL)
city_section_html = city_match.group(1).replace('<!-- ============ FIND THE RIGHT FRANCHISE', '').strip() if city_match else ""


# ------------------------------------------------------------------------------
# RELOCATE TO franchises.html
# ------------------------------------------------------------------------------
with open("franchises.html", "r", encoding="utf-8") as f:
    f_html = f.read()

# Add Budget Brackets and Calculator to franchises.html if not present
if "<!-- ============ BUDGET RAIL" not in f_html and budget_section_html:
    f_html = f_html.replace('<!-- ============ FOOTER ============ -->', f"{budget_section_html}\n\n<!-- ============ FOOTER ============ -->")

if "<!-- ============ INTERACTIVE FORMAT & BRAND ROI CALCULATOR" not in f_html and calc_section_html:
    f_html = f_html.replace('<!-- ============ FOOTER ============ -->', f"{calc_section_html}\n\n<!-- ============ FOOTER ============ -->")

with open("franchises.html", "w", encoding="utf-8") as f:
    f.write(f_html)
print("Relocated Budget Brackets & ROI Calculator to franchises.html")


# ------------------------------------------------------------------------------
# RELOCATE TO develop-brand.html
# ------------------------------------------------------------------------------
with open("develop-brand.html", "r", encoding="utf-8") as f:
    db_html = f.read()

if "<!-- ============ BEHIND THE COUNTER" not in db_html and kitchen_section_html:
    db_html = db_html.replace('<!-- ============ FOOTER ============ -->', f"{kitchen_section_html}\n\n<!-- ============ FOOTER ============ -->")

with open("develop-brand.html", "w", encoding="utf-8") as f:
    f.write(db_html)
print("Relocated Behind The Counter SOP Showcase to develop-brand.html")


# ------------------------------------------------------------------------------
# RELOCATE TO find-franchise.html
# ------------------------------------------------------------------------------
with open("find-franchise.html", "r", encoding="utf-8") as f:
    ff_html = f.read()

if "<!-- ============ CITY AVAILABILITY CHECKER" not in ff_html and city_section_html:
    ff_html = ff_html.replace('<!-- ============ FOOTER ============ -->', f"{city_section_html}\n\n<!-- ============ FOOTER ============ -->")

with open("find-franchise.html", "w", encoding="utf-8") as f:
    f.write(ff_html)
print("Relocated City Availability Checker to find-franchise.html")


# ------------------------------------------------------------------------------
# STREAMLINE index.html (Keep only the clean, high-impact sections from Doc Section 1)
# ------------------------------------------------------------------------------

# 1. Remove #how (Enquiry to first order in 9 weeks) since #how-it-works replaces it
index_html = re.sub(r'<!-- ============ HOW IT WORKS \(9 WEEKS\) ============ -->.*?(?=<!-- ============ BEHIND THE COUNTER|<!-- ============ FRANCHISE 101 ECOSYSTEM)', '', index_html, flags=re.DOTALL)
index_html = re.sub(r'<section class="sec" id="how">.*?</section>', '', index_html, flags=re.DOTALL)

# 2. Remove #kitchen-craft from homepage (now in develop-brand.html & franchises.html)
index_html = re.sub(r'<!-- ============ BEHIND THE COUNTER.*?<!-- ============ FRANCHISE 101 ECOSYSTEM', '<!-- ============ FRANCHISE 101 ECOSYSTEM', index_html, flags=re.DOTALL)

# 3. Remove #calculator from homepage (now in franchises.html)
index_html = re.sub(r'<!-- ============ INTERACTIVE FORMAT & BRAND ROI CALCULATOR.*?<!-- ============ WHY FRANCHISE 101', '<!-- ============ WHY FRANCHISE 101', index_html, flags=re.DOTALL)

# 4. Remove #city-sec from homepage (now in find-franchise.html)
index_html = re.sub(r'<!-- ============ CITY AVAILABILITY CHECKER.*?<!-- ============ HOW IT WORKS', '<!-- ============ HOW IT WORKS', index_html, flags=re.DOTALL)

# 5. Remove #quiz from homepage (replace with a compact "Find Your Right Franchise" teaser banner)
FIND_MATCH_TEASER_HTML = """<!-- ============ FIND YOUR RIGHT FRANCHISE (MATCH TEASER) ============ -->
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

index_html = re.sub(r'<!-- ============ FIND THE RIGHT FRANCHISE \(INTERACTIVE QUIZ\).*?</section>', FIND_MATCH_TEASER_HTML, index_html, flags=re.DOTALL)

# 6. Remove #budget (What ₹6L buys and what ₹60L does) from homepage
index_html = re.sub(r'<!-- ============ BUDGET RAIL.*?<!-- ============ METRICS', '<!-- ============ METRICS', index_html, flags=re.DOTALL)
index_html = re.sub(r'<section class="brackets" id="budget">.*?</section>', '', index_html, flags=re.DOTALL)

# 7. Remove #brand-services, #about, and #apply from homepage
index_html = re.sub(r'<!-- ============ BRAND SERVICES OVERVIEW.*?<!-- ============ ABOUT SECTION', '<!-- ============ ABOUT SECTION', index_html, flags=re.DOTALL)
index_html = re.sub(r'<section class="sec on-dark" id="brand-services">.*?</section>', '', index_html, flags=re.DOTALL)

index_html = re.sub(r'<!-- ============ ABOUT SECTION.*?<!-- ============ FAQ', '<!-- ============ FAQ', index_html, flags=re.DOTALL)
index_html = re.sub(r'<section class="sec" id="about">.*?</section>', '', index_html, flags=re.DOTALL)

index_html = re.sub(r'<!-- ============ DIRECT APPLICATION FORM.*?</section>', '', index_html, flags=re.DOTALL)
index_html = re.sub(r'<section class="sec tight" id="apply">.*?</section>', '', index_html, flags=re.DOTALL)

# Remove redundant metrics / since-2019 and voices
index_html = re.sub(r'<!-- ============ METRICS ============ -->.*?<!-- ============ VOICES ============ -->', '', index_html, flags=re.DOTALL)
index_html = re.sub(r'<!-- ============ VOICES ============ -->.*?(?=<!-- ============ OFFICIAL FAQ|<!-- ============ FINAL CTA)', '', index_html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("Streamlined index.html and franq-franchise-website.html successfully!")

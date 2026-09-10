# -*- coding: utf-8 -*-
import os, re

print("=== FIXING HEADER ALIGNMENT AND EXPLORE FRANCHISES PAGE ===")

# ==============================================================================
# 1. UPDATE styles.css WITH BULLETPROOF NAV & COMPLETE CALCULATOR + BRACKETS CSS
# ==============================================================================
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

NAV_AND_PAGE_CSS = """
/* ==========================================================================
   PERFECT SINGLE-LINE NAV & COMPREHENSIVE SECTION ALIGNMENT FIXES
   ========================================================================== */

.nav {
  position: fixed !important;
  top: 14px !important;
  left: 50% !important;
  transform: translate(-50%, 0) !important;
  width: min(1320px, calc(100% - 28px)) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 8px 14px 8px 22px !important;
  background: rgba(14, 18, 26, 0.94) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  border: 1px solid rgba(255, 255, 255, 0.16) !important;
  border-radius: 999px !important;
  box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.65), 0 0 0 1px rgba(255, 176, 32, 0.15) !important;
  z-index: 9999 !important;
  white-space: nowrap !important;
  height: 58px !important;
  box-sizing: border-box !important;
}

.logo {
  font-family: var(--font-editorial, Georgia, serif) !important;
  font-weight: 800 !important;
  font-size: 19px !important;
  letter-spacing: -0.02em !important;
  color: #FFFFFF !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
  line-height: 1 !important;
}

.logo .dot {
  width: 8px !important;
  height: 8px !important;
  border-radius: 50% !important;
  background: var(--kesar, #FFB020) !important;
  display: inline-block !important;
  box-shadow: 0 0 8px var(--kesar, #FFB020) !important;
  flex-shrink: 0 !important;
}

.nav-links {
  display: flex !important;
  align-items: center !important;
  gap: clamp(10px, 1.3vw, 20px) !important;
  white-space: nowrap !important;
  flex-shrink: 1 !important;
  margin: 0 !important;
  padding: 0 !important;
}

.nav-links a {
  font-family: var(--font-body, 'Plus Jakarta Sans', sans-serif) !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  color: rgba(248, 250, 252, 0.82) !important;
  white-space: nowrap !important;
  padding: 6px 2px !important;
  transition: color 0.2s ease !important;
  text-decoration: none !important;
  display: inline-block !important;
  line-height: 1.2 !important;
}

.nav-links a:hover, .nav-links a.active {
  color: #FFFFFF !important;
}

.nav-links a.active {
  color: var(--kesar, #FFB020) !important;
  position: relative !important;
}

.nav-cta-wrap {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  flex-shrink: 0 !important;
}

.nav .btn--kesar {
  white-space: nowrap !important;
  padding: 10px 20px !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  border-radius: 999px !important;
  line-height: 1 !important;
}

@media (max-width: 1140px) {
  .nav-links {
    display: none !important;
  }
  .nav-toggle {
    display: flex !important;
  }
}

/* ============ INTERACTIVE ROI CALCULATOR STYLES ============ */
.calc-section {
  background: var(--jamun-soft, #181F2C) !important;
  color: #FFFFFF !important;
  border-radius: clamp(24px, 4vw, 36px) !important;
  padding: clamp(32px, 5vw, 56px) clamp(20px, 4vw, 48px) !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.5) !important;
}

.calc-grid {
  display: grid !important;
  grid-template-columns: 1.2fr 1fr !important;
  gap: clamp(28px, 4vw, 48px) !important;
  align-items: start !important;
}

@media (max-width: 960px) {
  .calc-grid {
    grid-template-columns: 1fr !important;
  }
}

.calc-card {
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  border-radius: 20px !important;
  padding: 24px 26px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 20px !important;
}

.calc-group {
  display: flex !important;
  flex-direction: column !important;
  gap: 8px !important;
}

.calc-label-row {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  font-family: var(--font-mono, monospace) !important;
  font-size: 13px !important;
  color: #FFFFFF !important;
  font-weight: 600 !important;
}

.calc-val-badge {
  color: var(--kesar, #FFB020) !important;
  font-weight: 700 !important;
  font-size: 15px !important;
}

.calc-slider {
  -webkit-appearance: none !important;
  width: 100% !important;
  height: 6px !important;
  border-radius: 6px !important;
  background: rgba(255, 255, 255, 0.25) !important;
  outline: none !important;
  cursor: pointer !important;
}

.calc-slider::-webkit-slider-thumb {
  -webkit-appearance: none !important;
  width: 20px !important;
  height: 20px !important;
  border-radius: 50% !important;
  background: var(--kesar, #FFB020) !important;
  box-shadow: 0 0 10px rgba(255, 176, 32, 0.7) !important;
  cursor: pointer !important;
}

.calc-formats {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 8px !important;
}

@media (max-width: 600px) {
  .calc-formats {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

.calc-brand-pills {
  display: flex !important;
  gap: 6px !important;
  flex-wrap: wrap !important;
  margin-top: 4px !important;
}

.fmt-btn {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1px solid rgba(255, 255, 255, 0.16) !important;
  color: rgba(255, 255, 255, 0.85) !important;
  padding: 10px 8px !important;
  border-radius: 10px !important;
  font-family: var(--font-mono, monospace) !important;
  font-size: 11.5px !important;
  cursor: pointer !important;
  text-align: center !important;
  transition: all 0.2s !important;
}

.fmt-btn.active {
  background: var(--kesar, #FFB020) !important;
  color: var(--jamun-deep, #080B10) !important;
  border-color: var(--kesar, #FFB020) !important;
  font-weight: 700 !important;
  box-shadow: 0 0 12px rgba(255, 176, 32, 0.35) !important;
}

.brand-pill-btn {
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.14) !important;
  color: rgba(255, 255, 255, 0.8) !important;
  padding: 6px 12px !important;
  border-radius: 999px !important;
  font-family: var(--font-mono, monospace) !important;
  font-size: 11px !important;
  cursor: pointer !important;
  text-align: center !important;
  transition: all 0.2s !important;
}

.brand-pill-btn:hover {
  border-color: var(--kesar, #FFB020) !important;
  color: #FFFFFF !important;
}

.brand-pill-btn.active {
  background: var(--kesar, #FFB020) !important;
  color: var(--jamun-deep, #080B10) !important;
  border-color: var(--kesar, #FFB020) !important;
  font-weight: 700 !important;
}

.calc-results-board {
  background: var(--jamun-deep, #080B10) !important;
  border: 1px solid rgba(255, 176, 32, 0.35) !important;
  border-radius: 20px !important;
  padding: 26px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 18px !important;
  box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6) !important;
}

.calc-metric-row {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 14px !important;
}

.calc-metric-item {
  background: rgba(255, 255, 255, 0.05) !important;
  border-radius: 12px !important;
  padding: 14px !important;
}

.calc-metric-item small {
  display: block !important;
  font-family: var(--font-mono, monospace) !important;
  font-size: 11px !important;
  color: rgba(255, 255, 255, 0.7) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.1em !important;
}

.calc-metric-item strong {
  display: block !important;
  font-family: var(--font-editorial, Georgia, serif) !important;
  font-size: 24px !important;
  font-weight: 800 !important;
  color: var(--kesar, #FFB020) !important;
  margin-top: 4px !important;
}

.calc-highlight-box {
  background: rgba(16, 185, 129, 0.12) !important;
  border: 1px solid rgba(16, 185, 129, 0.35) !important;
  border-radius: 14px !important;
  padding: 16px 18px !important;
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
}

.calc-highlight-box small {
  display: block !important;
  font-family: var(--font-mono, monospace) !important;
  font-size: 11px !important;
  color: rgba(255, 255, 255, 0.85) !important;
  text-transform: uppercase !important;
}

.calc-highlight-box b {
  font-family: var(--font-editorial, Georgia, serif) !important;
  font-size: 28px !important;
  color: var(--pista, #00E599) !important;
}

/* ============ BUDGET BRACKETS STYLES ============ */
.brackets {
  background: var(--jamun-deep, #080B10) !important;
  color: #FFFFFF !important;
  border-radius: clamp(24px, 4vw, 44px) !important;
  margin-block: clamp(32px, 5vw, 64px) !important;
}
.rail-outer {
  padding: clamp(48px, 6vw, 80px) 0 !important;
}
.rail {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)) !important;
  gap: 20px !important;
  margin-top: 32px !important;
}
.slab {
  border-radius: 20px !important;
  padding: 24px !important;
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 14px !important;
}
.slab .shot {
  aspect-ratio: 16/9 !important;
  border-radius: 12px !important;
  overflow: hidden !important;
}
.slab-amt {
  font-family: var(--font-editorial, Georgia, serif) !important;
  font-weight: 800 !important;
  font-size: 28px !important;
  color: var(--kesar, #FFB020) !important;
}
.slab p {
  color: rgba(255, 255, 255, 0.75) !important;
  font-size: 14px !important;
  line-height: 1.55 !important;
}
.slab ul {
  list-style: none !important;
  margin: auto 0 0 !important;
  padding: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 8px !important;
}
.slab li {
  font-size: 13.5px !important;
  color: rgba(255, 255, 255, 0.85) !important;
  display: flex !important;
  gap: 8px !important;
  align-items: flex-start !important;
}
.slab li::before {
  content: "•" !important;
  color: var(--kesar, #FFB020) !important;
  font-weight: bold !important;
}
"""

if "/* ==========================================================================\n   PERFECT SINGLE-LINE NAV" in css:
    css = re.sub(r'/\* ==========================================================================\s*PERFECT SINGLE-LINE NAV.*', NAV_AND_PAGE_CSS, css, flags=re.DOTALL)
else:
    css += "\n" + NAV_AND_PAGE_CSS

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated styles.css with single-line nav and calculator/budget CSS!")


# ==============================================================================
# 2. UPDATE NAVBAR ACROSS ALL 15 HTML FILES WITH CLEAN, NON-DUPLICATE LINKS
# ==============================================================================
ALL_PAGES = [
    "index.html", "franq-franchise-website.html", "franchises.html", 
    "develop-brand.html", "develop-scale.html", "franchise-marketing.html", 
    "about.html", "contact.html", "find-franchise.html", "book-consultation.html",
    "beyond-temptation.html", "dunk-burgers.html", "mr-sandwich.html", 
    "south-twist.html", "cafe-choco-craze.html"
]

def make_clean_nav(active_page):
    return f"""  <a class="logo" href="index.html" aria-label="Franchise 101 Home">FRANCHISE 101<span class="dot"></span></a>
  <div class="nav-links">
    <a href="index.html"{' class="active"' if active_page == 'index' else ''}>Home</a>
    <a href="franchises.html"{' class="active"' if active_page == 'franchises' else ''}>Explore Franchises</a>
    <a href="develop-brand.html"{' class="active"' if active_page == 'develop-brand' else ''}>Build Your Brand</a>
    <a href="develop-scale.html"{' class="active"' if active_page == 'develop-scale' else ''}>Franchise &amp; Scale</a>
    <a href="franchise-marketing.html"{' class="active"' if active_page == 'franchise-marketing' else ''}>Franchise Marketing</a>
    <a href="about.html"{' class="active"' if active_page == 'about' else ''}>About Us</a>
    <a href="contact.html"{' class="active"' if active_page in ['contact', 'book-consultation'] else ''}>Contact</a>
  </div>
  <div class="nav-cta-wrap">
    <a class="btn btn--kesar" href="contact.html">Book a Consultation <span class="arw">&rarr;</span></a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>"""

def make_clean_mobile(active_page):
    return f"""    <div class="logo">FRANCHISE 101<span class="dot"></span></div>
    <nav>
      <a href="index.html" class="mobile-nav-link{' active' if active_page == 'index' else ''}>Home</a>
      <a href="franchises.html" class="mobile-nav-link{' active' if active_page == 'franchises' else ''}>Explore Franchises</a>
      <a href="develop-brand.html" class="mobile-nav-link{' active' if active_page == 'develop-brand' else ''}>Build Your Brand</a>
      <a href="develop-scale.html" class="mobile-nav-link{' active' if active_page == 'develop-scale' else ''}>Franchise &amp; Scale</a>
      <a href="franchise-marketing.html" class="mobile-nav-link{' active' if active_page == 'franchise-marketing' else ''}>Franchise Marketing</a>
      <a href="about.html" class="mobile-nav-link{' active' if active_page == 'about' else ''}>About Us</a>
      <a href="contact.html" class="mobile-nav-link{' active' if active_page in ['contact', 'book-consultation'] else ''}>Contact &middot; Book Consultation</a>
    </nav>
    <div style="margin-top:auto;display:flex;flex-direction:column;gap:12px">
      <a class="btn btn--kesar" href="contact.html" style="width:100%;text-align:center">Book a Consultation &rarr;</a>
      <p style="font-family:var(--font-mono, monospace);font-size:12px;color:rgba(248,250,252,.6);text-align:center">Zero fee &middot; Direct brand connect</p>
    </div>"""

for p in ALL_PAGES:
    if not os.path.exists(p):
        continue
    page_key = p.replace(".html", "")
    if "index" in page_key or "franq" in page_key:
        page_key = "index"
    
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Clean rogue closing divs right before page-hero
    html = re.sub(r'</div>\s*</div>\s*</div>\s*(<!-- ============ PAGE HERO)', r'</div>\n</div>\n\n\1', html)
    
    # Replace nav
    html = re.sub(r'<nav class="nav" id="nav">.*?</nav>', f'<nav class="nav" id="nav">\n{make_clean_nav(page_key)}\n</nav>', html, flags=re.DOTALL)
    
    # Replace mobile drawer content
    html = re.sub(r'<div class="mobile-drawer-content">.*?</div>\s*</div>', f'<div class="mobile-drawer-content">\n{make_clean_mobile(page_key)}\n  </div>\n</div>', html, flags=re.DOTALL)
    
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)

print("Standardized clean single-line nav across all pages!")


# ==============================================================================
# 3. FIX franchises.html SPECIFICALLY (ALIGN ALL SECTIONS + ADD JS LOGIC)
# ==============================================================================
with open("franchises.html", "r", encoding="utf-8") as f:
    f_html = f.read()

# Fix rogue closing div before page hero
f_html = f_html.replace('</div>\n</div>\n</div>\n\n<!-- ============ PAGE HERO ============ -->', '</div>\n</div>\n\n<!-- ============ PAGE HERO ============ -->')

# Clean #budget section to be standard wrapped section
BUDGET_CLEAN = """<!-- ============ BUDGET RAIL ============ -->
<section class="sec" id="budget" style="background:var(--jamun-deep);color:#FFFFFF;border-top:1px solid var(--line-dark);border-bottom:1px solid var(--line-dark)">
  <div class="wrap">
    <div class="sec-top rv" style="margin-bottom:32px">
      <div class="sec-head wide">
        <p class="eyebrow on-dark">By Budget Bracket</p>
        <h2 style="color:#FFFFFF;font-size:clamp(26px, 3.4vw, 42px)">What &#8377;6 Lakh Buys, and What &#8377;60 Lakh Does.</h2>
      </div>
      <p class="sec-note on-dark">Pick the bracket you can fund without borrowing against the house. The format follows the capital, not the other way round.</p>
    </div>
    
    <div class="rail rv">
      <article class="slab">
        <div class="shot"><img loading="lazy" src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=700&h=350&fit=crop" alt="Coffee cups on a counter" /></div>
        <span class="slab-amt">&#8377;6&ndash;15L</span>
        <p><strong>Kiosk &amp; Takeaway Formats.</strong> Low capex, high density, quick to launch.</p>
        <ul>
          <li>Chai, momo, waffle and bakery counters</li>
          <li>90&ndash;200 sqft, shutter or mall kiosk</li>
          <li>Break-even typically 11&ndash;15 months</li>
          <li>Can run hands-on or with compact 2-person crew</li>
        </ul>
      </article>

      <article class="slab">
        <div class="shot"><img loading="lazy" src="https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=700&h=350&fit=crop" alt="Burger on a counter" /></div>
        <span class="slab-amt">&#8377;15&ndash;30L</span>
        <p><strong>Full QSR Outlets.</strong> Dine-in counter with a dedicated commercial kitchen line.</p>
        <ul>
          <li>Ice cream parlours, burger and biryani QSR</li>
          <li>300&ndash;600 sqft on a high-street location</li>
          <li>Break-even typically 16&ndash;22 months</li>
          <li>Needs a shift manager and 4&ndash;6 staff</li>
        </ul>
      </article>

      <article class="slab">
        <div class="shot"><img loading="lazy" src="https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=700&h=350&fit=crop" alt="Cafe interior with plants" /></div>
        <span class="slab-amt">&#8377;30&ndash;60L</span>
        <p><strong>Caf&eacute;s &amp; Casual Dining.</strong> Higher ticket size, premium seating, higher repeat footfall.</p>
        <ul>
          <li>Caf&eacute; lounges and 40&ndash;80 cover restaurants</li>
          <li>1,000&ndash;2,000 sqft with roadside visibility</li>
          <li>Break-even typically 20&ndash;28 months</li>
          <li>Six months of working capital is recommended</li>
        </ul>
      </article>

      <article class="slab">
        <div class="shot"><img loading="lazy" src="https://images.unsplash.com/photo-1552566626-52f8b828add9?w=700&h=350&fit=crop" alt="Large dining hall" /></div>
        <span class="slab-amt">&#8377;60L+</span>
        <p><strong>Master Territory Rights.</strong> Exclusive rights for a city, district or state.</p>
        <ul>
          <li>Territory exclusivity with sub-franchise royalty sharing</li>
          <li>Three to five units committed over 24 months</li>
          <li>Direct founder introductions and area exclusivity</li>
          <li>Centralized regional supply coordination</li>
        </ul>
      </article>
    </div>
  </div>
</section>"""

f_html = re.sub(r'<!-- ============ BUDGET RAIL ============ -->.*?(?=<!-- ============ INTERACTIVE FORMAT)', BUDGET_CLEAN + "\n\n", f_html, flags=re.DOTALL)

# Add Calculator Interactive JavaScript into franchises.html if not present
CALC_SCRIPT = """
<script>
// Format & Brand Simulator Data
const FORMAT_PRESETS = {
  kiosk: { capex: 800000, margin: 42, dailyOrders: 85, aov: 160, rent: 25000, staff: 2, staffCost: 28000, royaltyRate: 0 },
  qsr: { capex: 1600000, margin: 38, dailyOrders: 140, aov: 240, rent: 55000, staff: 5, staffCost: 75000, royaltyRate: 0 },
  cloud: { capex: 1000000, margin: 40, dailyOrders: 110, aov: 280, rent: 30000, staff: 3, staffCost: 45000, royaltyRate: 0 },
  dine: { capex: 5000000, margin: 36, dailyOrders: 220, aov: 480, rent: 140000, staff: 12, staffCost: 220000, royaltyRate: 0 }
};

const BRAND_PRESETS = {
  'general': { foodCost: 32, royalty: 0, label: 'General F&B' },
  'beyond-temptation': { foodCost: 32, royalty: 0, label: 'Beyond Temptation (32% Food Cost)' },
  'dunk-burgers': { foodCost: 30, royalty: 0, label: 'Dunk Burgers (30% Food Cost · 0% Royalty)' },
  'mr-sandwich': { foodCost: 29, royalty: 0, label: 'Mr. Sandwich (29% Food Cost · 41% Margin)' },
  'south-twist': { foodCost: 26, royalty: 0, label: 'South Twist (26% Food Cost · Automated)' },
  'cafe-choco-craze': { foodCost: 31, royalty: 0, label: 'Cafe Choco Craze (31% Food Cost)' }
};

let currentFmt = 'kiosk';
let currentBrand = 'general';

function setCalcFormat(fmt) {
  currentFmt = fmt;
  document.querySelectorAll('.fmt-btn').forEach(b => b.classList.toggle('active', b.getAttribute('data-fmt') === fmt));
  const p = FORMAT_PRESETS[fmt];
  document.getElementById('calcCapex').value = p.capex;
  document.getElementById('calcOrders').value = p.dailyOrders;
  document.getElementById('calcAov').value = p.aov;
  document.getElementById('calcMargin').value = p.margin;
  updateCalc();
}

function setCalcBrand(brandKey) {
  currentBrand = brandKey;
  document.querySelectorAll('.brand-pill-btn').forEach(b => b.classList.toggle('active', b.getAttribute('data-brand') === brandKey));
  const bData = BRAND_PRESETS[brandKey];
  document.getElementById('calcBrandBadge').textContent = bData.label;
  const impliedMargin = 100 - bData.foodCost - 28;
  document.getElementById('calcMargin').value = Math.max(28, Math.min(46, impliedMargin));
  updateCalc();
}

function updateCalc() {
  const capex = parseInt(document.getElementById('calcCapex').value);
  const orders = parseInt(document.getElementById('calcOrders').value);
  const aov = parseInt(document.getElementById('calcAov').value);
  const marginPct = parseInt(document.getElementById('calcMargin').value);

  document.getElementById('calcCapexVal').textContent = '₹' + (capex >= 10000000 ? (capex/10000000).toFixed(1) + ' Cr' : (capex/100000).toFixed(1) + ' Lakh');
  document.getElementById('calcOrdersVal').textContent = orders + ' / day';
  document.getElementById('calcAovVal').textContent = '₹' + aov;
  document.getElementById('calcMarginVal').textContent = marginPct + '%';

  const monthlyRev = orders * aov * 30;
  const grossProfit = monthlyRev * (marginPct / 100);
  const p = FORMAT_PRESETS[currentFmt];
  const monthlyNet = Math.max(15000, grossProfit);
  const paybackMonths = Math.max(6, Math.min(36, Math.round(capex / monthlyNet)));
  const annualProfit = monthlyNet * 12;
  const annualRoi = Math.min(240, Math.round((annualProfit / capex) * 100));

  document.getElementById('resMonthlyRev').textContent = '₹' + (monthlyRev/100000).toFixed(2) + 'L';
  document.getElementById('resMonthlyNet').textContent = '₹' + (monthlyNet/100000).toFixed(2) + 'L';
  document.getElementById('resAnnualProfit').textContent = '₹' + (annualProfit/100000).toFixed(2) + 'L';
  document.getElementById('resAnnualRoi').textContent = annualRoi + '%';
  document.getElementById('resPayback').textContent = paybackMonths + ' Months';
}

// Initial binding
document.addEventListener('DOMContentLoaded', () => {
  ['calcCapex', 'calcOrders', 'calcAov', 'calcMargin'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', updateCalc);
  });
  if (document.getElementById('calcCapex')) updateCalc();
});
</script>
"""

if "function updateCalc()" not in f_html:
    f_html = f_html.replace('</body>', f"{CALC_SCRIPT}\n</body>")

with open("franchises.html", "w", encoding="utf-8") as f:
    f_html = f_html.replace('onclick="openBrandModal(\'', 'href="contact.html?brand=')
    f.write(f_html)

print("Updated franchises.html with clean aligned sections & interactive JS!")

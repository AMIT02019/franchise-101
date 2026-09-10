# -*- coding: utf-8 -*-
import re, os
from bs4 import BeautifulSoup

print("=== STARTING SYSTEMATIC SECTION ALIGNMENT RESOLUTION ===")

# ==============================================================================
# 1. UPDATE styles.css FOR BULLETPROOF SECTION & HEADING ALIGNMENT
# ==============================================================================
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add / improve .sec-top, .sec-head, and alignment utilities in styles.css
ALIGNMENT_CSS_ADDITIONS = """
/* ============ SECTION & HEADINGS ALIGNMENT RESOLUTION ============ */
.sec-top {
  display: flex !important;
  justify-content: space-between !important;
  align-items: flex-end !important;
  gap: 24px !important;
  flex-wrap: wrap !important;
  margin-bottom: clamp(28px, 4vw, 44px) !important;
}
.sec-top .sec-head {
  margin-bottom: 0 !important;
  flex: 1 1 320px !important;
  max-width: none !important;
}
.sec-top .sec-note {
  flex: 1 1 300px !important;
  max-width: 54ch !important;
}
.sec-head h2 {
  max-width: 32ch !important;
  line-height: 1.15 !important;
}
.sec-head.wide h2 {
  max-width: 40ch !important;
}
.sec-head.centered, .sec-centered {
  text-align: center !important;
  align-items: center !important;
  margin-inline: auto !important;
}
.sec-head.centered h2, .sec-centered h2 {
  margin-inline: auto !important;
}
.sec-head.centered .sec-note, .sec-centered .sec-note {
  margin-inline: auto !important;
}

/* Teaser Grid & Two-Column Split Alignment */
.teaser-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: clamp(24px, 4vw, 40px);
  align-items: center;
}
@media (max-width: 860px) {
  .teaser-grid {
    grid-template-columns: 1fr !important;
    gap: 28px !important;
  }
}

/* Universal Equal Height Flex for Grid Cards */
.grid-cards-equal > div,
.cards > article,
.steps > .step,
.scale-grid-3 > .scale-card,
.team-grid > .team-card {
  display: flex !important;
  flex-direction: column !important;
  height: 100% !important;
}

.grid-cards-equal > div > :last-child,
.cards > article > :last-child,
.scale-card > :last-child {
  margin-top: auto !important;
}
"""

if "/* ============ SECTION & HEADINGS ALIGNMENT RESOLUTION ============" not in css:
    css += "\n" + ALIGNMENT_CSS_ADDITIONS
    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated styles.css with robust alignment rules")


# ==============================================================================
# 2. STANDARDIZE NAV LINKS ACROSS ALL PAGES
# ==============================================================================
PAGES = [
    "index.html", "franq-franchise-website.html", "franchises.html", 
    "develop-brand.html", "develop-scale.html", "franchise-marketing.html", 
    "about.html", "contact.html", "find-franchise.html", "book-consultation.html",
    "beyond-temptation.html", "dunk-burgers.html", "mr-sandwich.html", 
    "south-twist.html", "cafe-choco-craze.html"
]

def get_nav_html(active_page):
    return f"""  <a class="logo" href="index.html" aria-label="Franchise 101 Home">FRANCHISE 101<span class="dot"></span></a>
  <div class="nav-links">
    <a href="index.html"{' class="active"' if active_page == 'index' else ''}>Home</a>
    <a href="franchises.html"{' class="active"' if active_page == 'franchises' else ''}>Explore Franchises</a>
    <a href="develop-brand.html"{' class="active"' if active_page == 'develop-brand' else ''}>Build Your Brand</a>
    <a href="develop-scale.html"{' class="active"' if active_page == 'develop-scale' else ''}>Franchise &amp; Scale</a>
    <a href="franchise-marketing.html"{' class="active"' if active_page == 'franchise-marketing' else ''}>Franchise Marketing</a>
    <a href="about.html"{' class="active"' if active_page == 'about' else ''}>About Us</a>
    <a href="contact.html"{' class="active"' if active_page in ['contact', 'book-consultation'] else ''}>Book a Consultation</a>
  </div>
  <div class="nav-cta-wrap">
    <a class="btn btn--kesar" href="contact.html">Book a Consultation <span class="arw">&rarr;</span></a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>"""

def get_mobile_drawer_html(active_page):
    return f"""    <div class="logo">FRANCHISE 101<span class="dot"></span></div>
    <nav>
      <a href="index.html" class="mobile-nav-link{' active' if active_page == 'index' else ''}">Home</a>
      <a href="franchises.html" class="mobile-nav-link{' active' if active_page == 'franchises' else ''}">Explore Franchises</a>
      <a href="develop-brand.html" class="mobile-nav-link{' active' if active_page == 'develop-brand' else ''}">Build Your Brand</a>
      <a href="develop-scale.html" class="mobile-nav-link{' active' if active_page == 'develop-scale' else ''}">Franchise &amp; Scale</a>
      <a href="franchise-marketing.html" class="mobile-nav-link{' active' if active_page == 'franchise-marketing' else ''}">Franchise Marketing</a>
      <a href="about.html" class="mobile-nav-link{' active' if active_page == 'about' else ''}">About Us</a>
      <a href="contact.html" class="mobile-nav-link{' active' if active_page in ['contact', 'book-consultation'] else ''}>Book a Consultation</a>
    </nav>
    <div style="margin-top:auto;display:flex;flex-direction:column;gap:12px">
      <a class="btn btn--kesar" href="contact.html" style="width:100%;text-align:center">Book a Consultation &rarr;</a>
      <p style="font-family:var(--font-mono, monospace);font-size:12px;color:rgba(248,250,252,.6);text-align:center">Zero fee &middot; Direct brand connect</p>
    </div>"""

for p in PAGES:
    if not os.path.exists(p):
        continue
    page_key = p.replace(".html", "")
    if "index" in page_key or "franq" in page_key:
        page_key = "index"
    
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace nav
    content = re.sub(r'<nav class="nav" id="nav">.*?</nav>', f'<nav class="nav" id="nav">\n{get_nav_html(page_key)}\n</nav>', content, flags=re.DOTALL)
    
    # Replace mobile drawer content
    content = re.sub(r'<div class="mobile-drawer-content">.*?</div>\s*</div>', f'<div class="mobile-drawer-content">\n{get_mobile_drawer_html(page_key)}\n  </div>\n</div>', content, flags=re.DOTALL)
    
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

print("Standardized Nav links and mobile drawer across all pages!")


# ==============================================================================
# 3. FIX ALIGNMENT SPECIFICALLY IN index.html
# ==============================================================================
with open("index.html", "r", encoding="utf-8") as f:
    idx = f.read()

# Fix internal CSS in index.html that had .sec-top grid-template-columns: minmax(0,1.5fr) minmax(0,1fr)
idx = re.sub(
    r'\.sec-top\s*\{[^}]*\}',
    """.sec-top{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:clamp(28px,4vw,44px)}
.sec-top .sec-head{margin-bottom:0;flex:1 1 320px;max-width:none}
.sec-top .sec-note{flex:1 1 300px;max-width:54ch}""",
    idx
)

# Remove the narrow max-width on h2 in index.html
idx = re.sub(r'\.sec-head h2\s*\{max-width:\s*15ch\}', '.sec-head h2{max-width:32ch}', idx)
idx = re.sub(r'\.sec-head\.wide h2\s*\{max-width:\s*20ch\}', '.sec-head.wide h2{max-width:40ch}', idx)

# Align the #faq section header with the accordion column
OLD_FAQ_HEADER = """<div class="sec-top rv" style="margin-bottom:32px">
      <div class="sec-head wide">
        <p class="eyebrow"><span class="pulse"></span> Frequently Asked Questions</p>
        <h2 style="color:var(--ink);font-size:clamp(26px, 3.5vw, 42px)">Clear Answers. Objective Insights.</h2>
        <p class="sec-note" style="color:var(--ink-80)">
          Everything you need to know about navigating the Franchise 101 ecosystem.
        </p>
      </div>
    </div>"""

NEW_FAQ_HEADER = """<div style="max-width:880px;margin:0 auto clamp(28px, 4vw, 44px)" class="rv">
      <div class="sec-head wide" style="margin-bottom:0">
        <p class="eyebrow"><span class="pulse"></span> Frequently Asked Questions</p>
        <h2 style="color:var(--ink);font-size:clamp(26px, 3.5vw, 42px)">Clear Answers. Objective Insights.</h2>
        <p class="sec-note" style="color:var(--ink-80);margin-top:4px">
          Everything you need to know about navigating the Franchise 101 ecosystem.
        </p>
      </div>
    </div>"""

idx = idx.replace(OLD_FAQ_HEADER, NEW_FAQ_HEADER)

# Fix #find-match-teaser to use .teaser-grid for responsive alignment
idx = idx.replace(
    'style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:clamp(24px, 4vw, 36px);padding:clamp(32px, 5vw, 56px);display:grid;grid-template-columns:1.2fr 1fr;gap:36px;align-items:center;box-shadow:0 16px 45px -15px rgba(14,18,26,0.08)"',
    'class="teaser-grid" style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:clamp(24px, 4vw, 36px);padding:clamp(32px, 5vw, 56px);box-shadow:0 16px 45px -15px rgba(14,18,26,0.08)"'
)

# Move modal & back-to-top button from inside content to after </footer>
modal_search = re.search(r'(<div aria-labelledby="modalTitle".*?<!-- Back to Top Button -->\s*<button.*?<\/button>)', idx, re.DOTALL)
if modal_search:
    modal_block = modal_search.group(1)
    # Remove from current position
    idx = idx.replace(modal_block, '')
    # Put right before </body>
    idx = idx.replace('</body>', f"{modal_block}\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(idx)

print("Fixed alignment in index.html & franq-franchise-website.html")


# ==============================================================================
# 4. FIX ALIGNMENT IN franchises.html
# ==============================================================================
with open("franchises.html", "r", encoding="utf-8") as f:
    f_html = f.read()

# Fix #calculator wrapping so it is a standard full-width .sec with inner .wrap
OLD_CALC_TAG = '<section class="wrap" id="calculator">'
NEW_CALC_TAG = '<section class="sec" id="calculator" style="background:var(--paper);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:clamp(64px, 8vw, 100px) 0">\n  <div class="wrap">'

if OLD_CALC_TAG in f_html:
    f_html = f_html.replace(OLD_CALC_TAG, NEW_CALC_TAG)
    # Also add closing </div> before </section>
    f_html = f_html.replace('</section>\n\n<footer class="foot on-dark">', '  </div>\n</section>\n\n<footer class="foot on-dark">')

# Fix #budget rail-head padding and wrap alignment
OLD_BUDGET_START = """<section class="brackets" id="budget">
  <div class="rail-outer" id="railOuter">
    <div class="rail-sticky on-dark">
      <div class="rail-head">
        <div class="sec-top" style="margin-bottom:0">
          <div class="sec-head wide">
            <p class="eyebrow">By budget</p>
            <h2 style="color:var(--malai)">What &#8377;6 lakh buys, and what &#8377;60 lakh does.</h2>
          </div>
          <p class="sec-note">Pick the bracket you can fund without borrowing against the house. The format follows the capital, not the other way round.</p>
        </div>
      </div>"""

NEW_BUDGET_START = """<section class="brackets" id="budget">
  <div class="rail-outer" id="railOuter">
    <div class="rail-sticky on-dark">
      <div class="rail-head wrap">
        <div class="sec-top" style="margin-bottom:0">
          <div class="sec-head wide">
            <p class="eyebrow">By budget</p>
            <h2 style="color:var(--malai)">What &#8377;6 lakh buys, and what &#8377;60 lakh does.</h2>
          </div>
          <p class="sec-note">Pick the bracket you can fund without borrowing against the house. The format follows the capital, not the other way round.</p>
        </div>
      </div>"""

f_html = f_html.replace(OLD_BUDGET_START, NEW_BUDGET_START)

with open("franchises.html", "w", encoding="utf-8") as f:
    f.write(f_html)

print("Fixed alignment in franchises.html")


# ==============================================================================
# 5. FIX ALIGNMENT IN develop-brand.html & develop-scale.html
# ==============================================================================
def fix_service_cards(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Ensure card grids have equal-height and bottom alignment
    content = content.replace(
        'style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:22px"',
        'class="grid-cards-equal rv" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:22px"'
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

fix_service_cards("develop-brand.html")
fix_service_cards("develop-scale.html")
fix_service_cards("about.html")
print("Applied card alignment fixes across develop-brand, develop-scale, and about")

print("=== ALL SECTION ALIGNMENTS RESOLVED SUCCESSFULLY ===")

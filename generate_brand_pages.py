# -*- coding: utf-8 -*-
import os

# Base template builder for individual brand pages
def create_brand_page(brand_id, brand_name, category, tagline, investment, payback, margin, area, outlets, states, hero_img, food_img, store_img, desc, capex_items, capex_total, formats, menu_items, pnl_data, video_file="assets/videos/chocolate_craft.mp4", video_title="Central Kitchen Craft & SOPs"):
    
    # Formats HTML
    formats_html = ""
    for f in formats:
        formats_html += f"""
        <div class="card rv" style="background:var(--paper-card);border:1px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:12px">
          <div style="display:flex;justify-content:space-between;align-items:flex-start">
            <span class="tag gold">{f['tag']}</span>
            <strong style="font-size:22px;color:var(--kesar);font-family:var(--font-editorial)">{f['cost']}</strong>
          </div>
          <h3 style="font-size:20px;margin:0;color:var(--ink)">{f['name']}</h3>
          <p style="font-size:14px;color:var(--ink-60);line-height:1.55;margin:0">{f['desc']}</p>
          <div style="font-family:var(--font-mono);font-size:12.5px;color:var(--ink-60);margin-top:auto;border-top:1px solid var(--line);padding-top:12px">
            <div><strong>Space:</strong> {f['space']}</div>
            <div style="margin-top:4px"><strong>Ideal For:</strong> {f['ideal']}</div>
          </div>
        </div>
        """

    # Capex Rows HTML
    capex_rows = ""
    for item in capex_items:
        capex_rows += f"<tr><td>{item['name']}</td><td>{item['scope']}</td><td>{item['amount']}</td></tr>"

    # Menu Showcase HTML
    menu_html = ""
    for m in menu_items:
        menu_html += f"""
        <div style="background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:6px">
          <strong style="font-size:16px;color:var(--ink)">{m['title']}</strong>
          <span style="font-size:13.5px;color:var(--ink-60)">{m['desc']}</span>
          <span style="font-family:var(--font-mono);font-size:11.5px;color:var(--kesar);font-weight:700;margin-top:auto">{m['highlight']}</span>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{brand_name} Franchise — Cost, ROI, Profit &amp; Capex Sheet — Franchise 101</title>
<meta name="description" content="Official franchise details for {brand_name}. Investment {investment}, {margin} net margin, {payback} payback. Download audited capex sheet and apply for territory exclusivity." />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;0,9..144,800;1,9..144,400;1,9..144,600;1,9..144,700&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="styles.css" />
<style>
.brand-hero-grid {{
  display: grid; grid-template-columns: 1.15fr 1fr; gap: clamp(32px, 5vw, 64px); align-items: center;
}}
@media (max-width: 900px) {{ .brand-hero-grid {{ grid-template-columns: 1fr; }} }}

.brand-hero-img-box {{
  border-radius: 24px; overflow: hidden; position: relative; box-shadow: 0 25px 60px -20px rgba(0,0,0,0.5);
  border: 1.5px solid rgba(255, 243, 222, 0.2); aspect-ratio: 4/3;
}}
.brand-hero-img-box img {{ width: 100%; height: 100%; object-fit: cover; }}

.econ-summary-bar {{
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;
  background: var(--paper-card); border: 1px solid var(--line); border-radius: 18px; padding: 20px;
  box-shadow: 0 10px 30px -10px rgba(26,20,32,0.06); margin-top: -36px; position: relative; z-index: 10;
}}
@media (max-width: 768px) {{ .econ-summary-bar {{ grid-template-columns: 1fr 1fr; margin-top: -20px; }} }}

.econ-stat-item small {{ display: block; font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--ink-60); }}
.econ-stat-item strong {{ display: block; font-size: 20px; font-weight: 800; color: var(--ink); margin-top: 4px; }}

.capex-table-wrap {{
  background: #FFF; border: 1px solid var(--line); border-radius: 16px; overflow: hidden;
  box-shadow: 0 10px 25px -10px rgba(26,20,32,0.06);
}}
.capex-table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
.capex-table th, .capex-table td {{ padding: 12px 16px; border-bottom: 1px solid var(--line); text-align: left; }}
.capex-table th {{ background: rgba(26,20,32,0.04); font-family: var(--font-mono); font-size: 11.5px; text-transform: uppercase; color: var(--ink-60); }}
.capex-table td:last-child {{ text-align: right; font-family: var(--font-mono); font-weight: 700; color: var(--ink); }}
.capex-table tr.total-row {{ background: rgba(255,176,32,0.1); font-weight: 800; }}
.capex-table tr.total-row td {{ font-size: 15px; color: var(--ink); border-bottom: none; }}

.pnl-card {{
  background: var(--jamun-deep); color: var(--malai); border-radius: 20px; padding: clamp(24px, 4vw, 36px);
  border: 1px solid rgba(255,243,222,0.15); box-shadow: 0 20px 50px -15px rgba(10,3,18,0.5);
}}
@media (min-width: 901px) {{
  .pnl-card {{
    position: -webkit-sticky;
    position: sticky;
    top: 96px;
    z-index: 10;
    will-change: transform;
  }}
}}
.pnl-row {{
  display: flex; justify-content: space-between; align-items: center; padding: 10px 0;
  border-bottom: 1px solid rgba(255,243,222,0.12); font-size: 14.5px;
}}
.pnl-row:last-child {{ border-bottom: none; }}
.pnl-row strong {{ font-family: var(--font-mono); font-size: 16px; color: var(--kesar); }}
</style>
</head>
<body>

<div class="top-progress" id="topProgress"></div>

<!-- ============ FLOATING PILL CAPSULE NAV ============ -->
<nav class="nav" id="nav">
  <a class="logo" href="index.html" aria-label="Franchise 101 Home">FRANCHISE 101<span class="dot"></span></a>
  <div class="nav-links">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="franchises.html" class="active">Franchises</a>
    <a href="develop-brand.html">Develop Brand</a>
    <a href="develop-scale.html">Develop &amp; Scale</a>
    <a href="franchise-marketing.html">Marketing</a>
    <a href="find-franchise.html">Find Match</a>
    <a href="book-consultation.html">Contact</a>
  </div>
  <div class="nav-cta-wrap">
    <a class="btn btn--kesar" href="book-consultation.html?brand={brand_name.replace(' ', '+')}">Book Consultation <span class="arw">&rarr;</span></a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- Mobile Navigation Drawer -->
<div class="mobile-drawer" id="mobileDrawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation">
  <div class="mobile-drawer-content">
    <div class="logo">FRANCHISE 101<span class="dot"></span></div>
    <nav>
      <a href="index.html" class="mobile-nav-link">Home</a>
      <a href="about.html" class="mobile-nav-link">About Franchise 101</a>
      <a href="franchises.html" class="mobile-nav-link active">Franchise Opportunities</a>
      <a href="develop-brand.html" class="mobile-nav-link">Develop Your Own Brand</a>
      <a href="develop-scale.html" class="mobile-nav-link">Develop &amp; Scale</a>
      <a href="franchise-marketing.html" class="mobile-nav-link">Franchise Marketing</a>
      <a href="find-franchise.html" class="mobile-nav-link">Find The Right Franchise</a>
      <a href="book-consultation.html" class="mobile-nav-link">Book a Consultation</a>
    </nav>
    <div style="margin-top:auto;display:flex;flex-direction:column;gap:12px">
      <a class="btn btn--kesar" href="book-consultation.html?brand={brand_name.replace(' ', '+')}" style="width:100%;text-align:center">Apply For {brand_name} &rarr;</a>
      <p style="font-size:12px;color:rgba(255,243,222,.6);text-align:center">Zero brokerage &middot; Direct brand connect</p>
    </div>
  </div>
</div>

<!-- ============ BRAND HERO ============ -->
<header class="page-hero on-dark">
  <div class="wrap">
    <div class="brand-hero-grid">
      <div>
        <div class="badge-trust rise">
          <span class="pulse"></span> Verified Brand &middot; {outlets} Outlets in {states}
        </div>
        <h1 class="rise">{brand_name} <em>Franchise<span class="strike"></span></em></h1>
        <p class="page-hero-sub rise" style="margin-bottom:14px">{tagline}</p>
        <p class="rise" style="color:rgba(255,243,222,.8);font-size:15px;line-height:1.6;margin-bottom:24px">{desc}</p>
        
        <div class="rise" style="display:flex;gap:12px;flex-wrap:wrap;align-items:center">
          <a class="btn btn--kesar" href="#apply-brand">Apply For Territory <span class="arw">&rarr;</span></a>
          <a class="btn btn--ghost on-dark" href="#capex-breakdown">View Capex Breakdown</a>
          <a class="btn btn--ghost on-dark" href="franchises.html">&larr; All Brands</a>
        </div>
      </div>
      
      <div class="brand-hero-img-box rise">
        <img src="{hero_img}" alt="{brand_name} Storefront & Food" />
      </div>
    </div>
  </div>
</header>

<!-- ============ SUMMARY BAR ============ -->
<section style="padding:0">
  <div class="wrap">
    <div class="econ-summary-bar rv">
      <div class="econ-stat-item">
        <small>Total Investment</small>
        <strong style="color:var(--kesar)">{investment}</strong>
      </div>
      <div class="econ-stat-item">
        <small>Est. Net Margin</small>
        <strong style="color:var(--pista)">{margin}</strong>
      </div>
      <div class="econ-stat-item">
        <small>Est. Payback</small>
        <strong>{payback}</strong>
      </div>
      <div class="econ-stat-item">
        <small>Space Required</small>
        <strong>{area}</strong>
      </div>
    </div>
  </div>
</section>

<!-- ============ FRANCHISE FORMATS ============ -->
<section class="sec">
  <div class="wrap">
    <div class="sec-head wide rv" style="margin-bottom:32px">
      <p class="eyebrow">Investment Options</p>
      <h2>Available Store Formats for {brand_name}</h2>
      <p class="sec-note">Choose the layout and capital model that fits your available commercial shutter or target territory.</p>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:20px">
      {formats_html}
    </div>
  </div>
</section>

<!-- ============ SIGNATURE MENU SHOWCASE ============ -->
<section class="sec on-dark" style="background:var(--jamun-soft)">
  <div class="wrap">
    <div class="sec-head wide rv" style="margin-bottom:32px">
      <p class="eyebrow on-dark">High Margin Products</p>
      <h2 style="color:var(--malai)">Signature Menu &amp; Hero Offerings</h2>
      <p class="sec-note on-dark">Standardized chef-less pre-mix formulations ensure zero wastage and identical taste across all branches.</p>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:16px" class="rv">
      {menu_html}
    </div>
  </div>
</section>

<!-- ============ CENTRAL KITCHEN & OPS VIDEO SHOWCASE ============ -->
<section class="sec on-dark" style="background:var(--jamun-deep);position:relative;overflow:hidden">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px, 4vw, 56px);align-items:center">
      <div class="rv">
        <div class="badge-trust" style="margin-bottom:12px"><span class="pulse"></span> Standardized Food Manufacturing</div>
        <h2 style="color:var(--malai)">Behind the Taste: Proprietary Central Supply</h2>
        <p style="color:rgba(255,243,222,0.85);font-size:15px;line-height:1.65;margin-bottom:20px">
          {brand_name} eliminates skilled-chef dependency. Over 85% of core bases, signature seasonings, and pre-mixes are manufactured at central facilities and delivered directly to your outlet.
        </p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <div style="background:rgba(255,243,222,0.06);border:1px solid rgba(255,243,222,0.14);border-radius:12px;padding:14px">
            <strong style="color:var(--kesar);display:block;font-size:18px">0% Wastage</strong>
            <span style="font-size:12.5px;color:rgba(255,243,222,0.75)">Pre-portioned batches</span>
          </div>
          <div style="background:rgba(255,243,222,0.06);border:1px solid rgba(255,243,222,0.14);border-radius:12px;padding:14px">
            <strong style="color:var(--pista);display:block;font-size:18px">100% Chef-Less</strong>
            <span style="font-size:12.5px;color:rgba(255,243,222,0.75)">3-minute SOP training</span>
          </div>
        </div>
      </div>

      <div class="rv" style="position:relative;border-radius:24px;overflow:hidden;border:1.5px solid rgba(255,243,222,0.2);box-shadow:0 25px 60px -20px rgba(0,0,0,0.6)">
        <video autoplay muted loop playsinline preload="metadata" style="width:100%;height:100%;object-fit:cover;display:block">
          <source src="{video_file}" type="video/mp4">
        </video>
        <span class="tag gold" style="position:absolute;top:16px;left:16px;z-index:2">{video_title}</span>
      </div>
    </div>
  </div>
</section>

<!-- ============ AUDITED CAPEX & P&L SECTION ============ -->
<section class="sec" id="capex-breakdown">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:clamp(32px, 4vw, 56px);align-items:start">
      
      <!-- Left: Capex Table -->
      <div>
        <div class="sec-head rv" style="margin-bottom:24px">
          <p class="eyebrow">Audited Capex Sheet</p>
          <h2>Itemized Store Setup Cost</h2>
          <p class="sec-note">Official breakdown from brand brochure for turnkey setup.</p>
        </div>

        <div class="capex-table-wrap rv">
          <table class="capex-table">
            <tr><th>Component</th><th>Deliverables &amp; Scope</th><th>Cost</th></tr>
            {capex_rows}
            <tr class="total-row"><td><strong>Total Capex</strong></td><td><strong>Turnkey Setup (Excl. Taxes)</strong></td><td><strong>{capex_total}</strong></td></tr>
          </table>
        </div>
      </div>

      <!-- Right: Projected Monthly Unit Economics -->
      <div>
        <div class="sec-head rv" style="margin-bottom:24px">
          <p class="eyebrow">Unit Economics</p>
          <h2>Projected Monthly P&amp;L</h2>
          <p class="sec-note">Audited outlet financial model based on average footfall.</p>
        </div>

        <div class="pnl-card rv">
          <div class="pnl-row"><span>Avg Daily Orders</span><strong>{pnl_data['daily_orders']}</strong></div>
          <div class="pnl-row"><span>Avg Order Value (AOV)</span><strong>{pnl_data['aov']}</strong></div>
          <div class="pnl-row"><span>Monthly Gross Revenue</span><strong>{pnl_data['gross_rev']}</strong></div>
          <div class="pnl-row"><span>Raw Material / Food Cost</span><strong style="color:var(--pista)">{pnl_data['food_cost']}</strong></div>
          <div class="pnl-row"><span>Gross Profit</span><strong>{pnl_data['gross_profit']}</strong></div>
          <div class="pnl-row"><span>Store Expenses (Rent, Staff, Power)</span><strong>{pnl_data['expenses']}</strong></div>
          <div class="pnl-row" style="background:rgba(255,176,32,0.15);padding:14px;border-radius:12px;margin-top:10px">
            <span style="font-weight:800;color:var(--malai);font-size:16px">Monthly Net Profit</span>
            <strong style="font-size:22px;color:var(--kesar)">{pnl_data['net_profit']}</strong>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ============ APPLICATION FORM SECTION ============ -->
<section class="sec" id="apply-brand" style="background:var(--paper);padding:clamp(70px, 8vw, 100px) 0 clamp(90px, 10vw, 130px)">
  <div class="wrap">
    <div style="max-width:760px;margin:0 auto">
      <div class="sec-head wide text-center rv" style="text-align:center;margin-bottom:36px">
        <p class="eyebrow">Direct Founder Connect</p>
        <h2>Apply For {brand_name} Franchise</h2>
        <p class="sec-note" style="margin:0 auto">Zero brokerage fee. A dedicated Franchise 101 advisor will review your location and coordinate directly with {brand_name} brand directors.</p>
      </div>

      <div style="background:var(--paper-card);border:1px solid var(--line);border-radius:24px;padding:clamp(32px, 5vw, 48px);box-shadow:0 15px 40px -15px rgba(26,20,32,0.08)" class="rv">
        <form class="form" onsubmit="handleBrandApply(event)">
          <div class="field">
            <label for="bname">Full Name *</label>
            <input type="text" id="bname" placeholder="Rohan Deshmukh" required />
          </div>

          <div class="field">
            <label for="bphone">Mobile Number (WhatsApp) *</label>
            <input type="tel" id="bphone" placeholder="9820012345" required />
          </div>

          <div class="field">
            <label for="bcity">Target City / Catchment Area *</label>
            <input type="text" id="bcity" placeholder="Pune (Kothrud / Baner)" required />
          </div>

          <div class="field">
            <label for="bformat">Preferred Format *</label>
            <select id="bformat" required>
              <option value="">Select format</option>
              {"".join([f'<option value="{f["name"]}">{f["name"]} ({f["cost"]})</option>' for f in formats])}
            </select>
          </div>

          <div class="field full">
            <label for="bspace">Do you have a commercial property?</label>
            <select id="bspace">
              <option value="identifying">Actively identifying high-footfall location</option>
              <option value="owned">I own a commercial shop / space</option>
              <option value="rented">I have already rented a location</option>
              <option value="need_help">Need Franchise 101 site-selection advisory</option>
            </select>
          </div>

          <div id="applySuccess" style="display:none;background:rgba(169,232,107,0.2);border:1px solid var(--pista);border-radius:12px;padding:18px;margin:18px 0;color:var(--ink)">
            <strong style="color:var(--jamun-deep);font-size:16px">&#10003; Application Submitted Successfully!</strong>
            <p style="font-size:14px;margin:6px 0 0;color:var(--ink-80)">Your inquiry for {brand_name} has been routed to our senior team. A dedicated franchise manager will call you with the complete P&amp;L projection within 24 hours.</p>
          </div>

          <div class="form-actions">
            <button type="submit" class="btn btn--kesar" id="btnSubmitApply" style="padding:14px 30px;font-size:15px">
              Submit Application &rarr;
            </button>
            <a class="btn btn--ghost" href="https://wa.me/912240008899?text=Hi%2C%20I%20am%20interested%20in%20{brand_name}%20Franchise" target="_blank" style="padding:14px 24px">
              Chat on WhatsApp &#128172;
            </a>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- ============ FOOTER ============ -->
<footer class="foot on-dark">
  <div class="wrap">
    <div class="foot-banner">
      <div class="foot-banner-text">
        <h3>Explore other verified franchise opportunities</h3>
        <p>Compare all 5 curated F&amp;B brands side-by-side with audited capex sheets.</p>
      </div>
      <div class="foot-banner-actions">
        <a class="btn btn--kesar" href="franchises.html">All 5 Franchise Brands &rarr;</a>
        <a class="btn btn--ghost on-dark" href="find-franchise.html">Take Matching Quiz</a>
      </div>
    </div>

    <div class="foot-grid">
      <div class="foot-brand">
        <div class="logo">FRANCHISE 101<span class="dot"></span></div>
        <p>India's definitive food franchise intelligence and advisory platform. Connecting qualified investors with audited F&amp;B brands.</p>
        <div class="foot-contacts">
          <div>Email: <a href="mailto:partners@franchise101.in">partners@franchise101.in</a></div>
          <div>Phone: <a href="tel:+912240008899">+91 22 4000 8899</a></div>
        </div>
      </div>
      <div class="foot-col">
        <h4>Flagship Brands</h4>
        <ul>
          <li><a href="beyond-temptation.html">Beyond Temptation <small>&#8377;13&ndash;20L</small></a></li>
          <li><a href="dunk-burgers.html">Dunk Burgers <small>&#8377;15&ndash;25L</small></a></li>
          <li><a href="mr-sandwich.html">Mr. Sandwich <small>&#8377;9&ndash;17.5L</small></a></li>
          <li><a href="south-twist.html">South Twist <small>&#8377;10&ndash;20L</small></a></li>
          <li><a href="cafe-choco-craze.html">Cafe Choco Craze <small>&#8377;8&ndash;20L</small></a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h4>For Brand Owners</h4>
        <ul>
          <li><a href="develop-brand.html">Develop Your Own Brand</a></li>
          <li><a href="develop-scale.html">Develop &amp; Scale (Multi-City)</a></li>
          <li><a href="franchise-marketing.html">Franchise Marketing &amp; Leads</a></li>
          <li><a href="book-consultation.html?service=brand-growth">Brand Advisory Audit</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h4>Regional Desks</h4>
        <ul>
          <li><a href="book-consultation.html">BKC, Mumbai</a></li>
          <li><a href="book-consultation.html">Balewadi High St, Pune</a></li>
          <li><a href="book-consultation.html">Indiranagar, Bengaluru</a></li>
          <li><a href="book-consultation.html">Cyber City, Gurugram</a></li>
        </ul>
      </div>
    </div>

    <div class="foot-base">
      <div>&copy; 2026 Franchise 101 Advisory LLP. All rights reserved.</div>
      <div class="foot-status"><span class="dot-pulse"></span> Q1 2026 Batch Open</div>
    </div>
  </div>
</footer>

<button class="floating-up" id="btnBackToTop" aria-label="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&#8593;</button>

<script>
const nav = document.getElementById('nav');
const topProgress = document.getElementById('topProgress');
const btnBackToTop = document.getElementById('btnBackToTop');
const navToggle = document.getElementById('navToggle');
const mobileDrawer = document.getElementById('mobileDrawer');

let lastScrollY = window.scrollY;
const scrollDeltaThreshold = 8;

window.addEventListener('scroll', () => {{
  const scrolled = window.scrollY;
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  const progress = maxScroll > 0 ? (scrolled / maxScroll) * 100 : 0;
  
  if (topProgress) topProgress.style.width = progress + '%';
  if (btnBackToTop) btnBackToTop.classList.toggle('show', scrolled > 400);

  if (nav) {{
    nav.classList.toggle('stuck', scrolled > 20);

    const isDrawerOpen = mobileDrawer && mobileDrawer.classList.contains('open');

    if (!isDrawerOpen) {{
      if (scrolled <= 30) {{
        nav.classList.remove('nav--hidden');
      }} else if (scrolled > lastScrollY + scrollDeltaThreshold && scrolled > 80) {{
        nav.classList.add('nav--hidden');
      }} else if (scrolled < lastScrollY - scrollDeltaThreshold) {{
        nav.classList.remove('nav--hidden');
      }}
    }}
  }}
  lastScrollY = scrolled;
}});

if (navToggle && mobileDrawer) {{
  navToggle.addEventListener('click', () => {{
    const isOpen = mobileDrawer.classList.toggle('open');
    navToggle.classList.toggle('open', isOpen);
    navToggle.setAttribute('aria-expanded', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  }});
}}

// Reveal elements on scroll
const io = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{
    if (e.isIntersecting) {{
      e.target.classList.add('in');
      io.unobserve(e.target);
    }}
  }});
}}, {{ threshold: 0.05, rootMargin: '0px 0px 50px' }});
document.querySelectorAll('.rv').forEach(el => io.observe(el));

function handleBrandApply(e) {{
  e.preventDefault();
  document.getElementById('applySuccess').style.display = 'block';
  document.getElementById('btnSubmitApply').style.display = 'none';
}}
</script>
</body>
</html>"""

# ==============================================================================
# DATA FOR 5 INDIVIDUAL BRANDS
# ==============================================================================

# 1. BEYOND TEMPTATION
bt_html = create_brand_page(
    brand_id="beyond-temptation",
    brand_name="Beyond Temptation",
    category="Dessert & Multi-Cuisine Cafe",
    tagline="India's Iconic Dessert & Cafe Chain Since 2009",
    investment="₹13–20 Lakh",
    payback="12–16 Months",
    margin="> 35% Net",
    area="300–2,000 sq.ft",
    outlets="90+",
    states="8 States",
    hero_img="assets/brands/beyond-temptation.png",
    food_img="assets/brands/beyond_temptation_food.png",
    store_img="assets/brands/beyond_temptation_store.png",
    desc="Established in 2009 with 15+ years of in-house food manufacturing in Pune supplying >85% of menu raw materials. Renowned for Cad-Bee chocolate thick shakes, BT Special Cold Coffee, Mango Mastani, artisanal pizzas, burgers, momos and freak shakes. Chef-less zero wastage model.",
    capex_items=[
        {"name": "Franchise Brand Fee", "scope": "5-Year Agreement, Operations Training & Certification", "amount": "₹5,00,000"},
        {"name": "Commercial Kitchen & Espresso", "scope": "Espresso machines, induction lines, shake blenders & coolers", "amount": "₹4,50,000"},
        {"name": "Cafe Interior & 3D CAD Fitout", "scope": "Seating, counter design, acoustic lighting, neon branding", "amount": "₹4,00,000"},
        {"name": "Opening Raw Material & Packs", "scope": "Cad-Bee chocolate bases, syrups, pre-mixes, cups & packaging", "amount": "₹1,50,000"},
        {"name": "Billing ERP, POS & Compliance", "scope": "Touch POS terminal, inventory app, FSSAI & accounting setup", "amount": "₹1,00,000"}
    ],
    capex_total="₹16,00,000",
    formats=[
        {"name": "Compact Cafe", "cost": "₹13–15 Lakh", "tag": "High-Footfall Express", "space": "300–500 sq.ft", "ideal": "College hubs, transit points & tech parks", "desc": "Focused menu on Cad-Bee shakes, coffees, burgers and quick bites with minimal kitchen footprint."},
        {"name": "Lounge Cafe", "cost": "₹15–20 Lakh", "tag": "Flagship Dine-in", "space": "500–1,000 sq.ft", "ideal": "High streets, family markets & youth hubs", "desc": "Full dine-in cafe seating with complete dessert, pizza, pasta, burger & mocktail menu."},
        {"name": "Master Franchise", "cost": "₹50–80 Lakh", "tag": "Territory Rights", "space": "City / Multi-Unit Territory", "ideal": "Strategic investors & multi-unit operators", "desc": "Exclusive territorial rights, 40-50% franchise fee sharing & raw material revenue share."}
    ],
    menu_items=[
        {"title": "Cad-Bee Thick Shake", "desc": "Signature rich chocolate blend that built the brand across Maharashtra.", "highlight": "High Margin · Hero Product"},
        {"title": "BT Special Cold Coffee", "desc": "Creamy thick cold coffee with decadent chocolate swirls.", "highlight": "Highest Daily Volume"},
        {"title": "Mango Mastani", "desc": "Authentic Pune dessert drink with mango pulp, ice cream & dry fruits.", "highlight": "High Repeat Footfall"},
        {"title": "Gourmet Pizzas & Burgers", "desc": "Cheese burst pizzas and crispy patty burgers with in-house sauces.", "highlight": "Evening Dining Pull"}
    ],
    video_file="assets/videos/chocolate_craft.mp4",
    video_title="Cad-Bee & Chocolate Craft",
    pnl_data={
        "daily_orders": "140–180 Orders",
        "aov": "₹220",
        "gross_rev": "₹9,24,000 / mo",
        "food_cost": "32% (₹2,95,680)",
        "gross_profit": "68% (₹6,28,320)",
        "expenses": "₹4,10,000 (Rent, Staff, Power)",
        "net_profit": "₹2,18,320 / month"
    }
)

# 2. DUNK BURGERS
db_html = create_brand_page(
    brand_id="dunk-burgers",
    brand_name="Dunk Burgers",
    category="Dip-In Burgers & Fast Food",
    tagline="India's First Dip-In Burger Brand · Zero Royalty Model",
    investment="₹15–25 Lakh",
    payback="12–15 Months",
    margin="> 38% Net",
    area="300–1,000 sq.ft",
    outlets="16+ Years Experience",
    states="Pan-India Ready",
    hero_img="assets/brands/dunk-burgers.png",
    food_img="assets/brands/dunk_burgers_dip.png",
    store_img="assets/brands/dunk_burgers_cover.png",
    desc="India's First Dip-In Burger Brand. 16+ years of manufacturing and franchising expertise. Famous for dipping hot burgers into warm signature sauce baths (Mushroom Stroganoff, New York Mash, Latino Heat), crispy fiery wings, Korean loaded fries, Cad-B shakes & boba beverages. Zero royalty model — keep 100% of your profits.",
    capex_items=[
        {"name": "Franchise Setup & Brand Rights", "scope": "Turnkey franchise license, SOPs & pre-launch guidance", "amount": "₹4,50,000"},
        {"name": "Commercial Griddles & Fryers", "scope": "High-speed flat griddle, twin deep fryers, deep refrigeration", "amount": "₹5,00,000"},
        {"name": "Store Interior & Neon Dip Signage", "scope": "Dip station fabrication, acoustic lighting, dynamic menu board", "amount": "₹4,80,000"},
        {"name": "Initial Stock & Patty Batches", "scope": "Pre-seasoned patties, signature dip sauces, buns & packaging", "amount": "₹1,50,000"},
        {"name": "POS Hardware & Marketing Launch", "scope": "Billing system, Swiggy/Zomato onboarding & launch campaign", "amount": "₹1,20,000"}
    ],
    capex_total="₹17,00,000",
    formats=[
        {"name": "Express Cafe", "cost": "₹15–17 Lakh", "tag": "Zero Royalty Format", "space": "300–500 sq.ft", "ideal": "High-footfall high streets & transit points", "desc": "Streamlined burger, wing & shake counter with fast 3-minute order fulfillment."},
        {"name": "Lounge Cafe", "cost": "₹20–25 Lakh", "tag": "Youth Experience", "space": "500–1,000 sq.ft", "ideal": "Mall food courts & popular hangout streets", "desc": "Vibrant dine-in atmosphere with full dip-in menu, wings, fries, sizzlers & shakes."},
        {"name": "Master Franchise", "cost": "₹49.99 Lakh+", "tag": "State / Regional Rights", "space": "Territory Development", "ideal": "Experienced F&B operators & city developers", "desc": "Exclusive multi-unit expansion rights with significant franchise fee splits."}
    ],
    menu_items=[
        {"title": "Signature Dip-In Burgers", "desc": "Served with deep warm bowls of Mushroom Stroganoff & Latino Heat sauces.", "highlight": "Social Media Viral Hero"},
        {"title": "Crispy Fiery Wings", "desc": "Double-fried crunchy chicken & veg wings tossed in signature rubs.", "highlight": "High Margin"},
        {"title": "Korean Loaded Fries", "desc": "Crispy fries loaded with melted cheese, jalapenos and spicy drizzle.", "highlight": "Add-On Ticket Booster"},
        {"title": "Cad-B & Boba Shakes", "desc": "Thick chocolate shakes and refreshing fruit boba drinks.", "highlight": "High Margin Beverage"}
    ],
    video_file="assets/videos/dessert_donuts.mp4",
    video_title="Dip Station & High-Speed Assembly",
    pnl_data={
        "daily_orders": "150–200 Orders",
        "aov": "₹240",
        "gross_rev": "₹10,80,000 / mo",
        "food_cost": "30% (₹3,24,000)",
        "gross_profit": "70% (₹7,56,000)",
        "expenses": "₹4,80,000 (Rent, Staff, Power)",
        "net_profit": "₹2,76,000 / month"
    }
)

# 3. MR. SANDWICH
ms_html = create_brand_page(
    brand_id="mr-sandwich",
    brand_name="Mr. Sandwich",
    category="European Subs & Sandwiches",
    tagline="India's Largest Brand in the Sandwich Segment · Top 200 Franchise Brand",
    investment="₹9–17.5 Lakh",
    payback="8–12 Months",
    margin="39%–42% Net",
    area="100–600 sq.ft",
    outlets="200+",
    states="100+ Cities & 20+ States",
    hero_img="assets/brands/mr-sandwich.png",
    food_img="assets/brands/mr_sandwich_spread.png",
    store_img="assets/brands/mr_sandwich_kiosk.png",
    desc="India's Largest Brand in the Sandwich Segment. 200+ Outlets across 100+ Cities & 20+ States + 5 International Outlets. Famous for European-style gourmet subs, grilled paninis, cheesy burgers, pastas and artisanal shakes. Audited ₹15L–₹21.18L annual net profit per outlet.",
    capex_items=[
        {"name": "Franchise Fee (Single Unit)", "scope": "Brand License, Training, Operational SOPs & Central Supply", "amount": "₹5,00,000"},
        {"name": "Infrastructure & Interior Fitout", "scope": "400-600 sqft complete store fabrication, wooden finish & seating", "amount": "₹6,00,000"},
        {"name": "Machineries & Equipment", "scope": "Commercial sandwich grills, salamander, refrigeration line", "amount": "₹3,00,000"},
        {"name": "Branding & Signage Board", "scope": "Facade glow-sign board, indoor graphics, LED menu displays", "amount": "₹1,00,000"},
        {"name": "Refundable Security Deposit", "scope": "100% Refundable brand security deposit", "amount": "₹1,00,000"},
        {"name": "Opening Stock + POS Hardware", "scope": "Gourmet sauces, breads, packaging + billing terminal", "amount": "₹1,50,000"}
    ],
    capex_total="₹17,50,000",
    formats=[
        {"name": "Takeaway Model", "cost": "₹9.0 Lakh", "tag": "Lowest Entry Cost", "space": "100–200 sq.ft", "ideal": "High-footfall markets, college lanes & metro stations", "desc": "Compact kiosk setup with commercial grills and takeaway packaging with rapid 8-month payback."},
        {"name": "Stand-Alone Store", "cost": "₹17.5 Lakh", "tag": "Most Popular", "space": "400–600 sq.ft", "ideal": "Commercial high streets & family retail belts", "desc": "Complete store with dining seats, full European sandwich, burger, pasta & coffee line."},
        {"name": "Master Franchise", "cost": "₹40.0 Lakh", "tag": "City Territory", "space": "District / City Zone", "ideal": "High-net-worth investors & regional distributors", "desc": "Exclusive city rights, sub-franchising revenue share and bulk supply margins."}
    ],
    menu_items=[
        {"title": "Gourmet European Subs", "desc": "6-inch and 12-inch subs with signature house dressings and herb bread.", "highlight": "Highest Volume Seller"},
        {"title": "Grilled Paninis & Toasties", "desc": "Crispy pressed Italian breads with cheese blends and fresh veggies.", "highlight": "High Margin"},
        {"title": "Cheesy Burgers & Pastas", "desc": "Creamy Alfredo & Arrabiata pastas and stacked burgers.", "highlight": "Dinner & Weekend Booster"},
        {"title": "Artisanal Cold Coffees", "desc": "Thick blended frappes, hazelnut coffees and fruit smoothies.", "highlight": "High Margin Beverage"}
    ],
    video_file="assets/videos/baking_craft.mp4",
    video_title="Artisanal Bread & Sub Grilling",
    pnl_data={
        "daily_orders": "130–170 Orders",
        "aov": "₹210",
        "gross_rev": "₹8,82,000 / mo",
        "food_cost": "30% (₹2,64,600)",
        "gross_profit": "70% (₹6,17,400)",
        "expenses": "₹4,41,000 (Rent, Staff, Power)",
        "net_profit": "₹1,76,400 / month"
    }
)

# 4. SOUTH TWIST
st_html = create_brand_page(
    brand_id="south-twist",
    brand_name="South Twist",
    category="South Indian QSR",
    tagline="Authentic South with an Innovative Twist · Chef-Less Operations",
    investment="₹10–20 Lakh",
    payback="10–14 Months",
    margin="40%–45% Net",
    area="100–600 sq.ft",
    outlets="Fastest Growing QSR",
    states="MH, KA & Pan-India",
    hero_img="assets/brands/south_twist_food.png",
    food_img="assets/brands/south_twist_menu.png",
    store_img="assets/brands/south_twist_store.png",
    desc="India's Fastest Growing Authentic South Indian Franchise. Born in Pune. Famous for Ghee Podi Thatte Idlis, crispy Benne Dosas, Mysore Masala, Jamaican & Mix Veg Appe, Peri Peri Idli Fry, and Filter Coffee. Chef-less automated batter supply from own manufacturing unit ensures 0% food wastage and consistent taste.",
    capex_items=[
        {"name": "Franchise Brand Fee", "scope": "5-Year License, Recipe SOPs & Central Batter Supply", "amount": "₹4,00,000"},
        {"name": "Store Interior & Customer Seating", "scope": "Modern South aesthetic, service counter, exhaust chimney, lighting", "amount": "₹6,50,000"},
        {"name": "Specialized Commercial Steamers & Tawas", "scope": "High-capacity Thatte steamers, flat dosa griddles, cold storage", "amount": "₹4,00,000"},
        {"name": "Marketing & Grand Launch", "scope": "Local marketing campaign, influencer opening, launch PR", "amount": "₹1,00,000"},
        {"name": "Initial Stock & Podi Blends", "scope": "Ghee Podi blends, batter packs, filter coffee decoction, packaging", "amount": "₹1,00,000"},
        {"name": "Software, Hardware & Training", "scope": "POS billing terminal, staff uniform & kitchen SOP certification", "amount": "₹1,20,000"}
    ],
    capex_total="₹17,70,000",
    formats=[
        {"name": "Kiosk Model", "cost": "₹10–12L (₹13.3L All-in)", "tag": "Quick Break-Even", "space": "100–200 sq.ft", "ideal": "Metro stations, college clusters & tech parks", "desc": "Ultra-fast Thatte Idli, Podi Button Idli & Filter Coffee express counter."},
        {"name": "Stand-Alone Store", "cost": "₹15–20L (₹17.7L All-in)", "tag": "High Turn-Over", "space": "400–600 sq.ft", "ideal": "High-street retail corridors & residential hubs", "desc": "Full South Indian menu with Thatte Idlis, Benne Dosas, Appes and family seating."},
        {"name": "Master Franchise", "cost": "₹50 Lakh – 1 Crore", "tag": "State Partnership", "space": "City / State Level", "ideal": "Large institutional investors & master operators", "desc": "Exclusive state rights with central kitchen production and sub-franchise royalty sharing."}
    ],
    menu_items=[
        {"title": "Ghee Podi Thatte Idli", "desc": "Large plate-sized fluffy steamed idlis drenched in pure ghee & spicy podi.", "highlight": "Fastest Moving Item"},
        {"title": "Crispy Benne Dosa", "desc": "Davanagere-style butter roasted dosas with potato masala & coconut chutney.", "highlight": "Morning & Evening Pull"},
        {"title": "Jamaican & Mix Veg Appe", "desc": "Crispy appe balls served with tangy podi and signature chutneys.", "highlight": "High Margin Snack"},
        {"title": "Traditional Filter Coffee", "desc": "Authentic degree filter coffee brewed with chicory-roasted beans.", "highlight": "High Volume Repeat"}
    ],
    video_file="assets/videos/cookie_prep.mp4",
    video_title="Fresh Thatte Idli & Automated Batter",
    pnl_data={
        "daily_orders": "180–240 Orders",
        "aov": "₹160",
        "gross_rev": "₹10,08,000 / mo",
        "food_cost": "26% (₹2,62,080)",
        "gross_profit": "74% (₹7,45,920)",
        "expenses": "₹5,20,000 (Rent, Staff, Power)",
        "net_profit": "₹2,25,920 / month"
    }
)

# 5. CAFE CHOCO CRAZE
cc_html = create_brand_page(
    brand_id="cafe-choco-craze",
    brand_name="Cafe Choco Craze",
    category="Chocolate Cafe & Shakes",
    tagline="Pune's Iconic Chocolate Cafe Chain Since 2010 · 80+ Outlets",
    investment="₹8–20 Lakh",
    payback="9–14 Months",
    margin="35%–40% Net",
    area="100–800 sq.ft",
    outlets="80+",
    states="Maharashtra & Pan-India",
    hero_img="assets/brands/cafe-choco-craze.png",
    food_img="assets/brands/cafe-choco-craze.png",
    store_img="assets/brands/cafe-choco-craze.png",
    desc="The iconic Pune chocolate cafe chain. Renowned for Chocolick B (signature Cad-B chocolate thick shake), Chocolick M, Frosips, Exotic Cheese Burst Pizzas, Nutella Chocolate Grills, Garlic Breads, and Thick Cold Coffees. In-house chocolate compound manufacturing in Pune ensures unbeatable gross margins and zero supply chain delays.",
    capex_items=[
        {"name": "Franchise Brand License", "scope": "5-Year Brand Rights & Territorial Exclusivity", "amount": "₹3,50,000"},
        {"name": "Heavy-Duty Commercial Blenders", "scope": "High-torque shake blenders, deep chillers, sandwich grills", "amount": "₹4,20,000"},
        {"name": "Cafe Theme Interior & Wall Branding", "scope": "Signature chocolate decor, counter build, lighting & furniture", "amount": "₹5,00,000"},
        {"name": "Initial Chocolate Compounds & Stock", "scope": "Signature chocolate bases, shake premixes, beans, cups & boxes", "amount": "₹1,80,000"},
        {"name": "POS Software, Licences & Launch", "scope": "Billing terminal, staff SOP certification & local launch ads", "amount": "₹2,00,000"}
    ],
    capex_total="₹16,50,000",
    formats=[
        {"name": "Kiosk Model", "cost": "₹8–12 Lakh", "tag": "Low Investment", "space": "100–250 sq.ft", "ideal": "College gates, youth streets & food courts", "desc": "Compact shake and coffee counter focused on Cad-B, Chocolicks and takeaway snacks."},
        {"name": "Lounge Cafe", "cost": "₹15–20 Lakh", "tag": "Full Menu", "space": "400–800 sq.ft", "ideal": "Prominent high streets & family shopping destinations", "desc": "Complete dining cafe with chocolate shakes, cheese pizzas, garlic breads & desserts."},
        {"name": "Master Franchise", "cost": "₹40–60 Lakh", "tag": "City Partnership", "space": "City / District Rights", "ideal": "Multi-unit investors & regional developers", "desc": "Territorial master rights, franchise fee sharing and localized supply chain hub."}
    ],
    menu_items=[
        {"title": "Chocolick B (Cad-B)", "desc": "The legendary thick chocolate dessert shake that created a cult following in Pune.", "highlight": "Hero Product · 75% Gross Margin"},
        {"title": "Chocolick M & Frosips", "desc": "Rich milk chocolate and fruit-infused thick ice drinks.", "highlight": "High Repeat Rate"},
        {"title": "Nutella Chocolate Grills", "desc": "Crispy grilled sandwiches overflowing with hot melted Nutella chocolate.", "highlight": "Youth Favorite"},
        {"title": "Cheese Burst Pizzas", "desc": "Fresh hand-tossed pizzas loaded with mozzarella and gourmet toppings.", "highlight": "Evening Dining Pull"}
    ],
    video_file="assets/videos/chocolate_craft.mp4",
    video_title="Chocolick B & Chocolate Formulations",
    pnl_data={
        "daily_orders": "140–190 Orders",
        "aov": "₹200",
        "gross_rev": "₹9,80,000 / mo",
        "food_cost": "30% (₹2,94,000)",
        "gross_profit": "70% (₹6,86,000)",
        "expenses": "₹4,80,000 (Rent, Staff, Power)",
        "net_profit": "₹2,06,000 / month"
    }
)

# Write each file
with open("beyond-temptation.html", "w", encoding="utf-8") as f:
    f.write(bt_html)
print("Created beyond-temptation.html")

with open("dunk-burgers.html", "w", encoding="utf-8") as f:
    f.write(db_html)
print("Created dunk-burgers.html")

with open("mr-sandwich.html", "w", encoding="utf-8") as f:
    f.write(ms_html)
print("Created mr-sandwich.html")

with open("south-twist.html", "w", encoding="utf-8") as f:
    f.write(st_html)
print("Created south-twist.html")

with open("cafe-choco-craze.html", "w", encoding="utf-8") as f:
    f.write(cc_html)
print("Created cafe-choco-craze.html")

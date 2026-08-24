# -*- coding: utf-8 -*-
import re

COMPARATOR_SECTION_HTML = """<!-- ============ SIDE-BY-SIDE BRAND COMPARATOR ============ -->
<section class="sec" id="comparator-sec" style="background:var(--paper);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-top rv" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:32px">
      <div class="sec-head wide">
        <p class="eyebrow"><span class="pulse"></span> Decision Matrix</p>
        <h2 style="color:var(--ink)">Side-by-Side Brand Comparison Matrix</h2>
        <p class="sec-note">Compare the economics, Capex requirements, gross margins, and operational models across our 5 flagship food brands.</p>
      </div>
      <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">
        <span style="font-family:var(--font-mono);font-size:12px;color:var(--ink-60);font-weight:600">Select Brands to Compare:</span>
        <div class="comparator-toggles" id="compToggles" style="display:flex;gap:6px;flex-wrap:wrap">
          <button type="button" class="comp-toggle-btn active" data-b="bt" onclick="toggleCompBrand('bt', this)">Beyond Temptation</button>
          <button type="button" class="comp-toggle-btn active" data-b="db" onclick="toggleCompBrand('db', this)">Dunk Burgers</button>
          <button type="button" class="comp-toggle-btn active" data-b="ms" onclick="toggleCompBrand('ms', this)">Mr. Sandwich</button>
          <button type="button" class="comp-toggle-btn" data-b="st" onclick="toggleCompBrand('st', this)">South Twist</button>
          <button type="button" class="comp-toggle-btn" data-b="ccc" onclick="toggleCompBrand('ccc', this)">Cafe Choco Craze</button>
        </div>
      </div>
    </div>

    <!-- Interactive Comparison Matrix Wrap -->
    <div class="comparator-matrix-wrap rv" style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:24px;overflow-x:auto;box-shadow:0 18px 45px -15px rgba(14,18,26,0.08)">
      <table class="comparator-table" id="comparatorTable" style="width:100%;border-collapse:collapse;min-width:760px;font-size:14.5px">
        <thead>
          <tr style="background:rgba(14,18,26,0.03);border-bottom:1.5px solid var(--line)">
            <th style="padding:18px 20px;text-align:left;font-family:var(--font-mono);font-size:12px;text-transform:uppercase;color:var(--ink-60);width:22%">Feature / Parameter</th>
            <th class="col-bt" style="padding:18px 20px;text-align:left;width:26%">
              <div style="font-family:var(--font-editorial);font-size:18px;font-weight:700;color:var(--ink)">Beyond Temptation</div>
              <span class="tag gold" style="margin-top:4px">Dessert &amp; Cafe</span>
            </th>
            <th class="col-db" style="padding:18px 20px;text-align:left;width:26%">
              <div style="font-family:var(--font-editorial);font-size:18px;font-weight:700;color:var(--ink)">Dunk Burgers</div>
              <span class="tag green" style="margin-top:4px">Burgers &amp; QSR</span>
            </th>
            <th class="col-ms" style="padding:18px 20px;text-align:left;width:26%">
              <div style="font-family:var(--font-editorial);font-size:18px;font-weight:700;color:var(--ink)">Mr. Sandwich</div>
              <span class="tag gold" style="margin-top:4px">European Subs</span>
            </th>
            <th class="col-st" style="padding:18px 20px;text-align:left;width:26%;display:none">
              <div style="font-family:var(--font-editorial);font-size:18px;font-weight:700;color:var(--ink)">South Twist</div>
              <span class="tag green" style="margin-top:4px">South Indian QSR</span>
            </th>
            <th class="col-ccc" style="padding:18px 20px;text-align:left;width:26%;display:none">
              <div style="font-family:var(--font-editorial);font-size:18px;font-weight:700;color:var(--ink)">Cafe Choco Craze</div>
              <span class="tag gold" style="margin-top:4px">Chocolate Cafe</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--line)">
            <td style="padding:16px 20px;font-weight:700;color:var(--ink)">Investment (Capex)</td>
            <td class="col-bt" style="padding:16px 20px"><strong style="color:var(--kesar-hot);font-size:16px">&#8377;13 &ndash; 20 Lakh</strong></td>
            <td class="col-db" style="padding:16px 20px"><strong style="color:var(--kesar-hot);font-size:16px">&#8377;15 &ndash; 25 Lakh</strong></td>
            <td class="col-ms" style="padding:16px 20px"><strong style="color:var(--kesar-hot);font-size:16px">&#8377;9 &ndash; 17.5 Lakh</strong></td>
            <td class="col-st" style="padding:16px 20px;display:none"><strong style="color:var(--kesar-hot);font-size:16px">&#8377;10 &ndash; 20 Lakh</strong></td>
            <td class="col-ccc" style="padding:16px 20px;display:none"><strong style="color:var(--kesar-hot);font-size:16px">&#8377;8 &ndash; 20 Lakh</strong></td>
          </tr>
          <tr style="border-bottom:1px solid var(--line)">
            <td style="padding:16px 20px;font-weight:700;color:var(--ink)">Required Floor Space</td>
            <td class="col-bt" style="padding:16px 20px;color:var(--ink)">300 &ndash; 2,000 sqft</td>
            <td class="col-db" style="padding:16px 20px;color:var(--ink)">150 &ndash; 1,000 sqft</td>
            <td class="col-ms" style="padding:16px 20px;color:var(--ink)">80 &ndash; 500 sqft</td>
            <td class="col-st" style="padding:16px 20px;color:var(--ink);display:none">100 &ndash; 800 sqft</td>
            <td class="col-ccc" style="padding:16px 20px;color:var(--ink);display:none">100 &ndash; 600 sqft</td>
          </tr>
          <tr style="border-bottom:1px solid var(--line)">
            <td style="padding:16px 20px;font-weight:700;color:var(--ink)">Net Profit Margin</td>
            <td class="col-bt" style="padding:16px 20px"><span style="color:var(--pista-dark);font-weight:700">&gt; 35% Net</span></td>
            <td class="col-db" style="padding:16px 20px"><span style="color:var(--pista-dark);font-weight:700">&gt; 38% Net</span></td>
            <td class="col-ms" style="padding:16px 20px"><span style="color:var(--pista-dark);font-weight:700">&gt; 41% Net</span></td>
            <td class="col-st" style="padding:16px 20px;display:none"><span style="color:var(--pista-dark);font-weight:700">&gt; 38% Net</span></td>
            <td class="col-ccc" style="padding:16px 20px;display:none"><span style="color:var(--pista-dark);font-weight:700">&gt; 35% Net</span></td>
          </tr>
          <tr style="border-bottom:1px solid var(--line)">
            <td style="padding:16px 20px;font-weight:700;color:var(--ink)">Raw Food Cost %</td>
            <td class="col-bt" style="padding:16px 20px;color:var(--ink)">~32% (Central Factory)</td>
            <td class="col-db" style="padding:16px 20px;color:var(--ink)">~30% (Bulk Supply)</td>
            <td class="col-ms" style="padding:16px 20px;color:var(--ink)">~29% (European Pre-mix)</td>
            <td class="col-st" style="padding:16px 20px;color:var(--ink);display:none">~26% (Automated Batter)</td>
            <td class="col-ccc" style="padding:16px 20px;color:var(--ink);display:none">~31% (Cad-B Blends)</td>
          </tr>
          <tr style="border-bottom:1px solid var(--line)">
            <td style="padding:16px 20px;font-weight:700;color:var(--ink)">Royalty Fee</td>
            <td class="col-bt" style="padding:16px 20px;color:var(--ink)"><strong>0% Flat Royalty</strong></td>
            <td class="col-db" style="padding:16px 20px;color:var(--ink)"><strong>0% Flat Royalty</strong></td>
            <td class="col-ms" style="padding:16px 20px;color:var(--ink)"><strong>0% Flat Royalty</strong></td>
            <td class="col-st" style="padding:16px 20px;color:var(--ink);display:none"><strong>0% Flat Royalty</strong></td>
            <td class="col-ccc" style="padding:16px 20px;color:var(--ink);display:none"><strong>0% Flat Royalty</strong></td>
          </tr>
          <tr style="border-bottom:1px solid var(--line)">
            <td style="padding:16px 20px;font-weight:700;color:var(--ink)">Estimated Payback</td>
            <td class="col-bt" style="padding:16px 20px;color:var(--ink)">12 &ndash; 16 Months</td>
            <td class="col-db" style="padding:16px 20px;color:var(--ink)">12 &ndash; 15 Months</td>
            <td class="col-ms" style="padding:16px 20px;color:var(--ink)">9 &ndash; 12 Months</td>
            <td class="col-st" style="padding:16px 20px;color:var(--ink);display:none">10 &ndash; 13 Months</td>
            <td class="col-ccc" style="padding:16px 20px;color:var(--ink);display:none">10 &ndash; 14 Months</td>
          </tr>
          <tr style="border-bottom:1px solid var(--line)">
            <td style="padding:16px 20px;font-weight:700;color:var(--ink)">Operational Model</td>
            <td class="col-bt" style="padding:16px 20px;color:var(--ink)">FOFO &amp; FOCO Models</td>
            <td class="col-db" style="padding:16px 20px;color:var(--ink)">FOFO (You own &amp; operate)</td>
            <td class="col-ms" style="padding:16px 20px;color:var(--ink)">FOFO (200+ Outlets)</td>
            <td class="col-st" style="padding:16px 20px;color:var(--ink);display:none">FOFO &amp; FOCO Available</td>
            <td class="col-ccc" style="padding:16px 20px;color:var(--ink);display:none">FOFO (80+ Outlets)</td>
          </tr>
          <tr style="border-bottom:1.5px solid var(--line)">
            <td style="padding:16px 20px;font-weight:700;color:var(--ink)">Central Supply &amp; SOP</td>
            <td class="col-bt" style="padding:16px 20px;color:var(--ink-60);font-size:13.5px">&gt;85% factory pre-mix, Cad-Bee bases</td>
            <td class="col-db" style="padding:16px 20px;color:var(--ink-60);font-size:13.5px">Dip-In sauces, patties &amp; loaded fries</td>
            <td class="col-ms" style="padding:16px 20px;color:var(--ink-60);font-size:13.5px">Artisanal European dough &amp; paninis</td>
            <td class="col-st" style="padding:16px 20px;color:var(--ink-60);font-size:13.5px;display:none">Pre-fermented Thatte Idli batter</td>
            <td class="col-ccc" style="padding:16px 20px;color:var(--ink-60);font-size:13.5px;display:none">Chocolick B bases &amp; syrups</td>
          </tr>
          <tr style="background:rgba(14,18,26,0.02)">
            <td style="padding:20px;font-weight:700;color:var(--ink)">Dedicated Profile</td>
            <td class="col-bt" style="padding:20px">
              <a href="beyond-temptation.html" class="btn btn--kesar btn--sm" style="width:100%;font-size:13px;padding:10px 14px">View Beyond Temptation &rarr;</a>
            </td>
            <td class="col-db" style="padding:20px">
              <a href="dunk-burgers.html" class="btn btn--kesar btn--sm" style="width:100%;font-size:13px;padding:10px 14px">View Dunk Burgers &rarr;</a>
            </td>
            <td class="col-ms" style="padding:20px">
              <a href="mr-sandwich.html" class="btn btn--kesar btn--sm" style="width:100%;font-size:13px;padding:10px 14px">View Mr. Sandwich &rarr;</a>
            </td>
            <td class="col-st" style="padding:20px;display:none">
              <a href="south-twist.html" class="btn btn--kesar btn--sm" style="width:100%;font-size:13px;padding:10px 14px">View South Twist &rarr;</a>
            </td>
            <td class="col-ccc" style="padding:20px;display:none">
              <a href="cafe-choco-craze.html" class="btn btn--kesar btn--sm" style="width:100%;font-size:13px;padding:10px 14px">View Cafe Choco Craze &rarr;</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>"""

COMPARATOR_SCRIPT = """
// Interactive Brand Comparator Toggle Functionality
function toggleCompBrand(brandCode, btn) {
  const isCurrentlyActive = btn.classList.contains('active');
  const activeBtns = document.querySelectorAll('.comp-toggle-btn.active');
  
  if (isCurrentlyActive && activeBtns.length <= 2) {
    alert("Please keep at least 2 brands selected to compare!");
    return;
  }

  btn.classList.toggle('active');
  const show = btn.classList.contains('active');
  
  const cells = document.querySelectorAll('.col-' + brandCode);
  cells.forEach(cell => {
    cell.style.display = show ? '' : 'none';
  });
}
"""

COMPARATOR_STYLE = """
/* Brand Comparator Styles */
.comp-toggle-btn {
  background: var(--paper-card);
  border: 1.5px solid var(--line);
  color: var(--ink);
  padding: 8px 14px;
  border-radius: 999px;
  font-family: var(--font-mono);
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.comp-toggle-btn:hover {
  border-color: var(--kesar);
  transform: translateY(-1px);
}
.comp-toggle-btn.active {
  background: var(--kesar);
  color: var(--ink);
  font-weight: 700;
  border-color: var(--kesar);
  box-shadow: 0 4px 12px rgba(255,176,32,0.3);
}
"""

# 1. Update franchises.html
with open("franchises.html", "r", encoding="utf-8") as f:
    f_html = f.read()

if "<!-- ============ SIDE-BY-SIDE BRAND COMPARATOR ============ -->" not in f_html:
    # Insert right before footer
    f_html = f_html.replace('<!-- ============ FOOTER ============ -->', f"{COMPARATOR_SECTION_HTML}\n\n<!-- ============ FOOTER ============ -->")
    # Add script
    f_html = f_html.replace('</script>\n</body>', f"{COMPARATOR_SCRIPT}\n</script>\n</body>")
    # Add style
    f_html = f_html.replace('</style>', f"{COMPARATOR_STYLE}\n</style>")

with open("franchises.html", "w", encoding="utf-8") as f:
    f.write(f_html)

print("Added Side-by-Side Brand Comparator to franchises.html")

# 2. Update index.html and franq-franchise-website.html
with open("index.html", "r", encoding="utf-8") as f:
    idx_html = f.read()

if "<!-- ============ SIDE-BY-SIDE BRAND COMPARATOR ============ -->" not in idx_html:
    # Insert right after the brands marketplace or after #calculator
    idx_html = idx_html.replace('<!-- ============ CITY AVAILABILITY CHECKER ============ -->', f"{COMPARATOR_SECTION_HTML}\n\n<!-- ============ CITY AVAILABILITY CHECKER ============ -->")
    # Add script
    idx_html = idx_html.replace('</script>\n</body>', f"{COMPARATOR_SCRIPT}\n</script>\n</body>")
    # Add style
    idx_html = idx_html.replace('</style>', f"{COMPARATOR_STYLE}\n</style>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(idx_html)

print("Added Side-by-Side Brand Comparator to index.html and franq-franchise-website.html")

# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS for both Format buttons and Brand buttons
CALC_CSS_OLD = """.calc-formats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
@media(max-width:540px){.calc-formats{grid-template-columns:repeat(2,1fr)}}
.fmt-btn{
  background:rgba(248,250,252,.08);border:1px solid var(--line-dark);
  color:rgba(248,250,252,.85);padding:10px 8px;border-radius:10px;
  font-family:var(--mono);font-size:11.5px;cursor:pointer;text-align:center;
  transition:all .2s;
}
.fmt-btn.active{background:var(--kesar);color:var(--jamun-deep);border-color:var(--kesar);font-weight:700}"""

CALC_CSS_NEW = """.calc-formats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
@media(max-width:600px){.calc-formats{grid-template-columns:repeat(2,1fr)}}
.calc-brand-pills{display:flex;gap:6px;flex-wrap:wrap;margin-top:2px}
.fmt-btn{
  background:rgba(248,250,252,.08);border:1px solid var(--line-dark);
  color:rgba(248,250,252,.85);padding:10px 8px;border-radius:10px;
  font-family:var(--mono);font-size:11.5px;cursor:pointer;text-align:center;
  transition:all .2s;
}
.fmt-btn.active{background:var(--kesar);color:var(--jamun-deep);border-color:var(--kesar);font-weight:700;box-shadow:0 0 12px rgba(255,176,32,0.35)}
.brand-pill-btn{
  background:rgba(248,250,252,.06);border:1px solid var(--line-dark);
  color:rgba(248,250,252,.8);padding:6px 12px;border-radius:999px;
  font-family:var(--mono);font-size:11px;cursor:pointer;text-align:center;
  transition:all .2s;
}
.brand-pill-btn:hover{border-color:var(--kesar);color:var(--malai)}
.brand-pill-btn.active{background:var(--kesar);color:var(--jamun-deep);border-color:var(--kesar);font-weight:700}"""

html = html.replace(CALC_CSS_OLD, CALC_CSS_NEW)

# 2. Update Calculator Section HTML in index.html
OLD_CALC_SECTION = """<!-- ============ INTERACTIVE ROI CALCULATOR ============ -->
<section class="wrap" id="calculator">
  <div class="calc-section rv on-dark">
    <div class="sec-head on-dark" style="margin-bottom:28px">
      <p class="eyebrow on-dark">Unit Economics Simulator</p>
      <h2 style="color:var(--malai)">Calculate your monthly profit &amp; payback.</h2>
      <p class="sec-note on-dark">Adjust format, investment, and customer volume to see realistic gross margin, operational costs, and estimated breakeven period.</p>
    </div>

    <div class="calc-grid">
      <!-- Sliders / Controls -->
      <div class="calc-card">
        <div class="calc-group">
          <label style="font-family:var(--mono);font-size:11.5px;color:rgba(248,250,252,.7);text-transform:uppercase">1. Outlet Format</label>
          <div class="calc-formats">
            <button class="fmt-btn active" data-fmt="kiosk" onclick="setCalcFormat('kiosk')">Kiosk (&#8377;8L)</button>
            <button class="fmt-btn" data-fmt="qsr" onclick="setCalcFormat('qsr')">QSR (&#8377;16L)</button>
            <button class="fmt-btn" data-fmt="cloud" onclick="setCalcFormat('cloud')">Cloud (&#8377;10L)</button>
            <button class="fmt-btn" data-fmt="dine" onclick="setCalcFormat('dine')">Dine-in (&#8377;50L)</button>
          </div>
        </div>

        <div class="calc-group">
          <div class="calc-label-row">
            <span>Total Capital Investment</span>
            <span class="calc-val-badge" id="valInvestment">&#8377;8 Lakh</span>
          </div>
          <input type="range" class="calc-slider" id="sliderInvestment" min="6" max="70" step="1" value="8" oninput="updateCalculator()" />
        </div>

        <div class="calc-group">
          <div class="calc-label-row">
            <span>Daily Customer Orders</span>
            <span class="calc-val-badge" id="valOrders">160 bills / day</span>
          </div>
          <input type="range" class="calc-slider" id="sliderOrders" min="40" max="450" step="5" value="160" oninput="updateCalculator()" />
        </div>

        <div class="calc-group">
          <div class="calc-label-row">
            <span>Average Order Value (AOV)</span>
            <span class="calc-val-badge" id="valAOV">&#8377;120 / bill</span>
          </div>
          <input type="range" class="calc-slider" id="sliderAOV" min="50" max="650" step="10" value="120" oninput="updateCalculator()" />
        </div>
      </div>

      <!-- Live Calculation Results -->
      <div class="calc-results-board">
        <div class="calc-metric-row">
          <div class="calc-metric-item">
            <small>Est. Monthly Revenue</small>
            <strong id="resRevenue">&#8377;5,76,000</strong>
          </div>
          <div class="calc-metric-item">
            <small>Raw Food Cost (~34%)</small>
            <strong id="resFoodCost" style="color:rgba(248,250,252,.85)">&#8377;1,95,840</strong>
          </div>
        </div>

        <div class="calc-metric-row">
          <div class="calc-metric-item">
            <small>Staff &amp; Rent Overhead</small>
            <strong id="resOpex" style="color:rgba(248,250,252,.85)">&#8377;1,45,000</strong>
          </div>
          <div class="calc-metric-item">
            <small>Brand Royalty (5-8%)</small>
            <strong id="resRoyalty" style="color:rgba(248,250,252,.85)">&#8377;34,560</strong>
          </div>
        </div>

        <div class="calc-highlight-box">
          <div>
            <small>Est. Net Profit / Month</small>
            <b id="resNetProfit">&#8377;2,00,600</b>
          </div>
          <div style="text-align:right">
            <small>Est. Payback Period</small>
            <b id="resPayback" style="color:var(--kesar)">4.0 Months</b>
          </div>
        </div>

        <button class="btn btn--kesar" style="width:100%" onclick="applyForCalculatedBudget()">Apply For Brands in This Bracket &rarr;</button>
      </div>
    </div>
  </div>
</section>"""

NEW_CALC_SECTION = """<!-- ============ INTERACTIVE FORMAT & BRAND ROI CALCULATOR ============ -->
<section class="wrap" id="calculator">
  <div class="calc-section rv on-dark">
    <div class="sec-head on-dark" style="margin-bottom:28px">
      <p class="eyebrow on-dark"><span class="pulse"></span> Unit Economics Simulator</p>
      <h2 style="color:var(--malai)">Calculate Profit &amp; Payback by Format &amp; Brand.</h2>
      <p class="sec-note on-dark">Select an outlet format (Kiosk, QSR, Cloud Kitchen, Dine-in) and optionally apply audited brand data from our 5 flagship food brands.</p>
    </div>

    <div class="calc-grid">
      <!-- Sliders / Controls -->
      <div class="calc-card">
        <!-- 1. Format Selector -->
        <div class="calc-group">
          <label style="font-family:var(--mono);font-size:11.5px;color:rgba(248,250,252,.75);text-transform:uppercase;letter-spacing:0.06em">1. Select Outlet Format</label>
          <div class="calc-formats">
            <button type="button" class="fmt-btn active" data-fmt="kiosk" onclick="setCalcFormat('kiosk')">Kiosk (&#8377;8L)</button>
            <button type="button" class="fmt-btn" data-fmt="qsr" onclick="setCalcFormat('qsr')">QSR (&#8377;16L)</button>
            <button type="button" class="fmt-btn" data-fmt="cloud" onclick="setCalcFormat('cloud')">Cloud Kitchen (&#8377;10L)</button>
            <button type="button" class="fmt-btn" data-fmt="dine" onclick="setCalcFormat('dine')">Dine-in (&#8377;50L)</button>
          </div>
        </div>

        <!-- 2. Brand Presets -->
        <div class="calc-group" style="padding-top:4px">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <label style="font-family:var(--mono);font-size:11.5px;color:rgba(248,250,252,.75);text-transform:uppercase;letter-spacing:0.06em">2. Calibrate by Brand Model (Optional)</label>
            <span id="calcBrandBadge" style="font-family:var(--font-mono);font-size:11px;color:var(--kesar);font-weight:700">General F&amp;B</span>
          </div>
          <div class="calc-brand-pills">
            <button type="button" class="brand-pill-btn active" data-brand="general" onclick="setCalcBrand('general')">Standard F&amp;B</button>
            <button type="button" class="brand-pill-btn" data-brand="beyond-temptation" onclick="setCalcBrand('beyond-temptation')">Beyond Temptation</button>
            <button type="button" class="brand-pill-btn" data-brand="dunk-burgers" onclick="setCalcBrand('dunk-burgers')">Dunk Burgers</button>
            <button type="button" class="brand-pill-btn" data-brand="mr-sandwich" onclick="setCalcBrand('mr-sandwich')">Mr. Sandwich</button>
            <button type="button" class="brand-pill-btn" data-brand="south-twist" onclick="setCalcBrand('south-twist')">South Twist</button>
            <button type="button" class="brand-pill-btn" data-brand="cafe-choco-craze" onclick="setCalcBrand('cafe-choco-craze')">Cafe Choco Craze</button>
          </div>
        </div>

        <!-- 3. Sliders -->
        <div class="calc-group" style="margin-top:6px">
          <div class="calc-label-row">
            <span>Total Capital Investment</span>
            <span class="calc-val-badge" id="valInvestment">&#8377;8 Lakh</span>
          </div>
          <input type="range" class="calc-slider" id="sliderInvestment" min="6" max="75" step="1" value="8" oninput="updateCalculator()" />
        </div>

        <div class="calc-group">
          <div class="calc-label-row">
            <span>Daily Customer Orders</span>
            <span class="calc-val-badge" id="valOrders">160 bills / day</span>
          </div>
          <input type="range" class="calc-slider" id="sliderOrders" min="40" max="450" step="5" value="160" oninput="updateCalculator()" />
        </div>

        <div class="calc-group">
          <div class="calc-label-row">
            <span>Average Order Value (AOV)</span>
            <span class="calc-val-badge" id="valAOV">&#8377;120 / bill</span>
          </div>
          <input type="range" class="calc-slider" id="sliderAOV" min="50" max="650" step="10" value="120" oninput="updateCalculator()" />
        </div>
      </div>

      <!-- Live Calculation Results -->
      <div class="calc-results-board">
        <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.12);padding-bottom:12px">
          <div>
            <small style="font-family:var(--font-mono);font-size:11px;color:rgba(255,255,255,0.7);text-transform:uppercase">Active Simulator Model</small>
            <strong id="resModelTitle" style="display:block;font-size:16px;color:var(--malai)">Kiosk Format &middot; Standard F&amp;B</strong>
          </div>
          <span id="resTagMargin" class="tag gold">Audited Unit Economics</span>
        </div>

        <div class="calc-metric-row">
          <div class="calc-metric-item">
            <small>Est. Monthly Revenue</small>
            <strong id="resRevenue">&#8377;5,76,000</strong>
          </div>
          <div class="calc-metric-item">
            <small id="labelFoodCost">Raw Material Cost (~34%)</small>
            <strong id="resFoodCost" style="color:rgba(248,250,252,.85)">&#8377;1,95,840</strong>
          </div>
        </div>

        <div class="calc-metric-row">
          <div class="calc-metric-item">
            <small>Staff, Rent &amp; Overhead</small>
            <strong id="resOpex" style="color:rgba(248,250,252,.85)">&#8377;1,45,000</strong>
          </div>
          <div class="calc-metric-item">
            <small>Brand Royalty</small>
            <strong id="resRoyalty" style="color:var(--pista)">&#8377;0 (0% Royalty)</strong>
          </div>
        </div>

        <div class="calc-highlight-box">
          <div>
            <small>Est. Net Profit / Month</small>
            <b id="resNetProfit">&#8377;2,35,160</b>
          </div>
          <div style="text-align:right">
            <small>Est. Payback Period</small>
            <b id="resPayback" style="color:var(--kesar)">3.4 Months</b>
          </div>
        </div>

        <button class="btn btn--kesar" id="calcApplyBtn" style="width:100%" onclick="applyForCalculatedBudget()">Apply For This Franchise Opportunity &rarr;</button>
      </div>
    </div>
  </div>
</section>"""

html = html.replace(OLD_CALC_SECTION, NEW_CALC_SECTION)

# 3. Update JavaScript Engine in index.html
OLD_CALC_JS = """const formatConfigs = {
  kiosk: { baseInvest: 8, baseOrders: 160, baseAov: 120, foodCostPct: 0.34, opex: 145000, royaltyPct: 0.06 },
  qsr: { baseInvest: 16, baseOrders: 240, baseAov: 190, foodCostPct: 0.35, opex: 260000, royaltyPct: 0.05 },
  cloud: { baseInvest: 10, baseOrders: 180, baseAov: 260, foodCostPct: 0.38, opex: 160000, royaltyPct: 0.06 },
  dine: { baseInvest: 50, baseOrders: 130, baseAov: 680, foodCostPct: 0.36, opex: 650000, royaltyPct: 0.07 }
};

function setCalcFormat(fmt){
  calcFormat = fmt;
  document.querySelectorAll('.fmt-btn').forEach(b => b.classList.toggle('active', b.getAttribute('data-fmt') === fmt));
  const cfg = formatConfigs[fmt];
  document.getElementById('sliderInvestment').value = cfg.baseInvest;
  document.getElementById('sliderOrders').value = cfg.baseOrders;
  document.getElementById('sliderAOV').value = cfg.baseAov;
  updateCalculator();
}

function updateCalculator(){
  const investLakh = +document.getElementById('sliderInvestment').value;
  const dailyOrders = +document.getElementById('sliderOrders').value;
  const aov = +document.getElementById('sliderAOV').value;

  document.getElementById('valInvestment').textContent = `₹${investLakh} Lakh`;
  document.getElementById('valOrders').textContent = `${dailyOrders} bills / day`;
  document.getElementById('valAOV').textContent = `₹${aov} / bill`;

  const monthlyTurnover = dailyOrders * aov * 30;
  const cfg = formatConfigs[calcFormat] || formatConfigs.kiosk;

  const foodCost = monthlyTurnover * cfg.foodCostPct;
  const royalty = monthlyTurnover * cfg.royaltyPct;
  const opexScaled = cfg.opex * (1 + (investLakh - cfg.baseInvest) * 0.02);
  const netProfit = Math.max(monthlyTurnover - foodCost - royalty - opexScaled, 15000);

  const totalCapInr = investLakh * 100000;
  const paybackMonths = (totalCapInr / netProfit).toFixed(1);

  document.getElementById('resRevenue').textContent = '₹' + Math.round(monthlyTurnover).toLocaleString('en-IN');
  document.getElementById('resFoodCost').textContent = '₹' + Math.round(foodCost).toLocaleString('en-IN');
  document.getElementById('resOpex').textContent = '₹' + Math.round(opexScaled).toLocaleString('en-IN');
  document.getElementById('resRoyalty').textContent = '₹' + Math.round(royalty).toLocaleString('en-IN');
  document.getElementById('resNetProfit').textContent = '₹' + Math.round(netProfit).toLocaleString('en-IN');
  document.getElementById('resPayback').textContent = `${paybackMonths} Months`;
}
updateCalculator();

function applyForCalculatedBudget(){
  const investLakh = +document.getElementById('sliderInvestment').value;
  let bracket = '₹6–15 lakh';
  if (investLakh > 60) bracket = '₹60 lakh and above';
  else if (investLakh > 30) bracket = '₹30–60 lakh';
  else if (investLakh > 15) bracket = '₹15–30 lakh';

  const budgetDropdown = document.getElementById('fbudget');
  if (budgetDropdown) budgetDropdown.value = bracket;

  const applySection = document.getElementById('apply');
  if (applySection) applySection.scrollIntoView({ behavior: 'smooth' });
}"""

NEW_CALC_JS = """const formatConfigs = {
  kiosk: { name: 'Kiosk Format', baseInvest: 8, baseOrders: 160, baseAov: 120, opex: 120000 },
  qsr: { name: 'QSR Format', baseInvest: 16, baseOrders: 220, baseAov: 180, opex: 180000 },
  cloud: { name: 'Cloud Kitchen', baseInvest: 10, baseOrders: 170, baseAov: 240, opex: 130000 },
  dine: { name: 'Dine-in Format', baseInvest: 50, baseOrders: 140, baseAov: 480, opex: 380000 }
};

const brandProfiles = {
  general: {
    name: 'Standard F&B',
    foodCostPct: 0.34,
    royaltyPct: 0.05,
    tagline: 'Standard Industry Benchmark',
    badge: 'Industry Average'
  },
  'beyond-temptation': {
    name: 'Beyond Temptation',
    foodCostPct: 0.32,
    royaltyPct: 0.00,
    aovBoost: 190,
    investDefault: 15,
    tagline: 'Cad-Bee Chocolate Shakes & Cafe',
    badge: '32% Food Cost · 0% Royalty'
  },
  'dunk-burgers': {
    name: 'Dunk Burgers',
    foodCostPct: 0.30,
    royaltyPct: 0.00,
    aovBoost: 220,
    investDefault: 18,
    tagline: 'Dip-In Burgers & Loaded Sides',
    badge: '30% Food Cost · 0% Royalty'
  },
  'mr-sandwich': {
    name: 'Mr. Sandwich',
    foodCostPct: 0.29,
    royaltyPct: 0.00,
    aovBoost: 160,
    investDefault: 12,
    tagline: 'European Subs & Grills (200+ Outlets)',
    badge: '29% Food Cost · 41% Margin'
  },
  'south-twist': {
    name: 'South Twist',
    foodCostPct: 0.26,
    royaltyPct: 0.00,
    aovBoost: 130,
    investDefault: 14,
    tagline: 'Thatte Idli & Benne Dosa QSR',
    badge: '26% Food Cost · Automated'
  },
  'cafe-choco-craze': {
    name: 'Cafe Choco Craze',
    foodCostPct: 0.31,
    royaltyPct: 0.00,
    aovBoost: 175,
    investDefault: 13,
    tagline: 'Chocolick B Cad-B & Shakes',
    badge: '31% Food Cost · 80+ Outlets'
  }
};

let currentFormat = 'kiosk';
let currentBrand = 'general';

function setCalcFormat(fmt){
  currentFormat = fmt;
  document.querySelectorAll('.fmt-btn').forEach(b => b.classList.toggle('active', b.getAttribute('data-fmt') === fmt));
  
  const fCfg = formatConfigs[fmt];
  document.getElementById('sliderInvestment').value = fCfg.baseInvest;
  document.getElementById('sliderOrders').value = fCfg.baseOrders;
  
  if (currentBrand === 'general') {
    document.getElementById('sliderAOV').value = fCfg.baseAov;
  }
  updateCalculator();
}

function setCalcBrand(bKey){
  currentBrand = bKey;
  document.querySelectorAll('.brand-pill-btn').forEach(b => b.classList.toggle('active', b.getAttribute('data-brand') === bKey));
  
  const bData = brandProfiles[bKey];
  document.getElementById('calcBrandBadge').textContent = bData.name;
  
  if (bKey !== 'general') {
    if (bData.investDefault) document.getElementById('sliderInvestment').value = bData.investDefault;
    if (bData.aovBoost) document.getElementById('sliderAOV').value = bData.aovBoost;
  }
  updateCalculator();
}

function updateCalculator(){
  const fCfg = formatConfigs[currentFormat] || formatConfigs.kiosk;
  const bData = brandProfiles[currentBrand] || brandProfiles.general;

  const investLakh = +document.getElementById('sliderInvestment').value;
  const dailyOrders = +document.getElementById('sliderOrders').value;
  const aov = +document.getElementById('sliderAOV').value;

  document.getElementById('valInvestment').textContent = `₹${investLakh} Lakh`;
  document.getElementById('valOrders').textContent = `${dailyOrders} bills / day`;
  document.getElementById('valAOV').textContent = `₹${aov} / bill`;

  // UI labels
  document.getElementById('resModelTitle').textContent = `${fCfg.name} · ${bData.name}`;
  document.getElementById('resTagMargin').textContent = bData.badge;
  document.getElementById('labelFoodCost').textContent = `Raw Material Cost (${Math.round(bData.foodCostPct * 100)}%)`;

  const monthlyTurnover = dailyOrders * aov * 30;
  const foodCost = monthlyTurnover * bData.foodCostPct;
  const royalty = monthlyTurnover * bData.royaltyPct;
  const opexScaled = fCfg.opex * (1 + (investLakh - fCfg.baseInvest) * 0.025);
  const netProfit = Math.max(monthlyTurnover - foodCost - royalty - opexScaled, 20000);

  const totalCapInr = investLakh * 100000;
  const paybackMonths = (totalCapInr / netProfit).toFixed(1);

  document.getElementById('resRevenue').textContent = '₹' + Math.round(monthlyTurnover).toLocaleString('en-IN');
  document.getElementById('resFoodCost').textContent = '₹' + Math.round(foodCost).toLocaleString('en-IN');
  document.getElementById('resOpex').textContent = '₹' + Math.round(opexScaled).toLocaleString('en-IN');
  
  if (bData.royaltyPct === 0) {
    document.getElementById('resRoyalty').innerHTML = '<span style="color:var(--pista)">₹0 (0% Royalty)</span>';
  } else {
    document.getElementById('resRoyalty').textContent = '₹' + Math.round(royalty).toLocaleString('en-IN');
  }

  document.getElementById('resNetProfit').textContent = '₹' + Math.round(netProfit).toLocaleString('en-IN');
  document.getElementById('resPayback').textContent = `${paybackMonths} Months`;

  const applyBtn = document.getElementById('calcApplyBtn');
  if (applyBtn) {
    if (currentBrand !== 'general') {
      applyBtn.innerHTML = `Apply For ${bData.name} Franchise &rarr;`;
    } else {
      applyBtn.innerHTML = `Apply For ${fCfg.name} Franchise &rarr;`;
    }
  }
}

function applyForCalculatedBudget(){
  const investLakh = +document.getElementById('sliderInvestment').value;
  const bData = brandProfiles[currentBrand] || brandProfiles.general;

  let bracket = '₹6–15 lakh';
  if (investLakh > 60) bracket = '₹60 lakh and above';
  else if (investLakh > 30) bracket = '₹30–60 lakh';
  else if (investLakh > 15) bracket = '₹15–30 lakh';

  const budgetDropdown = document.getElementById('fbudget');
  if (budgetDropdown) budgetDropdown.value = bracket;

  const brandInput = document.getElementById('brandPrefill');
  if (brandInput && currentBrand !== 'general') {
    brandInput.value = bData.name;
  }

  const applySection = document.getElementById('apply');
  if (applySection) applySection.scrollIntoView({ behavior: 'smooth' });
}

// Initial calculation kickoff
if (document.getElementById('sliderInvestment')) {
  updateCalculator();
}"""

html = html.replace(OLD_CALC_JS, NEW_CALC_JS)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Added dual Format + Brand Presets to ROI Calculator!")

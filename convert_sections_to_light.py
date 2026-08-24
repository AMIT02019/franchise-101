# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. UPDATE .brackets CSS to Light Theme
OLD_BRACKETS_CSS = """.brackets{background:var(--jamun);color:var(--malai);border-radius:clamp(24px,4vw,44px)}
.rail-outer{height:230vh;position:relative}
.rail-sticky{position:sticky;top:0;height:100vh;padding-top:64px;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.rail-head{padding-inline:var(--gutter);margin-bottom:clamp(24px,3vw,36px)}
.rail-head .sec-top{margin-bottom:0}
.rail{display:flex;gap:18px;padding-inline:var(--gutter);will-change:transform}
.slab{
  flex:none;width:min(390px,78vw);border-radius:var(--r);padding:18px;
  background:linear-gradient(170deg,rgba(248,250,252,.1),rgba(248,250,252,.03));
  border:1px solid var(--line-dark);display:flex;flex-direction:column;gap:14px;
}
.slab .shot{aspect-ratio:16/8}
.slab-amt{font-family:var(--display);font-weight:800;font-size:clamp(30px,4vw,46px);letter-spacing:-.04em;line-height:.9;color:var(--kesar);padding-inline:6px}
.slab p{color:rgba(248,250,252,.75);font-size:15px;padding-inline:6px}
.slab ul{list-style:none;margin:auto 0 0;padding:0 6px;display:flex;flex-direction:column;gap:8px}
.slab li{display:flex;gap:10px;align-items:flex-start;font-size:14.5px;color:rgba(248,250,252,.86)}
.slab li::before{content:"";width:7px;height:7px;border-radius:2px;background:var(--pista);margin-top:7px;flex:none}
.progress{height:3px;background:var(--line-dark);margin:clamp(24px,3vw,36px) var(--gutter) 0;border-radius:99px;overflow:hidden}
.progress i{display:block;height:100%;width:0;background:var(--kesar-hot);border-radius:99px}"""

NEW_BRACKETS_CSS = """.brackets{
  background:var(--paper);color:var(--ink);
  border-top:1px solid var(--line);border-bottom:1px solid var(--line);
}
.rail-outer{height:230vh;position:relative}
.rail-sticky{position:sticky;top:0;height:100vh;padding-top:64px;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.rail-head{padding-inline:var(--gutter);margin-bottom:clamp(24px,3vw,36px)}
.rail-head .sec-top{margin-bottom:0}
.rail{display:flex;gap:20px;padding-inline:var(--gutter);will-change:transform}
.slab{
  flex:none;width:min(390px,78vw);border-radius:var(--r);padding:22px;
  background:#FFFFFF;
  border:1.5px solid var(--line);
  box-shadow:0 12px 32px -8px rgba(14,18,26,0.07);
  display:flex;flex-direction:column;gap:14px;
  transition:transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}
.slab:hover{
  transform:translateY(-4px);
  box-shadow:0 20px 40px -12px rgba(14,18,26,0.12);
  border-color:rgba(255,176,32,0.4);
}
.slab .shot{aspect-ratio:16/8;border-radius:12px;overflow:hidden}
.slab-amt{font-family:var(--display);font-weight:800;font-size:clamp(30px,4vw,46px);letter-spacing:-.04em;line-height:.9;color:var(--kesar);padding-inline:6px}
.slab p{color:var(--ink-60);font-size:15px;line-height:1.5;padding-inline:6px}
.slab ul{list-style:none;margin:auto 0 0;padding:0 6px;display:flex;flex-direction:column;gap:10px}
.slab li{display:flex;gap:10px;align-items:flex-start;font-size:14.5px;color:var(--ink);line-height:1.4}
.slab li::before{content:"";width:7px;height:7px;border-radius:2px;background:var(--pista);margin-top:6px;flex:none}
.progress{height:4px;background:rgba(14,18,26,0.08);margin:clamp(24px,3vw,36px) var(--gutter) 0;border-radius:99px;overflow:hidden}
.progress i{display:block;height:100%;width:0;background:var(--kesar);border-radius:99px}"""

html = html.replace(OLD_BRACKETS_CSS, NEW_BRACKETS_CSS)

# 2. Update HTML of #budget section
OLD_BUDGET_HTML = """<!-- ============ BUDGET RAIL ============ -->
<section class="brackets" id="budget">
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

NEW_BUDGET_HTML = """<!-- ============ BUDGET RAIL (LIGHT THEME) ============ -->
<section class="brackets" id="budget">
  <div class="rail-outer" id="railOuter">
    <div class="rail-sticky">
      <div class="rail-head">
        <div class="sec-top" style="margin-bottom:0">
          <div class="sec-head wide">
            <p class="eyebrow">By budget</p>
            <h2 style="color:var(--ink)">What &#8377;6 lakh buys, and what &#8377;60 lakh does.</h2>
          </div>
          <p class="sec-note">Pick the bracket you can fund without borrowing against the house. The format follows the capital, not the other way round.</p>
        </div>
      </div>"""

html = html.replace(OLD_BUDGET_HTML, NEW_BUDGET_HTML)

# 3. Update #kitchen-craft to Light Theme
OLD_KITCHEN_CRAFT = """<!-- ============ BEHIND THE COUNTER (VIDEO SHOWCASE) ============ -->
<section class="sec on-dark" id="kitchen-craft" style="background:var(--jamun-deep);position:relative;overflow:hidden">
  <div class="wrap">
    <div class="sec-top rv" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:40px">
      <div class="sec-head wide">
        <p class="eyebrow on-dark"><span class="pulse"></span> Standardized Operations</p>
        <h2 style="color:var(--malai)">Behind The Counter: Central Kitchen &amp; Supply SOPs</h2>
        <p class="sec-note on-dark">Every flagship brand on Franchise 101 eliminates skilled-chef dependency with automated premixes, central manufacturing, and fast SOPs.</p>
      </div>
      <a class="btn btn--kesar btn--sm" href="#apply">Visit A Live Outlet &rarr;</a>
    </div>

    <!-- 2x2 Balanced Split-Card Grid -->
    <div class="craft-grid-2x2 rv" style="display:grid;grid-template-columns:repeat(2, 1fr);gap:24px">
      
      <!-- Card 1: Beyond Temptation & Cafe Choco Craze -->
      <div class="craft-card" style="background:rgba(255,243,222,0.05);border:1px solid rgba(255,243,222,0.14);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 18px 40px -15px rgba(0,0,0,0.5);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
          </video>
          <span class="tag gold" style="position:absolute;top:12px;left:12px;z-index:2">Chocolate &amp; Cafe Craft</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--malai)">Proprietary Chocolate Bases</h4>
            <p style="font-size:13px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Over 85% of Cad-Bee bases &amp; dessert pre-mixes are manufactured centrally in Pune with 0% kitchen waste.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--pista);font-weight:700;margin-bottom:8px">&bull; Beyond Temptation &middot; Cafe Choco Craze</div>
            <a href="beyond-temptation.html" style="font-size:13px;color:var(--kesar);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 2: Mr. Sandwich -->
      <div class="craft-card" style="background:rgba(255,243,222,0.05);border:1px solid rgba(255,243,222,0.14);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 18px 40px -15px rgba(0,0,0,0.5);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/baking_craft.mp4" type="video/mp4">
          </video>
          <span class="tag green" style="position:absolute;top:12px;left:12px;z-index:2">Chef-Less Baking</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--malai)">Standardized Bread &amp; Subs</h4>
            <p style="font-size:13px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">European subs, paninis, and dough recipes certified for 0% chef skill dependency and fast 4-min dispatch.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--kesar);font-weight:700;margin-bottom:8px">&bull; Mr. Sandwich &middot; 200+ Outlets</div>
            <a href="mr-sandwich.html" style="font-size:13px;color:var(--kesar);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 3: South Twist -->
      <div class="craft-card" style="background:rgba(255,243,222,0.05);border:1px solid rgba(255,243,222,0.14);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 18px 40px -15px rgba(0,0,0,0.5);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/cookie_prep.mp4" type="video/mp4">
          </video>
          <span class="tag" style="position:absolute;top:12px;left:12px;z-index:2">Automated Batter</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--malai)">Thatte Idli Pre-Fermented Batter</h4>
            <p style="font-size:13px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Pre-fermented Thatte Idli batter and Ghee Podi formulations shipped fresh with zero on-site grinding.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--pista);font-weight:700;margin-bottom:8px">&bull; South Twist &middot; QSR Express</div>
            <a href="south-twist.html" style="font-size:13px;color:var(--kesar);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 4: Dunk Burgers -->
      <div class="craft-card" style="background:rgba(255,243,222,0.05);border:1px solid rgba(255,243,222,0.14);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 18px 40px -15px rgba(0,0,0,0.5);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
          </video>
          <span class="tag gold" style="position:absolute;top:12px;left:12px;z-index:2">Dip-In &amp; Glaze Station</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--malai)">Signature Dip-In &amp; Fast Assembly</h4>
            <p style="font-size:13px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Warm sauce bath burgers, crispy loaded sides, and dessert items prepared in under 180 seconds.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--kesar);font-weight:700;margin-bottom:8px">&bull; Dunk Burgers &middot; Zero Royalty</div>
            <a href="dunk-burgers.html" style="font-size:13px;color:var(--kesar);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>"""

NEW_KITCHEN_CRAFT = """<!-- ============ BEHIND THE COUNTER (LIGHT THEME) ============ -->
<section class="sec" id="kitchen-craft" style="background:#FFFFFF;position:relative;overflow:hidden;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-top rv" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:40px">
      <div class="sec-head wide">
        <p class="eyebrow"><span class="pulse"></span> Standardized Operations</p>
        <h2 style="color:var(--ink)">Behind The Counter: Central Kitchen &amp; Supply SOPs</h2>
        <p class="sec-note">Every flagship brand on Franchise 101 eliminates skilled-chef dependency with automated premixes, central manufacturing, and fast SOPs.</p>
      </div>
      <a class="btn btn--kesar btn--sm" href="#apply">Visit A Live Outlet &rarr;</a>
    </div>

    <!-- 2x2 Balanced Split-Card Grid (Light & Crisp) -->
    <div class="craft-grid-2x2 rv" style="display:grid;grid-template-columns:repeat(2, 1fr);gap:24px">
      
      <!-- Card 1: Beyond Temptation & Cafe Choco Craze -->
      <div class="craft-card" style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 12px 32px -8px rgba(14,18,26,0.07);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
          </video>
          <span class="tag gold" style="position:absolute;top:12px;left:12px;z-index:2">Chocolate &amp; Cafe Craft</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--ink)">Proprietary Chocolate Bases</h4>
            <p style="font-size:13.5px;color:var(--ink-60);line-height:1.5;margin:0">Over 85% of Cad-Bee bases &amp; dessert pre-mixes are manufactured centrally in Pune with 0% kitchen waste.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--pista-dark);font-weight:700;margin-bottom:8px">&bull; Beyond Temptation &middot; Cafe Choco Craze</div>
            <a href="beyond-temptation.html" style="font-size:13px;color:var(--kesar-hot);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 2: Mr. Sandwich -->
      <div class="craft-card" style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 12px 32px -8px rgba(14,18,26,0.07);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/baking_craft.mp4" type="video/mp4">
          </video>
          <span class="tag green" style="position:absolute;top:12px;left:12px;z-index:2">Chef-Less Baking</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--ink)">Standardized Bread &amp; Subs</h4>
            <p style="font-size:13.5px;color:var(--ink-60);line-height:1.5;margin:0">European subs, paninis, and dough recipes certified for 0% chef skill dependency and fast 4-min dispatch.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--kesar-hot);font-weight:700;margin-bottom:8px">&bull; Mr. Sandwich &middot; 200+ Outlets</div>
            <a href="mr-sandwich.html" style="font-size:13px;color:var(--kesar-hot);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 3: South Twist -->
      <div class="craft-card" style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 12px 32px -8px rgba(14,18,26,0.07);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/cookie_prep.mp4" type="video/mp4">
          </video>
          <span class="tag" style="position:absolute;top:12px;left:12px;z-index:2">Automated Batter</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--ink)">Thatte Idli Pre-Fermented Batter</h4>
            <p style="font-size:13.5px;color:var(--ink-60);line-height:1.5;margin:0">Pre-fermented Thatte Idli batter and Ghee Podi formulations shipped fresh with zero on-site grinding.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--pista-dark);font-weight:700;margin-bottom:8px">&bull; South Twist &middot; QSR Express</div>
            <a href="south-twist.html" style="font-size:13px;color:var(--kesar-hot);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 4: Dunk Burgers -->
      <div class="craft-card" style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 12px 32px -8px rgba(14,18,26,0.07);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
          </video>
          <span class="tag gold" style="position:absolute;top:12px;left:12px;z-index:2">Dip-In &amp; Glaze Station</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--ink)">Signature Dip-In &amp; Fast Assembly</h4>
            <p style="font-size:13.5px;color:var(--ink-60);line-height:1.5;margin:0">Warm sauce bath burgers, crispy loaded sides, and dessert items prepared in under 180 seconds.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--kesar-hot);font-weight:700;margin-bottom:8px">&bull; Dunk Burgers &middot; Zero Royalty</div>
            <a href="dunk-burgers.html" style="font-size:13px;color:var(--kesar-hot);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>"""

html = html.replace(OLD_KITCHEN_CRAFT, NEW_KITCHEN_CRAFT)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Converted Budget Brackets and Behind The Counter sections to clean light theme!")

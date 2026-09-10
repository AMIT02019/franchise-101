# -*- coding: utf-8 -*-
import os, re

# Update create_brand_page in generate_brand_pages.py to support brand-specific video
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    code = f.read()

# Add video_file parameter to create_brand_page definition
code = code.replace(
    'def create_brand_page(brand_id, brand_name, category, tagline, investment, payback, margin, area, outlets, states, hero_img, food_img, store_img, desc, capex_items, capex_total, formats, menu_items, pnl_data):',
    'def create_brand_page(brand_id, brand_name, category, tagline, investment, payback, margin, area, outlets, states, hero_img, food_img, store_img, desc, capex_items, capex_total, formats, menu_items, pnl_data, video_file="assets/videos/chocolate_craft.mp4", video_title="Central Kitchen Craft & SOPs"):'
)

# Add video section template inside create_brand_page HTML
VIDEO_SECTION_TEMPLATE = """<!-- ============ CENTRAL KITCHEN & OPS VIDEO SHOWCASE ============ -->
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
</section>"""

code = code.replace('<!-- ============ AUDITED CAPEX & P&L SECTION ============ -->', f'{VIDEO_SECTION_TEMPLATE}\n\n<!-- ============ AUDITED CAPEX & P&L SECTION ============ -->')

# Update 5 brand definitions with their specific video files
code = code.replace(
    'pnl_data={\n        "daily_orders": "140–180 Orders",',
    'video_file="assets/videos/chocolate_craft.mp4",\n    video_title="Cad-Bee & Chocolate Craft",\n    pnl_data={\n        "daily_orders": "140–180 Orders",'
)

code = code.replace(
    'pnl_data={\n        "daily_orders": "150–200 Orders",',
    'video_file="assets/videos/dessert_donuts.mp4",\n    video_title="Dip Station & High-Speed Assembly",\n    pnl_data={\n        "daily_orders": "150–200 Orders",'
)

code = code.replace(
    'pnl_data={\n        "daily_orders": "130–170 Orders",',
    'video_file="assets/videos/baking_craft.mp4",\n    video_title="Artisanal Bread & Sub Grilling",\n    pnl_data={\n        "daily_orders": "130–170 Orders",'
)

code = code.replace(
    'pnl_data={\n        "daily_orders": "180–240 Orders",',
    'video_file="assets/videos/cookie_prep.mp4",\n    video_title="Fresh Thatte Idli & Automated Batter",\n    pnl_data={\n        "daily_orders": "180–240 Orders",'
)

code = code.replace(
    'pnl_data={\n        "daily_orders": "140–190 Orders",',
    'video_file="assets/videos/chocolate_craft.mp4",\n    video_title="Chocolick B & Chocolate Formulations",\n    pnl_data={\n        "daily_orders": "140–190 Orders",'
)

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated generate_brand_pages.py with individual video integration")

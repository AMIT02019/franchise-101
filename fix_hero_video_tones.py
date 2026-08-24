# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Video Tag: Remove dessert_donuts.mp4 and use chocolate_craft.mp4 & baking_craft.mp4
OLD_VID_TAG = """  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="assets/brands/beyond_temptation_food.png">
      <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
      <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
      <source src="assets/videos/baking_craft.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

NEW_VID_TAG = """  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="assets/brands/beyond_temptation_food.png">
      <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
      <source src="assets/videos/baking_craft.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

html = html.replace(OLD_VID_TAG, NEW_VID_TAG)

# 2. Update CSS for Hero Video Overlay to eliminate any bright/blue tones and preserve Royal Jamun palette
OLD_OVERLAY_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
.hero-video-wrap {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 1;
}
.hero-bg-video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 1 !important;
  display: block !important;
  filter: brightness(0.88) contrast(1.08) saturate(1.15);
}
.hero-video-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: rgba(24, 8, 37, 0.48);
  pointer-events: none;
}"""

NEW_OVERLAY_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
.hero-video-wrap {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 1;
}
.hero-bg-video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.55 !important;
  display: block !important;
  filter: brightness(0.7) contrast(1.15) saturate(1.1);
}
.hero-video-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: radial-gradient(circle at 50% 30%, rgba(37, 16, 60, 0.6) 0%, rgba(24, 8, 37, 0.85) 65%, rgba(24, 8, 37, 0.96) 100%);
  pointer-events: none;
}"""

html = html.replace(OLD_OVERLAY_CSS, NEW_OVERLAY_CSS)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Replaced blue donut video with chocolate craft video and applied royal jamun palette!")

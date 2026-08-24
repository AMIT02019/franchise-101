# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add CSS for Hero Background Video
HERO_VIDEO_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
.hero-video-wrap {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}
.hero-bg-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.35;
  filter: brightness(0.6) contrast(1.15) saturate(1.2);
  transition: opacity 1.2s ease;
}
.hero-video-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 20%, rgba(37, 16, 60, 0.72) 0%, rgba(24, 8, 37, 0.88) 60%, rgba(24, 8, 37, 0.98) 100%);
}
.hero-video-overlay::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(24, 8, 37, 0.3) 0%, transparent 40%, rgba(24, 8, 37, 0.95) 100%);
}"""

if "/* ============ HERO BACKGROUND VIDEO ============ */" not in html:
    html = html.replace("/* ============ HERO ============ */", f"{HERO_VIDEO_CSS}\n\n/* ============ HERO ============ */")

# 2. Add Video Markup into <header class="hero on-dark" id="top">
HERO_MARKUP_OLD = '<header class="hero on-dark" id="top">\n  <div class="wrap hero-grid">'
HERO_MARKUP_NEW = """<header class="hero on-dark" id="top">
  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" autoplay muted loop playsinline poster="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600&auto=format&fit=crop&q=80">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-top-view-of-a-pizza-being-prepared-42774-large.mp4" type="video/mp4">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-chef-preparing-a-dish-in-a-restaurant-kitchen-42773-large.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>

  <div class="wrap hero-grid">"""

html = html.replace(HERO_MARKUP_OLD, HERO_MARKUP_NEW)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Added ambient background video to index.html and franq-franchise-website.html")

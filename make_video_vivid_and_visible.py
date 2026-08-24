# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

OLD_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
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

NEW_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
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
  opacity: 0.78;
  filter: brightness(0.85) contrast(1.1) saturate(1.2);
  transition: opacity 1.2s ease;
}
.hero-video-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 30%, rgba(37, 16, 60, 0.35) 0%, rgba(24, 8, 37, 0.6) 60%, rgba(24, 8, 37, 0.85) 100%);
}
.hero-video-overlay::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(24, 8, 37, 0.2) 0%, transparent 35%, rgba(24, 8, 37, 0.88) 100%);
}"""

html = html.replace(OLD_CSS, NEW_CSS)

# Add text shadow to hero text for maximum legibility over bright video
html = html.replace(".hero h1{color:var(--malai);max-width:14ch}", ".hero h1{color:var(--malai);max-width:14ch;text-shadow:0 4px 24px rgba(0,0,0,0.8), 0 2px 10px rgba(0,0,0,0.9)}")
html = html.replace(".hero-sub{max-width:54ch;color:rgba(255,243,222,.78);font-size:clamp(16px,1.6vw,19px)}", ".hero-sub{max-width:54ch;color:rgba(255,243,222,.94);font-size:clamp(16px,1.6vw,19px);text-shadow:0 2px 16px rgba(0,0,0,0.85)}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated video visibility, opacity and text shadows in index.html")

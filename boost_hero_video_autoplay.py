# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Video Tag with complete autoplay attributes and reliable multi-source streams
OLD_VIDEO_TAG = """  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" autoplay muted loop playsinline poster="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600&auto=format&fit=crop&q=80">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-top-view-of-a-pizza-being-prepared-42774-large.mp4" type="video/mp4">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-chef-preparing-a-dish-in-a-restaurant-kitchen-42773-large.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

NEW_VIDEO_TAG = """  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600&auto=format&fit=crop&q=80">
      <source src="https://player.vimeo.com/external/371433846.sd.mp4?s=236da2f3c0fd273d2c6d9a064f3ae35579b2bbdf&profile_id=164&oauth2_token_id=57447761" type="video/mp4">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-top-view-of-a-pizza-being-prepared-42774-large.mp4" type="video/mp4">
      <source src="https://assets.mixkit.co/videos/preview/mixkit-chef-preparing-a-dish-in-a-restaurant-kitchen-42773-large.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

html = html.replace(OLD_VIDEO_TAG, NEW_VIDEO_TAG)

# 2. Add Programmatic Autoplay Kickoff Script
AUTOPLAY_JS = """
// ============ GUARANTEED AUTOPLAY KICKOFF ============
(function() {
  const bgVid = document.getElementById('heroBgVideo');
  if (bgVid) {
    bgVid.muted = true;
    bgVid.defaultMuted = true;
    
    const playVid = function() {
      const p = bgVid.play();
      if (p !== undefined) {
        p.catch(function() {
          // Autoplay policy prevented, will play on user scroll or touch
        });
      }
    };

    // Try immediately on DOM load
    playVid();
    
    // Also try on window load
    window.addEventListener('load', playVid);

    // Fallback trigger on first user gesture
    ['touchstart', 'scroll', 'mousemove', 'click'].forEach(function(evt) {
      window.addEventListener(evt, playVid, { once: true, passive: true });
    });
  }
})();
"""

if "// ============ GUARANTEED AUTOPLAY KICKOFF ============" not in html:
    html = html.replace("</script>\n</body>", f"{AUTOPLAY_JS}\n</script>\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Boosted background video autoplay across index.html and franq-franchise-website.html")

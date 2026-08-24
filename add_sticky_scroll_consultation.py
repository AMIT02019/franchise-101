# -*- coding: utf-8 -*-
import os, re

with open("book-consultation.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace <style> block in book-consultation.html
NEW_CONSULT_STYLES = """<style>
/* Contact & Consultation Page Styles */
.contact-layout-grid {
  display: grid;
  grid-template-columns: 1fr 1.28fr;
  gap: clamp(32px, 5vw, 64px);
  align-items: start;
  position: relative;
}
@media (max-width: 960px) {
  .contact-layout-grid {
    grid-template-columns: 1fr;
  }
}

/* Sticky Consultation Form Card */
.consult-form-box {
  background: var(--jamun-deep);
  color: var(--malai);
  border-radius: clamp(24px, 4vw, 36px);
  padding: clamp(28px, 4.5vw, 44px);
  box-shadow: 0 24px 60px -20px rgba(10,3,18,0.6), 0 0 0 1px rgba(255, 243, 222, 0.12);
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 243, 222, 0.15);
}

@media (min-width: 961px) {
  .consult-form-box {
    position: -webkit-sticky;
    position: sticky;
    top: 96px;
    z-index: 20;
    will-change: transform;
    transition: box-shadow 0.3s ease, border-color 0.3s ease;
  }
}

.consult-form-box::after {
  content: "";
  position: absolute;
  top: 0; right: 0;
  width: 240px; height: 240px;
  background: radial-gradient(circle, rgba(255,176,32,0.18), transparent 70%);
  pointer-events: none;
}

.form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 18px;
}
@media (max-width: 560px) {
  .form {
    grid-template-columns: 1fr;
    gap: 14px;
  }
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: 100%;
}
.field.full {
  grid-column: 1 / -1;
}

.field label {
  font-family: var(--font-body);
  font-size: 13px;
  font-weight: 600;
  color: rgba(255, 243, 222, 0.9);
  display: block;
}

.field input,
.field select,
.field textarea {
  font: inherit;
  font-size: 14.5px;
  color: var(--malai);
  background: rgba(255, 243, 222, 0.08);
  border: 1.5px solid rgba(255, 243, 222, 0.18);
  border-radius: 12px;
  padding: 12px 15px;
  transition: all 0.25s ease;
  width: 100%;
  box-sizing: border-box;
  outline: none;
}

.field textarea {
  resize: vertical;
  min-height: 80px;
}

.field select option {
  color: #FFF3DE;
  background: #1e0e30;
}

.field input:hover,
.field select:hover,
.field textarea:hover {
  background: rgba(255, 243, 222, 0.12);
  border-color: rgba(255, 176, 32, 0.4);
}

.field input:focus,
.field select:focus,
.field textarea:focus {
  outline: none;
  border-color: var(--kesar);
  background: rgba(255, 243, 222, 0.14);
  box-shadow: 0 0 0 3px rgba(255, 176, 32, 0.2);
}

.field .err {
  font-size: 12px;
  color: #FF9C7A;
  min-height: 16px;
  line-height: 16px;
}

.brand-selected-badge {
  grid-column: 1 / -1;
  display: none;
  align-items: center;
  justify-content: space-between;
  background: rgba(255,176,32,0.15);
  border: 1px solid var(--kesar);
  border-radius: 12px;
  padding: 10px 16px;
  font-size: 13.5px;
  color: var(--malai);
}
.brand-selected-badge.show { display: flex; }
.brand-selected-badge button {
  background: none; border: 0; color: var(--kesar); cursor: pointer; font-weight: 700; font-size: 13px;
}

.sent {
  grid-column: 1 / -1;
  display: none;
  flex-direction: column;
  gap: 14px;
  background: rgba(169,232,107,0.16);
  border: 1.5px solid var(--pista);
  border-radius: 16px;
  padding: 24px;
}
.sent.show { display: flex; }
.sent b {
  font-family: var(--font-display);
  font-size: 22px;
  color: var(--pista);
}

/* Office Cards with Scroll-Spy & Active State */
.office-card {
  background: var(--paper-card);
  border: 1.5px solid var(--line);
  border-radius: 20px;
  padding: 22px 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 18px;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  box-shadow: 0 8px 20px -8px rgba(26,20,32,0.05);
}
.office-card::before {
  content: "";
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 4.5px;
  background: var(--kesar);
  border-radius: 20px 0 0 20px;
  opacity: 0;
  transition: opacity 0.3s ease;
}
.office-card:hover, .office-card.active-spy {
  transform: translateX(6px);
  border-color: var(--kesar);
  background: #FFF;
  box-shadow: 0 16px 36px -10px rgba(255, 176, 32, 0.2);
}
.office-card:hover::before, .office-card.active-spy::before {
  opacity: 1;
}

.office-card strong {
  font-family: var(--font-display);
  font-size: 18px;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 8px;
}
.office-card p {
  font-size: 14px;
  color: var(--ink-60);
  line-height: 1.5;
  margin: 0;
}
.office-card small {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--kesar-hot);
  font-weight: 600;
}

/* Advisory Steps Timeline Box */
.advisory-steps-box {
  background: var(--paper-card);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 24px;
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.advisory-step-item {
  display: flex;
  gap: 14px;
  align-items: flex-start;
}
.step-num-badge {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(255,176,32,0.15);
  color: var(--kesar-hot);
  font-weight: 800;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
</style>"""

html = re.sub(r'<style>[\s\S]*?</style>', NEW_CONSULT_STYLES, html)

# Add Advisory Steps Timeline in Left Column if not present
LEFT_COLUMN_ADDITION = """        <!-- Advisory Steps Timeline -->
        <div class="advisory-steps-box rv">
          <h4 style="margin:0;font-size:16.5px;color:var(--ink)">What Happens After You Apply?</h4>
          
          <div class="advisory-step-item">
            <span class="step-num-badge">1</span>
            <div>
              <strong style="font-size:14px;color:var(--ink);display:block">Confidential Call in 24h</strong>
              <span style="font-size:13px;color:var(--ink-60)">A senior manager reviews your city footfall, budget bracket &amp; category preference.</span>
            </div>
          </div>

          <div class="advisory-step-item">
            <span class="step-num-badge">2</span>
            <div>
              <strong style="font-size:14px;color:var(--ink);display:block">Itemized P&amp;L &amp; Capex Sheets</strong>
              <span style="font-size:13px;color:var(--ink-60)">Receive audited cost sheets and raw material gross margins before signing any agreement.</span>
            </div>
          </div>

          <div class="advisory-step-item">
            <span class="step-num-badge">3</span>
            <div>
              <strong style="font-size:14px;color:var(--ink);display:block">Direct Founder Introduction</strong>
              <span style="font-size:13px;color:var(--ink-60)">Visit a running outlet and speak with the brand directors with 100% zero brokerage fee.</span>
            </div>
          </div>
        </div>"""

if "What Happens After You Apply?" not in html:
    html = html.replace('<!-- Right: Guided Consultation Form -->', f'{LEFT_COLUMN_ADDITION}\n\n      <!-- Right: Guided Consultation Form -->')

# Add Scroll-Spy Script at bottom
SCROLL_SPY_SCRIPT = """
// Office Card Scroll-Spy Spotlight Animation
const officeCards = document.querySelectorAll('.office-card');
if (officeCards.length > 0) {
  const spyObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        officeCards.forEach(c => c.classList.remove('active-spy'));
        entry.target.classList.add('active-spy');
      }
    });
  }, { threshold: 0.6, rootMargin: '-10% 0px -30% 0px' });

  officeCards.forEach(c => spyObserver.observe(c));
}
"""

if "Office Card Scroll-Spy Spotlight Animation" not in html:
    html = html.replace('document.querySelectorAll(\'.rv\').forEach(el => io.observe(el));', f'document.querySelectorAll(\'.rv\').forEach(el => io.observe(el));\n{SCROLL_SPY_SCRIPT}')

with open("book-consultation.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated book-consultation.html with sticky scroll animation & scroll-spy spotlight!")

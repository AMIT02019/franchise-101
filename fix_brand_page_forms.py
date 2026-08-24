# -*- coding: utf-8 -*-
import os, re

# 1. UPDATE STYLES.CSS WITH COMPLETE FORM STYLING
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

FORM_CSS = """
/* ==========================================================================
   GLOBAL FORM STYLES
   ========================================================================== */
.form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px 20px;
  width: 100%;
}
@media (max-width: 640px) {
  .form {
    grid-template-columns: 1fr !important;
    gap: 14px !important;
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
  font-size: 13.5px;
  font-weight: 600;
  color: rgba(255, 243, 222, 0.9);
  font-family: var(--font-body);
  display: block;
}

.field input,
.field select,
.field textarea {
  width: 100%;
  box-sizing: border-box;
  background: rgba(255, 243, 222, 0.08);
  border: 1.5px solid rgba(255, 243, 222, 0.2);
  border-radius: 12px;
  padding: 12px 16px;
  font-size: 14.5px;
  color: var(--malai);
  font-family: var(--font-body);
  transition: border-color 0.2s, background 0.2s, box-shadow 0.2s;
  outline: none;
}

.field input:focus,
.field select:focus,
.field textarea:focus {
  border-color: var(--kesar);
  background: rgba(255, 243, 222, 0.12);
  box-shadow: 0 0 0 3px rgba(255, 176, 32, 0.2);
}

.field input::placeholder {
  color: rgba(255, 243, 222, 0.4);
}

.field select option {
  background: #1e0e30;
  color: #FFF3DE;
}

.form-actions {
  grid-column: 1 / -1;
  display: flex;
  gap: 14px;
  align-items: center;
  flex-wrap: wrap;
  margin-top: 8px;
}
"""

if "GLOBAL FORM STYLES" not in css:
    css += FORM_CSS
else:
    css = re.sub(r'/\* ==========================================================================\s+GLOBAL FORM STYLES[\s\S]*?\.form-actions \{[^\}]*\}', FORM_CSS.strip(), css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Updated styles.css with pristine form styles")

# 2. UPDATE GENERATE_BRAND_PAGES.PY & RE-RUN
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    gen_code = f.read()

# Update form actions wrapper
old_form_actions = """          <div style="margin-top:16px;display:flex;gap:14px;align-items:center;flex-wrap:wrap">
            <button type="submit" class="btn btn--kesar" id="btnSubmitApply">
              Submit Application &rarr;
            </button>
            <a class="btn btn--ghost on-dark" href="https://wa.me/912240008899?text=Hi%2C%20I%20am%20interested%20in%20{brand_name}%20Franchise" target="_blank">Chat on WhatsApp 💬</a>
          </div>"""

new_form_actions = """          <div class="form-actions">
            <button type="submit" class="btn btn--kesar" id="btnSubmitApply" style="padding:14px 28px;font-size:15px">
              Submit Application &rarr;
            </button>
            <a class="btn btn--ghost on-dark" href="https://wa.me/912240008899?text=Hi%2C%20I%20am%20interested%20in%20{brand_name}%20Franchise" target="_blank" style="padding:14px 24px">
              Chat on WhatsApp &#128172;
            </a>
          </div>"""

gen_code = gen_code.replace(old_form_actions, new_form_actions)

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(gen_code)
print("Updated generate_brand_pages.py")

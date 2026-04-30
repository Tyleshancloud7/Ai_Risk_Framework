# Screenshots Guide

> Exact instructions for capturing the 6 screenshots used in the README.

---

## Tools Needed
- Excel or LibreOffice Calc (for toolkit screenshots)
- PDF viewer (for report screenshots)
- Screenshot tool: Snagit, ShareX, macOS Screenshot, or Windows Snipping Tool
- **Resolution:** Capture at 1440px width minimum; save as PNG

---

## Screenshot 1 — `01_checklist.png`
**Sheet:** `2. Risk Assessment Checklist`
**What to show:** Rows for D1 (Bias & Fairness) — the domain header row + all 7 question rows, columns A–G visible
**Zoom level:** 90%
**Highlights:** Ensure the colored Risk Level cells (High = red, Medium = amber) are visible

**Crop:** Include just the domain header banner + the 7 question rows. Do not show the full sheet.

---

## Screenshot 2 — `02_dashboard.png`
**Sheet:** `3. Scoring Dashboard`
**What to show:** The full scoring dashboard — all 6 domain rows + the Overall total row + the Thresholds table
**Zoom level:** 85%
**Highlights:** Make sure the risk rating column shows colored labels (HIGH in red, MODERATE in amber)

---

## Screenshot 3 — `03_report_cover.png`
**File:** `reports/ChatGPT_GPT4_Risk_Assessment.pdf` — Page 1 (cover)
**What to show:** Full cover page
**Method:** Take a full-page screenshot of the PDF cover in your PDF viewer at ~100% zoom

---

## Screenshot 4 — `04_domain_findings.png`
**File:** PDF report — Section 3 (Risk Findings by Domain)
**What to show:** 2–3 domain findings blocks stacked — show D4 (Security) and D2 (Privacy) findings
**Zoom level:** 100% in PDF viewer
**Crop:** Cut to just the 2 domain finding blocks, portrait orientation

---

## Screenshot 5 — `05_heatmap.png`
**File:** PDF report — Section 4 (Risk Heat Map)
**What to show:** The full heat map table + legend
**Zoom level:** 125% in PDF viewer for clarity
**Crop:** Just the heat map table and the 4-color legend below it

---

## Screenshot 6 — `06_top5_risks.png`
**File:** PDF report — Section 5 (Top 5 Risks)
**What to show:** Risk #1 and Risk #2 blocks (the red header + detail rows beneath each)
**Zoom level:** 100% in PDF viewer
**Crop:** Portrait, showing just the two risk blocks

---

## Pro Tips

1. **Use a light desktop background** — the dark navy of the toolkit contrasts better on white/gray
2. **Hide personal info** — if your Excel username appears anywhere, crop it out
3. **Compress before uploading** — use [Squoosh](https://squoosh.app) to reduce PNG size without quality loss; aim for < 300 KB per image
4. **Consistent dimensions** — make all 6 images approximately the same width for a clean README table layout
5. **Retina / HiDPI screens** — GitHub renders images at 2× on retina; capture at 1440px for best quality

---

## Naming Convention

```
assets/
└── screenshots/
    ├── 01_checklist.png          ← Sheet 2 checklist view
    ├── 02_dashboard.png          ← Sheet 3 scoring dashboard
    ├── 03_report_cover.png       ← PDF cover page
    ├── 04_domain_findings.png    ← PDF domain findings section
    ├── 05_heatmap.png            ← PDF heat map
    └── 06_top5_risks.png         ← PDF top 5 risks section
```

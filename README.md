# 🛡️ AI Risk Assessment Framework

<div align="center">

![Version](https://img.shields.io/badge/version-1.0-blue?style=for-the-badge)
![Framework](https://img.shields.io/badge/NIST_AI_RMF-1.0-navy?style=for-the-badge)
![ISO](https://img.shields.io/badge/ISO%2FIEC-42001-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-orange?style=for-the-badge)

**A lightweight, professional AI Governance, Risk & Compliance (GRC) toolkit for assessing enterprise AI systems.**

*Aligned with NIST AI RMF 1.0 · ISO/IEC 42001 · OWASP LLM Top 10 · EU AI Act*

[📊 View Toolkit](#-toolkit) · [📄 Sample Report](#-sample-report) · [🚀 Quick Start](#-quick-start) · [🗂️ Framework Design](#%EF%B8%8F-framework-design)

</div>

---

## 📌 Overview

This project provides a **repeatable, structured methodology** for assessing the risk posture of AI systems across six critical governance domains. It is designed for:

- **GRC & compliance professionals** governing AI adoption
- **Security teams** evaluating LLM attack surfaces
- **AI governance leads** building oversight programs
- **Portfolio demonstration** of real-world AI governance skills

The framework was applied to **ChatGPT (GPT-4)** as a worked example, producing a score of **3.72 / 5.00 — HIGH risk**, with Security and Data Privacy as the most exposed domains.

---

## 🖼️ Screenshots

<img width="1536" height="1024" alt="ChatGPT Image Mar 18, 2026 at 02_30_46 PM" src="https://github.com/user-attachments/assets/61770d31-43b8-46dc-8df5-addbe2f3d4b3" />


> 📸 See [`assets/screenshots/`](assets/screenshots/) for full-resolution images.

---

## 🗂️ Framework Design

The framework spans **6 risk domains** with **46 assessment questions**, each scored 1–5 and weighted by domain criticality.

### Risk Domains & Weights

| # | Domain | Weight | Rationale |
|---|--------|--------|-----------|
| D1 | 🟣 Bias & Fairness | 15% | Legal liability and ethical accountability |
| D2 | 🔵 Data Privacy & Protection | **20%** | GDPR/CCPA regulatory exposure and reputational damage |
| D3 | 🟢 Model Transparency & Explainability | 10% | Enables oversight; lower direct impact |
| D4 | 🔴 Security Risks | **25%** | Highest impact — adversarial attacks, prompt injection, leakage |
| D5 | 🟤 Accountability & Governance | 15% | Oversight gaps multiply all other risks |
| D6 | 🔵 Compliance & Legal Risk | 15% | Regulatory penalties and audit findings |

### Scoring Model

```
Domain Score    = Average of question scores (1–5)
Weighted Score  = Domain Score × Domain Weight
Overall Score   = Σ (Weighted Scores across all 6 domains)

Risk Rating:
  Score < 2.5   →  🟢 LOW
  Score 2.5–3.4 →  🟡 MODERATE
  Score 3.5–4.4 →  🔴 HIGH
  Score ≥ 4.5   →  ⚠️  CRITICAL
```

---

## 🚀 Quick Start

### Option A — Use the Excel Toolkit (Recommended)

1. Download [`toolkit/AI_Risk_Assessment_Toolkit.xlsx`](toolkit/AI_Risk_Assessment_Toolkit.xlsx)
2. Open **Sheet 2 — Risk Assessment Checklist**
3. Score each question **1–5** for your target AI system
4. View auto-calculated results in **Sheet 3 — Scoring Dashboard**
5. Review findings and recommendations in **Sheet 4 — Risk Summary**

### Option B — Generate a Custom Report (Python)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-risk-assessment-framework.git
cd ai-risk-assessment-framework

# Install dependencies
pip install -r requirements.txt

# Generate the PDF report
python scripts/generate_report.py --system "Your AI System" --output reports/

# Generate the Excel toolkit
python scripts/generate_toolkit.py --output toolkit/
```

---

## 📊 Toolkit

**File:** [`toolkit/AI_Risk_Assessment_Toolkit.xlsx`](toolkit/AI_Risk_Assessment_Toolkit.xlsx)

| Sheet | Purpose |
|-------|---------|
| 📋 **1. Instructions** | Framework overview, scoring legend, domain weight rationale |
| ✅ **2. Risk Assessment Checklist** | 46 questions across 6 domains with scoring column |
| 📊 **3. Scoring Dashboard** | Auto-calculated domain scores and overall risk rating |
| 📝 **4. Risk Summary** | Pre-filled ChatGPT sample with top risks and remediation roadmap |

**Key Excel features:**
- `AVERAGE()` formula auto-calculates domain scores from question responses
- `IF()` nested logic auto-assigns risk rating labels
- Weighted score formula: `=Avg_Score × Domain_Weight`
- Conditional formatting highlights Critical/High/Moderate/Low cells

---

## 📄 Sample Report

**File:** [`reports/ChatGPT_GPT4_Risk_Assessment.pdf`](reports/ChatGPT_GPT4_Risk_Assessment.pdf)

### ChatGPT (GPT-4) — Assessment Results

| Domain | Weight | Score | Wtd Score | Rating |
|--------|--------|-------|-----------|--------|
| Bias & Fairness | 15% | 3.4 | 0.51 | 🟡 MODERATE |
| Data Privacy & Protection | 20% | 3.8 | 0.76 | 🔴 HIGH |
| Transparency & Explainability | 10% | 3.6 | 0.36 | 🔴 HIGH |
| **Security Risks** | **25%** | **4.1** | **1.03** | 🔴 **HIGH** |
| Accountability & Governance | 15% | 3.2 | 0.48 | 🟡 MODERATE |
| Compliance & Legal Risk | 15% | 3.5 | 0.53 | 🔴 HIGH |
| **OVERALL** | **100%** | — | **3.72** | 🔴 **HIGH** |

### Top 5 Risks Identified

| # | Risk | Domain | Severity |
|---|------|--------|----------|
| 1 | Prompt injection enabling policy bypass | Security | ⚠️ CRITICAL |
| 2 | Training data memorization leaking PII | Privacy | 🔴 HIGH |
| 3 | No explainability for high-stakes decisions | Transparency | 🔴 HIGH |
| 4 | EU AI Act / GDPR cross-border compliance gap | Compliance | 🔴 HIGH |
| 5 | Demographic bias in content/decision outputs | Bias | 🟡 MODERATE |

---

## 📁 Project Structure

```
ai-risk-assessment-framework/
│
├── 📄 README.md                          ← You are here
├── 📄 requirements.txt                   ← Python dependencies
├── 📄 LICENSE                            ← MIT License
│
├── 📂 framework/
│   ├── domain_definitions.md             ← Full domain descriptions & questions
│   ├── scoring_methodology.md            ← Scoring model & formula documentation
│   └── controls_library.md              ← Mitigation controls reference library
│
├── 📂 toolkit/
│   └── AI_Risk_Assessment_Toolkit.xlsx   ← Main Excel assessment tool
│
├── 📂 reports/
│   └── ChatGPT_GPT4_Risk_Assessment.pdf  ← Sample completed assessment
│
├── 📂 scripts/
│   ├── generate_report.py                ← PDF report generator
│   ├── generate_toolkit.py               ← Excel toolkit generator
│   └── requirements.txt                  ← Script-level dependencies
│
├── 📂 docs/
│   ├── CONTRIBUTING.md                   ← How to contribute
│   ├── CHANGELOG.md                      ← Version history
│   └── screenshots_guide.md              ← What screenshots to capture
│
└── 📂 assets/
    └── screenshots/                      ← UI screenshots for README
        ├── 01_checklist.png
        ├── 02_dashboard.png
        ├── 03_report_cover.png
        ├── 04_domain_findings.png
        ├── 05_heatmap.png
        └── 06_top5_risks.png
```

---

## 🔍 Domain Deep Dive

<details>
<summary><strong>D1 — Bias & Fairness (7 questions)</strong></summary>

Assesses whether the AI system exhibits unfair discrimination across demographic groups, and whether fairness controls are documented and enforced.

**Sample questions:**
- Has the training data been audited for demographic or historical bias?
- Are fairness metrics (equalized odds, demographic parity) defined and monitored?
- Is model performance monitored separately per subgroup (accuracy, FPR, FNR)?

**Key controls:** Bias audits, disparate impact analysis, fairness dashboards, diverse training data.

</details>

<details>
<summary><strong>D2 — Data Privacy & Protection (8 questions)</strong></summary>

Evaluates PII handling, consent mechanisms, data minimization, retention policies, and regulatory compliance (GDPR/CCPA).

**Sample questions:**
- Is PII identified, classified, and minimized in training datasets?
- Are model memorization and training data extraction risks evaluated?
- Is consent obtained and recorded for personal data used in model training?

**Key controls:** Differential privacy, DSAR workflow, DPAs with vendors, data minimization.

</details>

<details>
<summary><strong>D3 — Model Transparency & Explainability (7 questions)</strong></summary>

Covers explainability tooling, model documentation (model cards), user disclosure, and contestation mechanisms.

**Sample questions:**
- Can the system provide human-understandable explanations for its outputs?
- Is there a mechanism for users to contest AI-generated decisions?
- Are model limitations and known failure modes documented?

**Key controls:** Model cards, SHAP/LIME integration, confidence scores, audit logs.

</details>

<details>
<summary><strong>D4 — Security Risks (9 questions)</strong></summary>

The highest-weighted domain. Covers adversarial attacks, prompt injection, data leakage, API security, and supply chain integrity.

**Sample questions:**
- Has the model been tested against adversarial input attacks?
- Are prompt injection and jailbreak attack vectors identified and mitigated?
- Is there a documented incident response plan specific to AI system compromise?

**Key controls:** Red-teaming, input sanitization, output filtering, API rate limiting, IR playbooks.

</details>

<details>
<summary><strong>D5 — Accountability & Governance (8 questions)</strong></summary>

Assesses governance structures: AI risk ownership, oversight committees, HITL processes, vendor governance.

**Sample questions:**
- Is there a designated AI Risk Owner with clear accountability?
- Does an AI governance committee review high-risk deployments?
- Is an AI model inventory maintained listing all systems in production?

**Key controls:** AI governance charter, model inventory, RACI matrix, vendor AI clauses.

</details>

<details>
<summary><strong>D6 — Compliance & Legal Risk (7 questions)</strong></summary>

Reviews regulatory obligations: EU AI Act classification, sector regulations (HIPAA, FCRA), copyright/IP, cross-border data flows.

**Sample questions:**
- Is the AI system assessed against EU AI Act risk classification?
- Are copyright/IP ownership issues resolved for training data and outputs?
- Is cross-border data transfer compliance maintained?

**Key controls:** Legal reviews, SCCs, regulatory monitoring, AI liability contractual clauses.

</details>

---

## 🛠️ Customization Guide

### Adapting for Your Organization

1. **Adjust domain weights** in `framework/scoring_methodology.md` to reflect your risk appetite
2. **Add/remove questions** in Sheet 2 of the Excel toolkit — formulas auto-adjust
3. **Update scoring thresholds** for LOW/MODERATE/HIGH/CRITICAL in the dashboard formulas
4. **Extend the controls library** in `framework/controls_library.md` with your existing control catalog

### Applying to a Different AI System

Replace the ChatGPT sample assessment with your own:
1. Open Sheet 2 and update scores column (E) for each question
2. Add evidence and notes in column G
3. Review the auto-updated dashboard in Sheet 3
4. Update the system metadata in Sheet 4

---

## 📚 Framework Alignment

| Standard | How This Framework Maps |
|----------|------------------------|
| **NIST AI RMF 1.0** | GOVERN → D5; MAP → D1,D2,D3,D6; MEASURE → All domains; MANAGE → Recommendations |
| **ISO/IEC 42001** | Clause 6.1 (Risk) → All; Clause 8.4 (System impact) → D1,D4; Clause 9.1 (Monitoring) → D3,D5 |
| **OWASP LLM Top 10** | LLM01 Prompt Injection → D4; LLM06 Sensitive Disclosure → D2; LLM09 Overreliance → D3 |
| **EU AI Act** | GPAI obligations → D6; Transparency → D3; Fundamental rights → D1 |
| **GDPR** | Art. 5 (principles) → D2; Art. 22 (automated decisions) → D3,D5; Art. 32 (security) → D4 |

---

## 🤝 Contributing

Contributions are welcome. See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) for guidelines.

Ideas for contributions:
- Additional assessment questions for emerging risks (agentic AI, multimodal systems)
- Translations of the framework into other languages
- Integration scripts for popular GRC platforms (ServiceNow, Archer)
- Additional worked examples (open-source LLMs, computer vision systems)

---

## 📜 License

MIT License — see [`LICENSE`](LICENSE) for details.

---

## 👤 Author

Built as a portfolio project demonstrating AI Governance, Risk & Compliance (GRC) skills.

**Frameworks referenced:**
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-rmf)
- [ISO/IEC 42001](https://www.iso.org/standard/81230.html)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [EU AI Act](https://artificialintelligenceact.eu/)

---

<div align="center">
<i>If this project helped you, please ⭐ star the repo and share it with your network.</i>
</div>

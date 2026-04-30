# Scoring Methodology

> Complete documentation of the AI Risk Assessment Framework scoring model, formulas, and risk rating logic.

---

## Overview

The framework uses a **weighted composite scoring model** with two levels of aggregation:

1. **Question-level scoring** — each question scored 1–5 by the assessor
2. **Domain-level scoring** — average of question scores, multiplied by domain weight
3. **Overall composite score** — sum of all weighted domain scores

---

## Question Scoring Scale

| Score | Label | Description | Control Maturity |
|-------|-------|-------------|------------------|
| **1** | Very Low | Risk is negligible or fully mitigated | Strong, documented, tested controls in place |
| **2** | Low | Risk is minor with adequate controls | Controls exist and are mostly effective |
| **3** | Moderate | Risk is present with partial controls | Controls exist but gaps remain |
| **4** | High | Significant risk with weak/missing controls | Controls are minimal or ad hoc |
| **5** | Critical | Severe risk with no meaningful controls | No controls or controls are ineffective |

**Scoring guidance:** Score based on the *current state* of controls in your organization. Do not score based on vendor claims unless independently verified. When uncertain, score conservatively (higher risk).

---

## Domain Weights

| Domain | Weight | Rationale |
|--------|--------|-----------|
| Security Risks (D4) | **25%** | Highest direct impact; adversarial exploitation is active and proven |
| Data Privacy & Protection (D2) | **20%** | Regulatory penalties and reputational harm are high-consequence |
| Bias & Fairness (D1) | 15% | Legal liability and ethical accountability in high-stakes decisions |
| Accountability & Governance (D5) | 15% | Governance gaps amplify all other risk domains |
| Compliance & Legal Risk (D6) | 15% | Direct regulatory exposure; fines scale with organization size |
| Model Transparency & Explainability (D3) | 10% | Operational risk; enables oversight but lower direct financial impact |
| **Total** | **100%** | |

> **Customizing weights:** Organizations may adjust weights to reflect their industry, regulatory environment, or risk appetite. Document any changes in your assessment record. Weights must sum to 100%.

---

## Formulas

### Domain Average Score
```
Domain_Avg = AVERAGE(Q1_score, Q2_score, ..., Qn_score)
```

**Excel formula (example for D1, questions in E6:E12):**
```excel
=AVERAGE('2. Risk Assessment Checklist'!E6:E12)
```

---

### Weighted Domain Score
```
Domain_Weighted = Domain_Avg × Domain_Weight
```

**Excel formula (example for D1 on dashboard row 5):**
```excel
=E5 * C5
```
Where `E5` = domain average, `C5` = domain weight (0.15)

---

### Overall Composite Score
```
Overall_Score = Σ (Domain_Weighted_Score) for all 6 domains
```

**Excel formula:**
```excel
=SUM(F5:F10)
```
Where `F5:F10` contains the 6 weighted domain scores.

---

### Risk Rating Label
```
IF Overall_Score >= 4.5 → CRITICAL
IF Overall_Score >= 3.5 → HIGH
IF Overall_Score >= 2.5 → MODERATE
ELSE                    → LOW
```

**Excel formula:**
```excel
=IF(E11>=4.5,"CRITICAL",IF(E11>=3.5,"HIGH",IF(E11>=2.5,"MODERATE","LOW")))
```

---

## Risk Rating Thresholds

| Rating | Score Range | Required Action | Typical Timeframe |
|--------|-------------|-----------------|-------------------|
| 🟢 **LOW** | < 2.5 | Maintain controls; periodic review | Annual review |
| 🟡 **MODERATE** | 2.5 – 3.4 | Implement mitigations; track via risk register | 90 days |
| 🔴 **HIGH** | 3.5 – 4.4 | Immediate remediation plan; executive awareness | 30 days |
| ⚠️ **CRITICAL** | ≥ 4.5 | Consider deployment halt; emergency response | Immediate |

---

## Worked Example — ChatGPT (GPT-4)

| Domain | Weight | Avg Score | Wtd Score |
|--------|--------|-----------|-----------|
| Bias & Fairness | 0.15 | 3.4 | **0.51** |
| Data Privacy | 0.20 | 3.8 | **0.76** |
| Transparency | 0.10 | 3.6 | **0.36** |
| Security | 0.25 | 4.1 | **1.03** |
| Governance | 0.15 | 3.2 | **0.48** |
| Compliance | 0.15 | 3.5 | **0.53** |
| **OVERALL** | **1.00** | — | **3.67** |

**Rating: 🔴 HIGH**

---

## Limitations & Assumptions

- Scores reflect assessor judgment at a point in time; risk posture changes as systems and controls evolve
- This framework is qualitative; it supplements but does not replace quantitative risk analysis
- Domain weights are illustrative defaults; adjust for your organizational context
- The framework does not assess vendor security independently — scores should reflect your own verified controls

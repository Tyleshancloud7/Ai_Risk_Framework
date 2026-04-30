# AI Risk Controls Library

> A reference catalog of mitigation controls mapped to each risk domain. Use this to populate the "Controls" column in your risk register and to design remediation roadmaps.

---

## D1 — Bias & Fairness Controls

| Control ID | Control Name | Description | Effort | Priority |
|------------|-------------|-------------|--------|----------|
| BF-01 | Training Data Audit | Conduct pre-training audit of data sources for demographic representation and historical bias | Medium | High |
| BF-02 | Fairness Metric Definition | Define and document measurable fairness metrics (demographic parity, equalized odds) for the use case | Low | High |
| BF-03 | Subgroup Performance Monitoring | Disaggregate production performance metrics by demographic subgroup; alert on divergence | Medium | High |
| BF-04 | Third-Party Bias Audit | Commission annual independent bias evaluation with published results | High | Medium |
| BF-05 | Disparate Impact Analysis | Conduct structured analysis of adverse outcomes by protected class before deployment | Medium | High |
| BF-06 | Diverse Evaluation Panel | Include diverse stakeholders in model evaluation and testing sign-off | Low | Medium |
| BF-07 | Bias Remediation SOP | Document the process for identifying, escalating, and remediating discovered bias | Low | Medium |

---

## D2 — Data Privacy & Protection Controls

| Control ID | Control Name | Description | Effort | Priority |
|------------|-------------|-------------|--------|----------|
| DP-01 | PII Classification & Scanning | Implement automated PII detection and classification across training datasets | Medium | Critical |
| DP-02 | Data Minimization | Remove or anonymize PII not required for model training objectives | Medium | High |
| DP-03 | Consent Management | Implement consent records for personal data used in training; verify legal basis | High | Critical |
| DP-04 | Differential Privacy | Apply DP-SGD or output perturbation to limit individual data exposure | High | High |
| DP-05 | ROPA Documentation | Maintain Records of Processing Activities for all AI-related data processing | Low | High |
| DP-06 | DSAR Workflow | Establish a documented workflow for responding to data subject access/erasure requests | Medium | High |
| DP-07 | Vendor DPAs | Ensure all AI vendors processing personal data have signed Data Processing Agreements | Low | High |
| DP-08 | Membership Inference Testing | Conduct adversarial membership inference tests to quantify training data leakage risk | High | High |
| DP-09 | Output PII Monitoring | Deploy automated PII detection on model outputs before delivery to users | Medium | Critical |

---

## D3 — Transparency & Explainability Controls

| Control ID | Control Name | Description | Effort | Priority |
|------------|-------------|-------------|--------|----------|
| TE-01 | Model Card Publication | Publish and maintain standardized model documentation per Google's Model Card standard | Low | High |
| TE-02 | AI Disclosure Notice | Display clear disclosure to users that they are interacting with an AI system | Low | Critical |
| TE-03 | Confidence Scoring | Surface model confidence/uncertainty estimates alongside outputs | Medium | Medium |
| TE-04 | Explainability Integration | Integrate SHAP, LIME, or Integrated Gradients for feature attribution | High | Medium |
| TE-05 | Audit Logging | Retain structured logs of model inputs, outputs, and user context for forensic analysis | Medium | High |
| TE-06 | Contestation Workflow | Implement a process for users to flag and appeal AI-generated decisions | Medium | High |
| TE-07 | Limitations Documentation | Document known failure modes, edge cases, and out-of-scope use cases in model docs | Low | Medium |

---

## D4 — Security Controls

| Control ID | Control Name | Description | Effort | Priority |
|------------|-------------|-------------|--------|----------|
| SEC-01 | Adversarial Red-Teaming | Conduct quarterly structured red-team exercises targeting OWASP LLM Top 10 | High | Critical |
| SEC-02 | Input Sanitization | Implement input validation and sanitization layer before prompts reach the model | Medium | Critical |
| SEC-03 | Output Filtering | Deploy content classifiers and PII detectors to screen model outputs | Medium | Critical |
| SEC-04 | Prompt Injection Detection | Implement LLM-specific injection detection classifiers or rule-based guards | Medium | Critical |
| SEC-05 | API Authentication & Rate Limiting | Enforce OAuth2/API key auth and per-user/org rate limits on model endpoints | Low | High |
| SEC-06 | AI-Specific IR Playbook | Develop and test incident response procedures specific to AI system compromise | Medium | High |
| SEC-07 | Model Artifact Protection | Encrypt model weights at rest; restrict access; monitor for exfiltration | Medium | High |
| SEC-08 | Supply Chain Verification | Maintain SBOM for AI dependencies; scan training data for poisoning indicators | High | High |
| SEC-09 | Production Anomaly Detection | Deploy behavioral monitoring to detect anomalous inference patterns and drift | High | High |

---

## D5 — Accountability & Governance Controls

| Control ID | Control Name | Description | Effort | Priority |
|------------|-------------|-------------|--------|----------|
| GOV-01 | AI Risk Owner Assignment | Designate a named AI Risk Owner with executive accountability and authority | Low | Critical |
| GOV-02 | AI Governance Committee | Establish a cross-functional AI review board for high-risk deployment approvals | Medium | High |
| GOV-03 | AI Model Inventory | Maintain a live registry of all AI systems in production with owner, risk rating, and review date | Medium | High |
| GOV-04 | HITL Policy | Define and enforce human-in-the-loop requirements for high-stakes AI decisions | Medium | High |
| GOV-05 | AI Risk Policy | Document AI risk policy covering governance, acceptable use, and prohibited applications | Low | High |
| GOV-06 | Vendor AI Governance Clauses | Include AI-specific obligations in vendor contracts (audit rights, incident notification) | Low | High |
| GOV-07 | AI Incident Register | Maintain a log of AI incidents, near-misses, and lessons learned with periodic review | Low | Medium |
| GOV-08 | AI Literacy Training | Deliver role-appropriate training on AI risks, limitations, and responsible use | Medium | Medium |

---

## D6 — Compliance & Legal Controls

| Control ID | Control Name | Description | Effort | Priority |
|------------|-------------|-------------|--------|----------|
| COMP-01 | EU AI Act Gap Analysis | Conduct structured gap analysis against GPAI or high-risk AI obligations | Medium | High |
| COMP-02 | Legal Review Process | Establish mandatory legal review sign-off for AI deployment in regulated contexts | Low | High |
| COMP-03 | IP & Copyright Review | Verify training data licensing and establish policy on generated content IP ownership | Medium | High |
| COMP-04 | Sector Regulation Mapping | Map applicable sector regulations (HIPAA, FCRA, ECOA) to AI use case requirements | Medium | High |
| COMP-05 | Regulatory Horizon Scanning | Subscribe to regulatory update services; designate owner for AI regulation monitoring | Low | Medium |
| COMP-06 | SCCs & Data Transfer Controls | Implement Standard Contractual Clauses or equivalent for cross-border AI data flows | Medium | High |
| COMP-07 | Contractual Liability Review | Review and update AI-related liability, indemnification, and warranty clauses | Medium | Medium |

---

## Control Priority Guide

| Priority | Action | Timeframe |
|----------|--------|-----------|
| **Critical** | Implement immediately; block deployment if not in place | 0–30 days |
| **High** | Implement as part of structured remediation plan | 30–90 days |
| **Medium** | Schedule for next planning cycle | 90–180 days |
| **Low** | Include in long-term governance roadmap | 180+ days |

---

*Add your own controls to this library as your program matures. Map each control to your existing GRC platform control catalog for continuity.*

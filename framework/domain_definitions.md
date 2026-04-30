# Domain Definitions & Assessment Questions

> Full reference for all 6 risk domains, 46 assessment questions, risk levels, and mitigation controls.
> Aligned with NIST AI RMF 1.0 | ISO/IEC 42001 | OWASP LLM Top 10 | EU AI Act

---

## D1 — Bias & Fairness
**Weight: 15% | Questions: 7**

### Definition
Assesses whether the AI system produces outputs that systematically disadvantage or discriminate against individuals based on protected characteristics (race, gender, age, disability, etc.), and whether the organization has implemented controls to detect and remediate bias.

### Assessment Questions

| ID | Question | Risk Level | Mitigation Controls |
|----|----------|------------|---------------------|
| D1.1 | Has the training data been audited for demographic or historical bias? | High | Data audits, bias testing reports, diverse dataset sourcing |
| D1.2 | Are fairness metrics (equalized odds, demographic parity) defined and monitored? | High | Fairness metric dashboards, alert thresholds |
| D1.3 | Does the system undergo bias testing across different demographic groups? | High | Third-party bias audits, subgroup evaluation suites |
| D1.4 | Are disparate impact analyses conducted before deployment in high-stakes decisions? | High | Pre-deployment impact assessments, sign-off gates |
| D1.5 | Is there a documented process to remediate bias when discovered post-deployment? | Medium | Bias remediation SOP, rollback capability |
| D1.6 | Are proxy variables that could introduce indirect bias identified and controlled? | Medium | Feature engineering review, proxy variable audits |
| D1.7 | Is model performance (accuracy, FPR, FNR) monitored separately per subgroup? | Medium | Disaggregated performance monitoring, drift alerts |

### Key References
- NIST AI RMF: MAP 1.5, MEASURE 2.5
- ISO/IEC 42001: Clause 8.4.2 (System impact assessment)
- EU AI Act: Article 10 (Training data), Article 9 (Risk management)

---

## D2 — Data Privacy & Protection
**Weight: 20% | Questions: 8**

### Definition
Evaluates how the AI system handles personal and sensitive data throughout its lifecycle — from training data collection to inference output — including consent, data minimization, retention, and regulatory compliance.

### Assessment Questions

| ID | Question | Risk Level | Mitigation Controls |
|----|----------|------------|---------------------|
| D2.1 | Is PII/sensitive data identified, classified, and minimized in training datasets? | High | Data classification framework, PII scanning tools |
| D2.2 | Are data retention policies enforced with documented deletion schedules? | High | Data retention automation, deletion audit logs |
| D2.3 | Is consent obtained and recorded for personal data used in model training? | High | Consent management platform, legal basis documentation |
| D2.4 | Is differential privacy or data anonymization applied to training datasets? | High | DP-SGD implementation, anonymization validation |
| D2.5 | Are data processing activities documented per GDPR/CCPA requirements? | High | ROPA (Record of Processing Activities), DPIAs |
| D2.6 | Is there a process to honor data subject access requests (DSAR) relating to AI outputs? | Medium | DSAR workflow, AI output traceability |
| D2.7 | Is data shared with third-party vendors governed by DPAs and contractual controls? | Medium | Vendor DPAs, AI-specific data sharing clauses |
| D2.8 | Are model memorization and training data extraction risks evaluated? | High | Membership inference testing, output monitoring |

### Key References
- GDPR: Articles 5, 13, 17, 25, 32
- NIST AI RMF: MAP 5.1, MEASURE 2.6
- ISO/IEC 42001: Clause 8.3 (AI system life cycle)

---

## D3 — Model Transparency & Explainability
**Weight: 10% | Questions: 7**

### Definition
Covers the degree to which the AI system's behavior, decision-making process, and limitations are understandable to stakeholders — including end-users, auditors, and regulators — and whether mechanisms exist for contestation of AI decisions.

### Assessment Questions

| ID | Question | Risk Level | Mitigation Controls |
|----|----------|------------|---------------------|
| D3.1 | Can the system provide human-understandable explanations for its outputs? | Medium | SHAP/LIME integration, explanation APIs |
| D3.2 | Is model documentation (model cards, datasheets) maintained and publicly available? | Medium | Model Card publication, documentation governance |
| D3.3 | Are feature importance and decision attribution methods implemented? | Medium | XAI tooling (SHAP, Captum), attribution dashboards |
| D3.4 | Are stakeholders informed that they are interacting with AI? | High | AI disclosure notices, UI labeling requirements |
| D3.5 | Is there a mechanism for users to contest AI-generated decisions? | High | Appeals workflow, human review escalation process |
| D3.6 | Are model limitations, known failure modes, and confidence levels documented? | Medium | Model Card "limitations" section, confidence scoring |
| D3.7 | Are audit logs of model inputs and outputs retained for forensic analysis? | Medium | Inference logging, log retention policy, SIEM integration |

### Key References
- EU AI Act: Articles 13–14 (Transparency, Human oversight)
- GDPR: Article 22 (Automated decision-making)
- NIST AI RMF: GOVERN 6.2, MEASURE 2.9

---

## D4 — Security Risks
**Weight: 25% | Questions: 9**

### Definition
Assesses the AI system's exposure to adversarial attacks, exploitation of model behavior, unauthorized access, and data leakage — with reference to OWASP LLM Top 10 and adversarial ML threat taxonomy.

### Assessment Questions

| ID | Question | Risk Level | Mitigation Controls |
|----|----------|------------|---------------------|
| D4.1 | Has the model been tested against adversarial input attacks (evasion, poisoning)? | Critical | Adversarial ML testing, robustness evaluation suites |
| D4.2 | Are prompt injection and jailbreak attack vectors identified and mitigated? | Critical | Input sanitization, output filtering, red-teaming |
| D4.3 | Is model inversion or membership inference attack risk assessed and controlled? | High | Differential privacy, output perturbation, canary tokens |
| D4.4 | Are API rate limits, authentication, and access controls enforced? | High | OAuth/API keys, rate limiting, WAF rules |
| D4.5 | Is the model supply chain (training data, dependencies) verified for integrity? | High | SBOM, dependency scanning, data provenance tracking |
| D4.6 | Are outputs sanitized to prevent leakage of sensitive training information? | Critical | Output monitors, PII detectors, content filters |
| D4.7 | Is there a documented AI-specific incident response plan? | High | AI IR playbook, SIRT escalation, tabletop exercises |
| D4.8 | Are model weights and IP protected against exfiltration? | High | Access controls on model artifacts, DRM, encryption at rest |
| D4.9 | Is continuous monitoring in place to detect anomalous model behavior in production? | High | Behavioral monitoring, drift detection, anomaly alerting |

### Key References
- OWASP LLM Top 10: LLM01 (Prompt Injection), LLM02 (Insecure Output), LLM06 (Sensitive Disclosure)
- NIST AI RMF: MANAGE 2.2, MEASURE 2.7
- MITRE ATLAS: Adversarial ML threat matrix

---

## D5 — Accountability & Governance
**Weight: 15% | Questions: 8**

### Definition
Evaluates the organizational structures, policies, and processes that ensure AI systems are developed, deployed, and monitored responsibly — including ownership, oversight, vendor governance, and staff training.

### Assessment Questions

| ID | Question | Risk Level | Mitigation Controls |
|----|----------|------------|---------------------|
| D5.1 | Is there a designated AI Risk Owner or AI Ethics Officer? | High | AI governance charter, RACI matrix |
| D5.2 | Does an AI governance committee review high-risk AI deployments? | High | AI review board, risk acceptance sign-off process |
| D5.3 | Is a human-in-the-loop (HITL) process defined for high-stakes AI decisions? | High | HITL policy, escalation thresholds, manual override capability |
| D5.4 | Are AI risk policies formally documented and reviewed at least annually? | Medium | AI risk policy, annual review calendar |
| D5.5 | Is an AI model inventory maintained listing all systems in production? | Medium | AI asset registry, version tracking, ownership mapping |
| D5.6 | Are third-party AI vendors subject to risk assessment and AI governance clauses? | High | Vendor AI risk questionnaire, contractual AI governance clauses |
| D5.7 | Are AI incidents and near-misses documented and reviewed? | Medium | AI incident log, post-incident review process |
| D5.8 | Is training provided to staff deploying or relying on AI system outputs? | Medium | AI literacy training program, role-based AI training |

### Key References
- NIST AI RMF: GOVERN 1.1–6.2 (entire GOVERN function)
- ISO/IEC 42001: Clauses 5 (Leadership), 6.2 (AI objectives), 7.3 (Awareness)
- EU AI Act: Articles 17–18 (Quality management, Record-keeping)

---

## D6 — Compliance & Legal Risk
**Weight: 15% | Questions: 7**

### Definition
Reviews the AI system's exposure to regulatory penalties, legal liability, and audit findings across applicable jurisdictions and sectors — including the EU AI Act, GDPR, sector regulations, and intellectual property law.

### Assessment Questions

| ID | Question | Risk Level | Mitigation Controls |
|----|----------|------------|---------------------|
| D6.1 | Has a legal review been conducted for AI use cases in regulated industries? | High | Legal sign-off process, in-house/external counsel review |
| D6.2 | Is the AI system assessed against EU AI Act risk classification requirements? | High | EU AI Act gap analysis, GPAI obligations review |
| D6.3 | Are copyright/IP ownership issues resolved for training data and model outputs? | High | IP legal review, training data licensing documentation |
| D6.4 | Are sector-specific regulations (HIPAA, FCRA, ECOA) evaluated for applicable AI use cases? | High | Regulatory mapping, sector compliance checklists |
| D6.5 | Is there a documented process to assess and respond to new AI regulation? | Medium | Regulatory watch service, horizon scanning process |
| D6.6 | Are contractual AI liability limitations reviewed with legal counsel? | Medium | Contractual AI liability clauses, indemnification review |
| D6.7 | Is cross-border data transfer compliance maintained for AI training and inference? | High | SCCs, Binding Corporate Rules, data localization controls |

### Key References
- EU AI Act: Full regulation (in force 2024–2026 phased)
- GDPR: Articles 44–49 (Cross-border transfers)
- NIST AI RMF: GOVERN 4.1 (Legal and regulatory requirements)

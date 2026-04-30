from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.lib.colors import HexColor
import datetime

# ── Colors ──────────────────────────────────────────────────────────────────
NAVY      = HexColor("#1B2A4A")
MID_BLUE  = HexColor("#2E5FA3")
LIGHT_BLUE= HexColor("#D6E4F7")
ACCENT    = HexColor("#E8713A")
DARK_GRAY = HexColor("#4A4A4A")
MID_GRAY  = HexColor("#8C9BAD")
LIGHT_GRAY= HexColor("#F5F7FA")
RED       = HexColor("#C0392B")
CRITICAL  = HexColor("#922B21")
AMBER     = HexColor("#D4AC0D")
GREEN     = HexColor("#1E8449")
WHITE     = colors.white
BLACK     = colors.black

styles = getSampleStyleSheet()

def style(name, **kw):
    return ParagraphStyle(name, **kw)

Title = style("Title2",
    fontName="Helvetica-Bold", fontSize=26, textColor=WHITE,
    alignment=TA_CENTER, spaceAfter=4, leading=32)

Subtitle = style("Subtitle2",
    fontName="Helvetica", fontSize=11, textColor=LIGHT_BLUE,
    alignment=TA_CENTER, spaceAfter=6)

H1 = style("H1", fontName="Helvetica-Bold", fontSize=14,
    textColor=NAVY, spaceBefore=18, spaceAfter=6,
    borderPad=4, leading=18)

H2 = style("H2", fontName="Helvetica-Bold", fontSize=11,
    textColor=MID_BLUE, spaceBefore=12, spaceAfter=4, leading=14)

Body = style("Body2", fontName="Helvetica", fontSize=10,
    textColor=DARK_GRAY, leading=15, spaceAfter=6, alignment=TA_JUSTIFY)

BulletStyle = style("Bullet2", fontName="Helvetica", fontSize=10,
    textColor=DARK_GRAY, leading=14, spaceAfter=3,
    leftIndent=16, bulletIndent=4)

Small = style("Small2", fontName="Helvetica", fontSize=8,
    textColor=MID_GRAY, leading=10)

FooterS = style("Footer2", fontName="Helvetica", fontSize=8,
    textColor=MID_GRAY, alignment=TA_CENTER)

Bold = style("Bold2", fontName="Helvetica-Bold", fontSize=10,
    textColor=DARK_GRAY, leading=14)

CalloutStyle = style("Callout", fontName="Helvetica-Bold", fontSize=13,
    textColor=WHITE, alignment=TA_CENTER, leading=16)

# ── Page template with header/footer ────────────────────────────────────────
PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch

def on_page(canvas, doc):
    canvas.saveState()
    # Top rule
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 0.35*inch, PAGE_W, 0.35*inch, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(WHITE)
    canvas.drawString(MARGIN, PAGE_H - 0.24*inch, "AI RISK ASSESSMENT FRAMEWORK")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.24*inch,
                           "ChatGPT (GPT-4) — CONFIDENTIAL SAMPLE")
    # Bottom rule
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 0.3*inch, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(WHITE)
    canvas.drawCentredString(PAGE_W/2, 0.1*inch,
        f"Page {doc.page}  |  AI Risk Assessment Framework v1.0  |  April 2026")
    canvas.restoreState()

def cover_page(canvas, doc):
    canvas.saveState()
    # Full-page gradient background
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Accent strip
    canvas.setFillColor(MID_BLUE)
    canvas.rect(0, PAGE_H*0.52, PAGE_W, PAGE_H*0.48, fill=1, stroke=0)
    # Bottom accent
    canvas.setFillColor(ACCENT)
    canvas.rect(0, 0, PAGE_W, 0.4*inch, fill=1, stroke=0)
    canvas.restoreState()

doc = BaseDocTemplate(
    "/home/claude/AI_Risk_Assessment_Report.pdf",
    pagesize=letter,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=0.7*inch, bottomMargin=0.6*inch,
)

frame_cover = Frame(0, 0, PAGE_W, PAGE_H, id="cover")
frame_body  = Frame(MARGIN, 0.55*inch, PAGE_W - 2*MARGIN,
                    PAGE_H - 1.0*inch, id="body")

doc.addPageTemplates([
    PageTemplate(id="Cover", frames=[frame_cover], onPage=cover_page),
    PageTemplate(id="Body",  frames=[frame_body],  onPage=on_page),
])

story = []

# ══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════
story.append(Spacer(1, 1.8*inch))

cover_title = Paragraph("AI RISK ASSESSMENT<br/>REPORT", style("CoverT",
    fontName="Helvetica-Bold", fontSize=36, textColor=WHITE,
    alignment=TA_CENTER, leading=44))
story.append(cover_title)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("Sample Assessment: ChatGPT (GPT-4, OpenAI)", style("CoverS",
    fontName="Helvetica", fontSize=14, textColor=LIGHT_BLUE, alignment=TA_CENTER)))
story.append(Spacer(1, 0.5*inch))

story.append(HRFlowable(width="60%", thickness=2, color=ACCENT,
                         hAlign="CENTER", spaceAfter=20))

meta_data = [
    ["Framework:", "NIST AI RMF 1.0 | ISO/IEC 42001"],
    ["Assessment Date:", "April 2026"],
    ["Classification:", "CONFIDENTIAL — PORTFOLIO SAMPLE"],
    ["Version:", "1.0"],
    ["Overall Risk Rating:", "HIGH (3.72 / 5.00)"],
]
mt = Table(meta_data, colWidths=[2*inch, 3.5*inch])
mt.setStyle(TableStyle([
    ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
    ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 11),
    ("TEXTCOLOR", (0,0), (0,-1), LIGHT_BLUE),
    ("TEXTCOLOR", (1,0), (1,-1), WHITE),
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [HexColor("#1B2A4A"), HexColor("#243B6E")]),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("TEXTCOLOR", (1,4), (1,4), HexColor("#E74C3C")),
    ("FONTNAME", (1,4), (1,4), "Helvetica-Bold"),
    ("FONTSIZE", (1,4), (1,4), 12),
]))
story.append(mt)

story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# BODY PAGES
# ══════════════════════════════════════════════════════════════════════════════

def section_hdr(text, color=NAVY):
    return Table([[Paragraph(text, style("SH",
        fontName="Helvetica-Bold", fontSize=13, textColor=WHITE, leading=16))]],
        colWidths=[PAGE_W - 2*MARGIN],
        style=TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), color),
            ("TOPPADDING", (0,0), (-1,-1), 8),
            ("BOTTOMPADDING", (0,0), (-1,-1), 8),
            ("LEFTPADDING", (0,0), (-1,-1), 12),
        ])
    )

def callout_box(label, value, label_color=NAVY, val_color=RED):
    return Table([[
        Paragraph(label, style("CL", fontName="Helvetica", fontSize=9,
                               textColor=WHITE, alignment=TA_CENTER)),
        Paragraph(value, style("CV", fontName="Helvetica-Bold", fontSize=16,
                               textColor=WHITE, alignment=TA_CENTER)),
    ]], colWidths=[1.2*inch, 1.8*inch],
    style=TableStyle([
        ("BACKGROUND", (0,0), (0,0), label_color),
        ("BACKGROUND", (1,0), (1,0), val_color),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

def risk_badge(text, level):
    colors_map = {
        "CRITICAL": CRITICAL, "HIGH": RED, "MODERATE": AMBER, "LOW": GREEN
    }
    bg = colors_map.get(level, MID_GRAY)
    return Paragraph(f'<font color="white"><b>{text}</b></font>',
                     style("RB", fontName="Helvetica-Bold", fontSize=9,
                           backColor=bg, alignment=TA_CENTER,
                           borderRadius=3, leading=12))

# ── SECTION 1: Executive Summary ─────────────────────────────────────────────
story.append(section_hdr("1. EXECUTIVE SUMMARY"))
story.append(Spacer(1, 10))

story.append(Paragraph(
    "This report presents a structured risk assessment of ChatGPT (GPT-4), a large language model (LLM) "
    "developed and operated by OpenAI. The assessment was conducted using the AI Risk Assessment Framework "
    "v1.0, which is aligned with the <b>NIST AI Risk Management Framework (AI RMF 1.0)</b> and "
    "<b>ISO/IEC 42001 AI Management Systems</b> standard.", Body))

story.append(Paragraph(
    "Across six risk domains — Bias & Fairness, Data Privacy & Protection, Model Transparency & "
    "Explainability, Security Risks, Accountability & Governance, and Compliance & Legal Risk — "
    "ChatGPT received an <b>overall weighted risk score of 3.72 out of 5.00</b>, corresponding to a "
    "<b>HIGH</b> risk rating. The most significant risk exposures were identified in Security Risks "
    "(4.1/5.0) and Data Privacy & Protection (3.8/5.0), driven by prompt injection vulnerabilities, "
    "training data memorization, and cross-jurisdictional regulatory complexity.", Body))

# Summary callout table
summary_data = [
    [callout_box("Overall Score", "3.72 / 5.00", NAVY, RED),
     callout_box("Risk Rating", "HIGH", NAVY, RED),
     callout_box("Domains Assessed", "6", NAVY, MID_BLUE),
     callout_box("Questions Assessed", "46", NAVY, MID_BLUE)],
]
st = Table(summary_data, colWidths=[1.55*inch]*4)
st.setStyle(TableStyle([
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(KeepTogether([st]))
story.append(Spacer(1, 10))

story.append(Paragraph(
    "Immediate remediation is recommended for prompt injection controls and PII output filtering. "
    "A structured AI governance program and EU AI Act compliance review should be initiated within "
    "90 days. This assessment is intended as a portfolio demonstration of GRC methodology; "
    "organizations should adapt the framework to their specific deployment context.", Body))

# ── SECTION 2: Scope & Methodology ───────────────────────────────────────────
story.append(Spacer(1, 8))
story.append(section_hdr("2. SCOPE & METHODOLOGY"))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>Assessment Scope</b>", H2))
story.append(Paragraph(
    "This assessment covers ChatGPT (GPT-4) as accessed via the OpenAI API and web interface, "
    "focusing on the model's behavior, governance controls, and risk posture as publicly documented. "
    "The assessment does not cover OpenAI's internal infrastructure security or proprietary training pipelines.", Body))

story.append(Paragraph("<b>Framework Alignment</b>", H2))
fw_data = [
    ["Framework", "Element Mapped"],
    ["NIST AI RMF 1.0", "GOVERN, MAP, MEASURE, MANAGE functions"],
    ["ISO/IEC 42001",   "Clauses 6 (Planning), 8 (Operation), 9 (Performance Evaluation)"],
    ["OWASP LLM Top 10","LLM01 (Prompt Injection), LLM06 (Sensitive Information Disclosure)"],
    ["EU AI Act",       "High-risk classification criteria and transparency obligations"],
]
ft = Table(fw_data, colWidths=[2.5*inch, 4.5*inch])
ft.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [LIGHT_GRAY, WHITE]),
    ("TEXTCOLOR", (0,1), (-1,-1), DARK_GRAY),
    ("TOPPADDING", (0,0), (-1,-1), 7),
    ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("GRID", (0,0), (-1,-1), 0.5, MID_GRAY),
]))
story.append(ft)
story.append(Spacer(1, 10))

story.append(Paragraph("<b>Scoring Methodology</b>", H2))
story.append(Paragraph(
    "Each of the 46 assessment questions was scored on a 1–5 scale (1 = Very Low risk, "
    "5 = Critical risk). Domain scores are averaged, then multiplied by domain weights to produce "
    "a weighted composite score. Security and Privacy domains carry higher weights reflecting their "
    "disproportionate regulatory and operational impact.", Body))

# ── SECTION 3: Risk Findings ─────────────────────────────────────────────────
story.append(PageBreak())
story.append(section_hdr("3. RISK FINDINGS BY DOMAIN"))
story.append(Spacer(1, 10))

domain_findings = [
    {
        "name": "D1 — Bias & Fairness",
        "weight": "15%", "score": 3.4, "level": "MODERATE",
        "color": HexColor("#5B2C6F"),
        "findings": [
            "ChatGPT exhibits documented performance disparities across languages and dialects, "
            "particularly for low-resource languages.",
            "OpenAI publishes a System Card with bias evaluation data, providing partial transparency.",
            "No standardized fairness metric (e.g., demographic parity) is publicly committed to for all use cases.",
            "Bias remediation post-deployment relies on user feedback and RLHF; no formal third-party audit cycle is disclosed.",
        ],
        "controls": "Positive: System Card publication, RLHF fine-tuning. Gap: No independent fairness audit schedule.",
    },
    {
        "name": "D2 — Data Privacy & Protection",
        "weight": "20%", "score": 3.8, "level": "HIGH",
        "color": HexColor("#1A5276"),
        "findings": [
            "Training data includes internet-scraped content potentially containing PII without explicit consent mechanisms.",
            "Model memorization of training data has been demonstrated in research, creating data leakage risk.",
            "OpenAI's Privacy Policy addresses data retention but DSAR fulfillment for training data is not comprehensively addressed.",
            "Enterprise API customers have opt-out provisions; consumer product data handling is more complex.",
        ],
        "controls": "Positive: API data opt-out, retention controls. Gap: Training data consent basis; memorization mitigations.",
    },
    {
        "name": "D3 — Model Transparency & Explainability",
        "weight": "10%", "score": 3.6, "level": "HIGH",
        "color": HexColor("#117A65"),
        "findings": [
            "ChatGPT does not provide feature attribution or explanation for its outputs.",
            "The model's system prompt and RLHF reward model are proprietary and not disclosed.",
            "Users are informed they are interacting with AI (disclosure), but reasoning is a black box.",
            "No formal contestation mechanism exists for users to challenge AI-generated decisions.",
        ],
        "controls": "Positive: AI disclosure, System Card. Gap: Explainability tooling, output contestation process.",
    },
    {
        "name": "D4 — Security Risks",
        "weight": "25%", "score": 4.1, "level": "HIGH",
        "color": HexColor("#922B21"),
        "findings": [
            "Prompt injection attacks have been publicly demonstrated, enabling partial policy bypass.",
            "Jailbreak techniques are actively maintained in public repositories, representing persistent threat.",
            "Training data extraction attacks have been demonstrated in academic research settings.",
            "API rate limiting and authentication are implemented; however, abuse at scale remains possible.",
            "Model weights are proprietary; supply chain integrity for fine-tuning APIs requires governance.",
        ],
        "controls": "Positive: Rate limiting, content moderation, API access controls. Gap: Prompt injection hardening, adversarial red-team cadence.",
    },
    {
        "name": "D5 — Accountability & Governance",
        "weight": "15%", "score": 3.2, "level": "MODERATE",
        "color": HexColor("#784212"),
        "findings": [
            "OpenAI has a Safety team and published AI safety commitments, providing some governance.",
            "An AI model registry and version control are implied by versioned API access.",
            "Third-party vendor governance for downstream API users is limited to Terms of Service.",
            "Human-in-the-loop processes are not enforced for high-stakes use cases by default.",
        ],
        "controls": "Positive: Safety team, usage policies, model versioning. Gap: HITL enforcement, downstream governance.",
    },
    {
        "name": "D6 — Compliance & Legal Risk",
        "weight": "15%", "score": 3.5, "level": "HIGH",
        "color": HexColor("#1B4F72"),
        "findings": [
            "ChatGPT is likely classified as a General Purpose AI (GPAI) under the EU AI Act, requiring transparency obligations.",
            "Copyright litigation risk is elevated given training data composition and output generation.",
            "Sector-specific compliance (HIPAA, FCRA) must be managed by deploying organizations, not OpenAI.",
            "Cross-border data transfer governance (GDPR Chapter V) requires ongoing legal review.",
        ],
        "controls": "Positive: GDPR DPA commitments for enterprise. Gap: EU AI Act GPAI compliance roadmap, IP liability clarity.",
    },
]

for df in domain_findings:
    score_color = RED if df["score"] >= 3.5 else AMBER if df["score"] >= 2.5 else GREEN
    hdr_data = [[
        Paragraph(df["name"], style("DH", fontName="Helvetica-Bold", fontSize=11,
                                    textColor=WHITE, leading=14)),
        Paragraph(f'Weight: {df["weight"]}', style("DW", fontName="Helvetica", fontSize=9,
                                                    textColor=LIGHT_BLUE, alignment=TA_RIGHT)),
        Paragraph(f'Score: {df["score"]}/5.0', style("DS", fontName="Helvetica-Bold", fontSize=11,
                                                      textColor=WHITE, alignment=TA_RIGHT)),
        Paragraph(f'{df["level"]}', style("DL", fontName="Helvetica-Bold", fontSize=10,
                                          textColor=WHITE, alignment=TA_CENTER)),
    ]]
    ht = Table(hdr_data, colWidths=[2.8*inch, 1.2*inch, 1.4*inch, 1.1*inch])
    ht.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), df["color"]),
        ("BACKGROUND", (3,0), (3,0), score_color),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    story.append(ht)

    findings_content = []
    for f in df["findings"]:
        findings_content.append(Paragraph(f"• {f}", BulletStyle))
    findings_content.append(Spacer(1, 4))
    findings_content.append(Paragraph(f"<b>Control Status:</b> {df['controls']}",
                                       style("CS", fontName="Helvetica", fontSize=9,
                                             textColor=DARK_GRAY, leading=13,
                                             leftIndent=10, backColor=LIGHT_GRAY,
                                             borderPad=6)))
    story.append(KeepTogether(findings_content))
    story.append(Spacer(1, 10))

# ── SECTION 4: Risk Heat Map ──────────────────────────────────────────────────
story.append(PageBreak())
story.append(section_hdr("4. RISK HEAT MAP"))
story.append(Spacer(1, 10))

story.append(Paragraph(
    "The heat map below plots each risk domain by <b>Likelihood</b> (probability of risk materializing) "
    "and <b>Impact</b> (consequence if risk materializes). Cell shading indicates overall risk severity.", Body))

heat_hdr = ["", "Impact: Low\n(Score 1–2)", "Impact: Medium\n(Score 3)", "Impact: High\n(Score 4–5)"]
heat_rows = [
    ["Likelihood:\nHigh",   "",                              "Bias & Fairness\n(D1: 3.4)",
     "Security Risks (D4: 4.1)\nData Privacy (D2: 3.8)\nCompliance (D6: 3.5)\nTransparency (D3: 3.6)"],
    ["Likelihood:\nMedium", "",                              "Governance\n(D5: 3.2)", ""],
    ["Likelihood:\nLow",    "",                              "",                       ""],
]

heat_table = Table([heat_hdr] + heat_rows,
    colWidths=[1.0*inch, 1.8*inch, 1.8*inch, 1.9*inch])
heat_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold"),
    ("BACKGROUND", (0,1), (0,-1), MID_BLUE),
    ("TEXTCOLOR", (0,1), (0,-1), WHITE),
    ("BACKGROUND", (3,1), (3,1), HexColor("#922B21")),  # High-High = Critical
    ("TEXTCOLOR", (3,1), (3,1), WHITE),
    ("FONTNAME", (3,1), (3,1), "Helvetica-Bold"),
    ("BACKGROUND", (2,1), (2,1), HexColor("#E8A020")),  # Med-High = Amber
    ("BACKGROUND", (2,2), (2,2), HexColor("#F0C040")),  # Med-Med = Yellow
    ("BACKGROUND", (1,1), (1,3), LIGHT_GRAY),
    ("BACKGROUND", (2,3), (3,3), HexColor("#D5F5E3")),  # Low = Green
    ("BACKGROUND", (3,2), (3,2), HexColor("#E8A020")),  # High-Med = Amber
    ("TOPPADDING", (0,0), (-1,-1), 10),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ("GRID", (0,0), (-1,-1), 0.5, WHITE),
    ("ROWHEIGHT", (0,0), (0,0), 30),
    ("ROWHEIGHT", (0,1), (0,3), 55),
]))
story.append(heat_table)
story.append(Spacer(1, 8))

legend_data = [["■ CRITICAL", "■ HIGH", "■ MODERATE", "■ LOW"]]
lt = Table(legend_data, colWidths=[1.6*inch]*4)
lt.setStyle(TableStyle([
    ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
    ("TEXTCOLOR", (0,0), (0,0), CRITICAL),
    ("TEXTCOLOR", (1,0), (1,0), RED),
    ("TEXTCOLOR", (2,0), (2,0), AMBER),
    ("TEXTCOLOR", (3,0), (3,0), GREEN),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
]))
story.append(lt)

# ── SECTION 5: Top 5 Risks ────────────────────────────────────────────────────
story.append(Spacer(1, 10))
story.append(section_hdr("5. TOP 5 RISKS & MITIGATIONS"))
story.append(Spacer(1, 10))

top5 = [
    {
        "rank": "RISK #1", "title": "Prompt Injection & Jailbreaking",
        "domain": "Security Risks", "severity": "CRITICAL",
        "desc": ("Adversaries can craft inputs that override system instructions, bypass content "
                 "policies, or cause the model to reveal sensitive information. Public jailbreak "
                 "repositories demonstrate active exploitation of this vector."),
        "impact": "Policy bypass, reputational damage, regulatory action, data leakage.",
        "mitigation": ("1. Implement robust input sanitization and output filtering pipelines. "
                       "2. Conduct quarterly adversarial red-team exercises. "
                       "3. Deploy LLM-specific WAF or input validation layer. "
                       "4. Implement prompt injection detection classifiers."),
        "timeline": "Immediate (0–30 days)",
        "color": CRITICAL,
    },
    {
        "rank": "RISK #2", "title": "Training Data Memorization & PII Leakage",
        "domain": "Data Privacy & Protection", "severity": "HIGH",
        "desc": ("Research has demonstrated that LLMs can memorize and reproduce verbatim sequences "
                 "from training data, including PII. This creates GDPR Article 17 erasure compliance "
                 "challenges and privacy harm risk."),
        "impact": "GDPR enforcement action, reputational harm, data subject harm.",
        "mitigation": ("1. Apply differential privacy techniques during fine-tuning. "
                       "2. Deploy PII detection and redaction on model outputs. "
                       "3. Conduct membership inference attack testing. "
                       "4. Establish training data erasure capability."),
        "timeline": "Short-term (30–90 days)",
        "color": RED,
    },
    {
        "rank": "RISK #3", "title": "Lack of Explainability for High-Stakes Decisions",
        "domain": "Transparency & Explainability", "severity": "HIGH",
        "desc": ("ChatGPT provides no feature attribution or reasoning trace. In high-stakes contexts "
                 "(medical, legal, financial), this prevents audit, creates accountability gaps, and "
                 "may violate emerging AI transparency regulations."),
        "impact": "Regulatory non-compliance, inability to audit or contest decisions.",
        "mitigation": ("1. Publish and maintain model cards for all production versions. "
                       "2. Implement confidence scoring on outputs. "
                       "3. Develop user contestation and human review workflow. "
                       "4. Restrict model use in regulated high-stakes decisions without HITL."),
        "timeline": "Medium-term (90–180 days)",
        "color": RED,
    },
    {
        "rank": "RISK #4", "title": "EU AI Act & Cross-Border Compliance Exposure",
        "domain": "Compliance & Legal Risk", "severity": "HIGH",
        "desc": ("As a General Purpose AI (GPAI) system, ChatGPT is subject to EU AI Act transparency "
                 "and risk management obligations. Cross-border data flows to US infrastructure also "
                 "require GDPR Chapter V compliance mechanisms."),
        "impact": "Fines up to 3% of global annual turnover; market access restrictions.",
        "mitigation": ("1. Conduct EU AI Act gap analysis against GPAI requirements. "
                       "2. Review and update Standard Contractual Clauses (SCCs) for data transfers. "
                       "3. Engage EU-based legal counsel for regulatory monitoring. "
                       "4. Implement GDPR-compliant data processing agreements with enterprise customers."),
        "timeline": "Short-term (30–90 days)",
        "color": RED,
    },
    {
        "rank": "RISK #5", "title": "Demographic Bias in Content & Decision Support",
        "domain": "Bias & Fairness", "severity": "MODERATE",
        "desc": ("Performance disparities across demographic groups have been documented in academic "
                 "literature. Without mandatory fairness audits, bias in downstream decision support "
                 "use cases (hiring, lending, healthcare triage) creates legal and ethical exposure."),
        "impact": "Disparate impact liability, regulatory investigation, reputational harm.",
        "mitigation": ("1. Commission annual third-party bias audit across demographic subgroups. "
                       "2. Publish fairness metrics in model documentation. "
                       "3. Implement subgroup performance monitoring in production. "
                       "4. Restrict use in regulated decision contexts without bias assessment."),
        "timeline": "Medium-term (90–180 days)",
        "color": AMBER,
    },
]

for risk in top5:
    rank_bg = risk["color"]
    risk_items = [
        [Paragraph(risk["rank"], style("RK", fontName="Helvetica-Bold", fontSize=11,
                                        textColor=WHITE, alignment=TA_CENTER)),
         Paragraph(f'<b>{risk["title"]}</b>', style("RT", fontName="Helvetica-Bold",
                                                     fontSize=11, textColor=WHITE)),
         Paragraph(f'Domain: {risk["domain"]}', style("RD", fontName="Helvetica", fontSize=9,
                                                        textColor=LIGHT_BLUE, alignment=TA_RIGHT)),
         Paragraph(risk["severity"], style("RS", fontName="Helvetica-Bold", fontSize=10,
                                            textColor=WHITE, alignment=TA_CENTER)),
        ],
    ]
    rt = Table(risk_items, colWidths=[0.9*inch, 2.8*inch, 1.8*inch, 1.0*inch])
    rt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), rank_bg),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    story.append(rt)

    detail_data = [
        [Paragraph("<b>Description:</b>", Bold),
         Paragraph(risk["desc"], Body)],
        [Paragraph("<b>Impact:</b>", Bold),
         Paragraph(risk["impact"], Body)],
        [Paragraph("<b>Mitigation:</b>", Bold),
         Paragraph(risk["mitigation"], Body)],
        [Paragraph("<b>Target Timeline:</b>", Bold),
         Paragraph(f'<b>{risk["timeline"]}</b>', style("TL", fontName="Helvetica-Bold",
                                                         fontSize=10, textColor=MID_BLUE))],
    ]
    dt = Table(detail_data, colWidths=[1.1*inch, 5.4*inch])
    dt.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [LIGHT_GRAY, WHITE]),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("GRID", (0,0), (-1,-1), 0.3, MID_GRAY),
    ]))
    story.append(KeepTogether([dt]))
    story.append(Spacer(1, 12))

# ── SECTION 6: Recommendations ───────────────────────────────────────────────
story.append(PageBreak())
story.append(section_hdr("6. KEY RECOMMENDATIONS"))
story.append(Spacer(1, 10))

recs = [
    ("Immediate\n0–30 Days", [
        "Deploy prompt injection detection and output filtering — prioritize security posture.",
        "Implement PII scanning on all model outputs in production environments.",
        "Initiate adversarial red-team exercise targeting LLM OWASP Top 10 vectors.",
    ], RED),
    ("Short-Term\n30–90 Days", [
        "Commission EU AI Act GPAI compliance gap analysis with legal counsel.",
        "Deploy subgroup performance monitoring for bias detection in production.",
        "Establish AI Risk Register and assign AI Risk Owner with executive accountability.",
    ], AMBER),
    ("Medium-Term\n90–180 Days", [
        "Publish comprehensive model cards and establish annual update cadence.",
        "Implement human-in-the-loop (HITL) processes for high-stakes decision use cases.",
        "Achieve ISO/IEC 42001 readiness assessment and initiate certification roadmap.",
    ], MID_BLUE),
    ("Long-Term\n180+ Days", [
        "Integrate AI risk into enterprise ERM program and board-level reporting.",
        "Pursue third-party bias audit with published findings and remediation commitments.",
        "Develop contestation and appeals workflow for users impacted by AI-generated decisions.",
    ], NAVY),
]

for timeframe, actions, color in recs:
    rec_rows = [[Paragraph(timeframe, style("TF", fontName="Helvetica-Bold", fontSize=10,
                                             textColor=WHITE, alignment=TA_CENTER,
                                             leading=13)),
                 Paragraph("<br/>".join([f"• {a}" for a in actions]),
                           style("RA", fontName="Helvetica", fontSize=10,
                                 textColor=DARK_GRAY, leading=15))]]
    rec_table = Table(rec_rows, colWidths=[1.1*inch, 5.4*inch])
    rec_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), color),
        ("BACKGROUND", (1,0), (1,0), LIGHT_GRAY),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("GRID", (0,0), (-1,-1), 0.5, WHITE),
    ]))
    story.append(rec_table)
    story.append(Spacer(1, 4))

# ── SECTION 7: Final Risk Rating ─────────────────────────────────────────────
story.append(Spacer(1, 12))
story.append(section_hdr("7. FINAL RISK RATING"))
story.append(Spacer(1, 10))

final_data = [
    ["Domain", "Weight", "Score", "Wtd Score", "Rating"],
    ["Bias & Fairness",                     "15%", "3.4", "0.51", "MODERATE"],
    ["Data Privacy & Protection",           "20%", "3.8", "0.76", "HIGH"],
    ["Model Transparency & Explainability", "10%", "3.6", "0.36", "HIGH"],
    ["Security Risks",                      "25%", "4.1", "1.03", "HIGH"],
    ["Accountability & Governance",         "15%", "3.2", "0.48", "MODERATE"],
    ["Compliance & Legal Risk",             "15%", "3.5", "0.53", "HIGH"],
    ["OVERALL WEIGHTED SCORE",              "100%","—",   "3.72", "HIGH"],
]
level_colors = {"MODERATE": AMBER, "HIGH": RED, "CRITICAL": CRITICAL, "LOW": GREEN}
ft2 = Table(final_data, colWidths=[2.6*inch, 0.7*inch, 0.7*inch, 0.9*inch, 1.6*inch])
ft2_style = [
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
    ("ROWBACKGROUNDS", (0,1), (-1,6), [LIGHT_GRAY, WHITE]),
    ("TEXTCOLOR", (0,1), (-1,6), DARK_GRAY),
    ("BACKGROUND", (0,7), (-1,7), DARK_GRAY),
    ("TEXTCOLOR", (0,7), (-1,7), WHITE),
    ("FONTNAME", (0,7), (-1,7), "Helvetica-Bold"),
    ("ALIGN", (1,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("GRID", (0,0), (-1,-1), 0.5, WHITE),
]
for row_i, row in enumerate(final_data[1:-1], 1):
    rating = row[4]
    col = level_colors.get(rating, MID_GRAY)
    ft2_style.append(("BACKGROUND", (4, row_i), (4, row_i), col))
    ft2_style.append(("TEXTCOLOR", (4, row_i), (4, row_i), WHITE))
    ft2_style.append(("FONTNAME", (4, row_i), (4, row_i), "Helvetica-Bold"))
ft2.setStyle(TableStyle(ft2_style))
story.append(ft2)
story.append(Spacer(1, 16))

# Final verdict box
verdict = Table([[
    Paragraph("FINAL VERDICT", style("FV1", fontName="Helvetica-Bold", fontSize=10,
                                      textColor=LIGHT_BLUE, alignment=TA_CENTER)),
    Paragraph("ChatGPT (GPT-4) presents a HIGH overall risk profile (3.72/5.00). "
              "Deployment in regulated or high-stakes contexts requires immediate security hardening, "
              "privacy controls, and a structured AI governance program before risk is reduced to MODERATE.",
              style("FV2", fontName="Helvetica", fontSize=10, textColor=WHITE, leading=15)),
]], colWidths=[1.2*inch, 5.3*inch])
verdict.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,0), RED),
    ("BACKGROUND", (1,0), (1,0), NAVY),
    ("TOPPADDING", (0,0), (-1,-1), 14),
    ("BOTTOMPADDING", (0,0), (-1,-1), 14),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story.append(verdict)

# Disclaimer
story.append(Spacer(1, 20))
story.append(HRFlowable(width="100%", thickness=0.5, color=MID_GRAY))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "<i>Disclaimer: This report is a portfolio demonstration of AI GRC methodology. Scores are "
    "based on publicly available information and professional judgment. This document does not "
    "constitute a formal audit or legal opinion. Organizations should engage qualified professionals "
    "for production AI risk assessments.</i>", Small))

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print("PDF saved.")

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(findings):

    filename = "reports/scan_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []


    title = "Security Misconfiguration Scanner Report"

    content.append(
        Paragraph(title, styles["Title"])
    )

    content.append(Spacer(1, 12))


    content.append(
        Paragraph(
            "Target URL: " + str(findings.get("url")),
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "Status Code: " + str(findings.get("status_code")),
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "HTTPS Enabled: " + str(findings.get("https")),
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "Server: " + str(findings.get("server")),
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "Risk Level: " + str(findings.get("risk")),
            styles["Normal"]
        )
    )


    content.append(Spacer(1, 12))


    content.append(
        Paragraph(
            "Missing Security Headers:",
            styles["Heading2"]
        )
    )


    for header in findings.get("missing_headers", []):

        content.append(
            Paragraph(
                "- " + header,
                styles["Normal"]
            )
        )


    content.append(Spacer(1, 12))


    content.append(
        Paragraph(
            "Detected Technologies:",
            styles["Heading2"]
        )
    )


    for tech in findings.get("technologies", []):

        content.append(
            Paragraph(
                "- " + tech,
                styles["Normal"]
            )
        )


    doc.build(content)


    print("[✓] PDF report saved successfully:", filename)

import json
import os
import uuid
from datetime import datetime


def print_summary(https_enabled, missing_headers, server, risk):

    print("\n========== SCAN SUMMARY ==========")

    print("HTTPS Enabled:", https_enabled)

    print("\nMissing Security Headers:")

    if missing_headers:
        for header in missing_headers:
            print("-", header)
    else:
        print("None")

    print("\nServer Information:", server)

    print("\nRisk Level:", risk)

    print("==================================")


def save_report(findings):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = "reports/scan_report.json"

    missing_headers = findings.get("missing_headers", [])
    exposed_directories = findings.get("exposed_directories", [])

    ssl_info = findings.get("ssl_certificate", {})

    total_issues = (
        len(missing_headers)
        + len(exposed_directories)
    )


    high = 0
    medium = 0
    low = 0


    if missing_headers:
        high += len(missing_headers)

    if exposed_directories:
        medium += len(exposed_directories)

    if findings.get("https"):

        low += 0


    report = {

        "report_title":
        "Security Misconfiguration Scanner Report",


        "scan_id":
        str(uuid.uuid4()),


        "scan_time":
        str(datetime.now()),


        "target":
        findings.get("url"),


        "summary": {

            "total_issues":
            total_issues,

            "severity": {

                "high":
                high,

                "medium":
                medium,

                "low":
                low

            },

            "risk_level":
            findings.get("risk")

        },


        "modules": {

            "HTTPS_Check":
            findings.get("https"),

            "Security_Headers":
            len(missing_headers),

            "Directory_Check":
            len(exposed_directories),

            "Technology_Detection":
            len(findings.get("technologies", [])),

            "SSL_Check":
            "ssl_certificate" in findings

        },


        "ssl_certificate":
        ssl_info,


        "findings":
        findings

    }


    with open(filename, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )


    print("\n[✓] Report saved successfully:", filename)

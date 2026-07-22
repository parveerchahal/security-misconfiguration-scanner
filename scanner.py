import requests
from checks import check_https, get_server
from directories import check_directories
from tech_detect import detect_technologies
from ssl_check import check_ssl
from report import print_summary, save_report
from pdf_report import create_pdf
from cookie_check import check_cookies
print("Welcome to Security Misconfiguration Scanner")

url = input("Enter Website URL: ")

findings = {}

try:
    response = requests.get(url, timeout=10)

    print("\nWebsite is reachable!")
    print("Status Code:", response.status_code)

    findings["url"] = url
    findings["status_code"] = response.status_code


    # HTTPS Check
    print("\nChecking HTTPS...\n")

    https_enabled = check_https(url)

    findings["https"] = https_enabled

    if https_enabled:
        print("[✓] Website is using HTTPS")
    else:
        print("[✗] Website is NOT using HTTPS")


    # Security Headers
    print("\nChecking Security Headers...\n")

    headers = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    missing_headers = []

    for header in headers:
        if header in response.headers:
            print(f"[✓] {header} is present")
        else:
            print(f"[✗] {header} is missing")
            missing_headers.append(header)

    findings["missing_headers"] = missing_headers


    # Server Information
    print("\nChecking Server Information...\n")

    server = get_server(response)

    findings["server"] = server

    if server == "Hidden":
        print("[✓] Server information is hidden")
    else:
        print("[!] Server Information:", server)


    # HTTP Methods
    print("\nChecking Allowed HTTP Methods...\n")

    try:
        options_response = requests.options(url, timeout=10)

        allowed_methods = options_response.headers.get("Allow")

        if allowed_methods:
            print("[+] Allowed Methods:", allowed_methods)
            findings["allowed_methods"] = allowed_methods
        else:
            print("[!] Server did not specify allowed methods")
            findings["allowed_methods"] = "Not specified"

    except Exception:
        print("[!] Could not determine allowed HTTP methods")
        findings["allowed_methods"] = "Unknown"


    # Directory Check
    exposed_directories = check_directories(url)

    findings["exposed_directories"] = exposed_directories


    # Technology Detection
    print("\nDetecting Technologies...\n")

    technologies = detect_technologies(response)

    for tech in technologies:
        print("[+] ", tech)

    findings["technologies"] = technologies


    # SSL Check
    ssl_information = check_ssl(url)

    findings["ssl_certificate"] = ssl_information
    
    # Cookie Security Check
    cookie_information = check_cookies(response)

    findings["cookie_security"] = cookie_information


    # Risk Score
    risk_points = len(missing_headers) + len(exposed_directories)

    if risk_points <= 1:
        risk = "LOW"
    elif risk_points <= 3:
        risk = "MEDIUM"
    else:
        risk = "HIGH"


    findings["risk"] = risk


    # Scan Summary
    print_summary(
        https_enabled,
        missing_headers,
        server,
        risk
    )


    # Save Report
    save_report(findings)
    # Create PDF Report
    create_pdf(findings)


except Exception as e:
    print("Error:", e)

# 🔒 Security Misconfiguration Scanner

A Python-based web security assessment tool that identifies common security misconfigurations in websites and generates detailed JSON and PDF security reports.

---

## 📖 Project Overview

The **Security Misconfiguration Scanner** is a Python project developed to analyze websites for common security weaknesses. It performs automated security checks and generates detailed reports that help identify potential security misconfigurations.

The scanner is intended for **educational purposes** and should only be used on websites that you own or have permission to test.

---

## ✨ Features

### ✅ Website Reachability Check
- Checks whether the target website is accessible.
- Displays HTTP response status code.

### ✅ HTTPS Security Check
- Detects whether HTTPS is enabled.

### ✅ Security Header Analysis
Checks important security headers:

- Content-Security-Policy
- Strict-Transport-Security
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy

### ✅ Server Information Detection
- Identifies server information exposed through HTTP headers.

### ✅ HTTP Methods Check
- Checks whether allowed HTTP methods are disclosed.

### ✅ Directory Exposure Check
Checks common sensitive paths:

- /admin
- /backup
- /.env
- /config.php

### ✅ Technology Detection
Detects possible technologies such as:

- Cloudflare
- Apache
- Nginx
- PHP
- WordPress

### ✅ SSL Certificate Analysis

Provides:

- Certificate issuer
- Expiry date
- Remaining validity
- Certificate status

### ✅ Cookie Security Check

Checks whether cookies use:

- Secure
- HttpOnly
- SameSite

### ✅ Risk Assessment

Calculates an overall risk level based on detected security issues.

### ✅ Report Generation

Generates:

- JSON Report
- PDF Report

---

# 🛠 Technologies Used

- Python 3
- Requests
- JSON
- SSL
- Socket
- FPDF
- Git
- GitHub

---

# 📂 Project Structure

```
security-misconfiguration-scanner/
│
├── scanner.py
├── checks.py
├── directories.py
├── tech_detect.py
├── ssl_check.py
├── cookie_check.py
├── report.py
├── pdf_report.py
├── README.md
├── reports/
└── backup/
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/parveerchahal/security-misconfiguration-scanner.git
```

Go to the project folder:

```bash
cd security-misconfiguration-scanner
```

Install dependencies:

```bash
pip install requests fpdf
```

Run the scanner:

```bash
python3 scanner.py
```

---

# ▶ Usage

1. Start the scanner.
2. Enter the target website URL.
3. The scanner performs all configured security checks.
4. Review the generated JSON and PDF reports.

---

# 📸 Sample Output

The scanner generates:

- Terminal output
- JSON security report
- PDF security report

*(Screenshots can be added here later.)*

---

# 🚀 Future Improvements

Possible future enhancements include:

- Port Scanning
- Subdomain Enumeration
- HTML Report Generation
- GUI Interface
- CVE Database Integration
- Multi-threaded Scanning

---

# 👩‍💻 Author

**Parveer Chahal**

Computer Science & Engineering Student

Cybersecurity Enthusiast

---

# ⚠ Disclaimer

This project is intended for **educational and authorized security testing only**.

Do not scan systems or websites without proper permission.

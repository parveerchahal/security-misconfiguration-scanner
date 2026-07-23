# 🔒 Security Misconfiguration Scanner

A Python-based web application security scanner that identifies common security misconfigurations in websites. The scanner performs multiple security checks, generates a detailed JSON report, and helps users identify potential vulnerabilities.

---

## ✨ Features

- ✅ Checks website availability
- 🔐 Verifies HTTPS configuration
- 🛡️ Detects missing security headers
- 🌐 Identifies server information
- 🔍 Checks allowed HTTP methods
- 📂 Detects exposed common directories
- ⚙️ Detects web technologies
- 📄 Generates a JSON report
- 📊 Displays scan summary with risk level

---

## 🛠️ Technologies Used

- Python 3
- Requests
- Flask
- JSON
- SSL/TLS
- Git
- GitHub

---

## 📁 Project Structure

```text
Security-Misconfiguration-Scanner/
│── scanner.py
│── checks.py
│── ssl_check.py
│── tech_detect.py
│── directories.py
│── report.py
│── reports/
│── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/parveerchahal/security-misconfiguration-scanner.git
```

### 2. Go to the project folder

```bash
cd security-misconfiguration-scanner
```

### 3. Install dependencies

```bash
pip install requests
```

### 4. Run the scanner

```bash
python3 scanner.py
```

---

# 📸 Project Screenshots

## ▶️ Running the Scanner

Shows the scanner analyzing the target website.

![Running the Scanner](scanner-run.png)

---

## 📋 Scan Summary

Displays detected security issues, missing headers, server details, and scan results.

![Scan Summary](scan-summary.png)

---

## 📄 Generated JSON Report

Automatically generated report containing scan findings and risk assessment.

![Generated JSON Report](json-report.png)

---

## 📂 Project Structure

Overview of the project files and folder organization.

![Project Structure](project-structure.png)

---

## 🔮 Future Improvements

- PDF report generation
- Multi-threaded scanning
- Export reports in multiple formats
- Additional OWASP security checks
- Improved vulnerability detection

---

## 👩‍💻 Author

**Parveer Kaur**

Computer Science & Engineering Student

Cybersecurity Trainee

---

⭐ If you found this project useful, consider giving it a star!

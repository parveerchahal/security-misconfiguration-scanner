# Security Misconfiguration Scanner

## Project Overview

Security Misconfiguration Scanner is a Python-based web security assessment tool that detects common security weaknesses in web applications.

The scanner performs automated checks for security headers, HTTPS configuration, exposed directories, server information, SSL certificate details, and technology detection.

---

## Features

### 1. Website Reachability Check
- Checks whether the target website is accessible.
- Displays HTTP response status code.

### 2. HTTPS Security Check
- Detects whether HTTPS is enabled.

### 3. Security Header Analysis
Checks important security headers:

- Content-Security-Policy
- Strict-Transport-Security
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy

### 4. Server Information Detection
- Identifies server information exposed through HTTP headers.

### 5. HTTP Methods Check
- Checks whether allowed HTTP methods are disclosed.

### 6. Directory Exposure Check
Checks common sensitive paths:

- /admin
- /backup
- /.env
- /config.php

### 7. Technology Detection
Detects possible technologies used by the website.

Examples:
- Cloudflare
- Apache
- PHP
- WordPress

### 8. SSL Certificate Analysis
Provides:

- Certificate issuer
- Expiry date
- Remaining validity days

### 9. Report Generation
Generates a JSON security assessment report.

---

## Technologies Used

- Python
- Requests Library
- SSL Module
- Socket Programming
- JSON Reporting

---

## Project Structure

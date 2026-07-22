def check_cookies(response):

    print("\nChecking Cookie Security...\n")

    cookie_results = []

    cookies = response.headers.get("Set-Cookie")


    if not cookies:
        print("[!] No cookies found")

        return [
            "No cookies detected"
        ]


    cookie = cookies.lower()


    if "secure" in cookie:
        print("[✓] Secure flag present")
        secure = "Present"
    else:
        print("[✗] Secure flag missing")
        secure = "Missing"


    if "httponly" in cookie:
        print("[✓] HttpOnly flag present")
        httponly = "Present"
    else:
        print("[✗] HttpOnly flag missing")
        httponly = "Missing"


    if "samesite" in cookie:
        print("[✓] SameSite attribute present")
        samesite = "Present"
    else:
        print("[✗] SameSite attribute missing")
        samesite = "Missing"


    cookie_results.append({
        "Secure": secure,
        "HttpOnly": httponly,
        "SameSite": samesite
    })


    return cookie_results

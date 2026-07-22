import requests


def check_directories(url):

    print("\nChecking Common Directories...\n")

    common_paths = [
        "/admin",
        "/login",
        "/backup",
        "/backup.zip",
        "/config.php",
        "/.env",
        "/robots.txt"
    ]

    found = []

    for path in common_paths:

        target = url.rstrip("/") + path

        try:
            response = requests.get(target, timeout=5)

            if response.status_code == 200:
                print("[!] Found:", target)
                found.append(target)

            else:
                print("[✗] Not Found:", path)

        except Exception:
            print("[!] Error checking:", path)

    return found

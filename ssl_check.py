import ssl
import socket
from datetime import datetime


def check_ssl(url):

    print("\nChecking SSL Certificate...\n")

    try:
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=10) as sock:

            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                certificate = ssock.getpeercert()


        expiry_date = certificate["notAfter"]

        expiry = datetime.strptime(
            expiry_date,
            "%b %d %H:%M:%S %Y %Z"
        )

        remaining_days = (expiry - datetime.now()).days


        issuer = certificate.get("issuer")


        ssl_data = {

            "issuer": str(issuer),

            "expiry_date": str(expiry),

            "days_remaining": remaining_days

        }


        print("[✓] SSL Certificate Valid")

        print("[+] Expiry:", expiry)

        print("[+] Days Remaining:", remaining_days)


        return ssl_data


    except Exception as e:

        print("[✗] SSL Check Failed:", e)

        return {
            "error": str(e)
        }

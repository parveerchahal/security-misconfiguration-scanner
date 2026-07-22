def detect_technologies(response):

    technologies = []

    headers = response.headers

    server = headers.get("Server", "")

    powered = headers.get("X-Powered-By", "")


    if server:
        technologies.append("Server: " + server)


    if powered:
        technologies.append("Powered By: " + powered)


    content = response.text.lower()


    if "wp-content" in content:
        technologies.append("WordPress")


    if "react" in content:
        technologies.append("React")


    if "jquery" in content:
        technologies.append("jQuery")


    if "php" in content:
        technologies.append("PHP")


    if "cloudflare" in server.lower():
        technologies.append("Cloudflare")


    return technologies

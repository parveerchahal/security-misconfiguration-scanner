def check_https(url):
    return url.startswith("https://")


def get_server(response):
    return response.headers.get("Server", "Hidden")

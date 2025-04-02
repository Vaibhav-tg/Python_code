def app(environ, start_response):
    start_response("200 OK", [])
    return iter([b"How It's work"])

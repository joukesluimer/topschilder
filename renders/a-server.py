"""Kleine renderserver voor de three.js-scènes in renders/a-*.html.

Gebruik (vanuit de projectmap):
    python3 renders/a-server.py [poort]
Open daarna bijvoorbeeld http://localhost:8731/renders/a-calculator.html
De pagina rendert de scène; `window.exportAll()` stuurt de webp-bestanden
per POST naar /save, en deze server schrijft ze naar fotos/renders/.
"""
import base64
import http.server
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOEL = os.path.join(ROOT, "fotos", "renders")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_POST(self):
        if self.path != "/save":
            self.send_error(404)
            return
        lengte = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(lengte))
        naam = os.path.basename(body["name"])
        if not naam.endswith(".webp"):
            self.send_error(400, "alleen .webp")
            return
        data = body["data"].split(",", 1)[-1]
        os.makedirs(DOEL, exist_ok=True)
        pad = os.path.join(DOEL, naam)
        with open(pad, "wb") as f:
            f.write(base64.b64decode(data))
        antwoord = json.dumps({"ok": True, "path": pad, "bytes": os.path.getsize(pad)}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(antwoord)))
        self.end_headers()
        self.wfile.write(antwoord)


if __name__ == "__main__":
    poort = int(sys.argv[1]) if len(sys.argv) > 1 else 8731
    http.server.ThreadingHTTPServer(("127.0.0.1", poort), Handler).serve_forever()

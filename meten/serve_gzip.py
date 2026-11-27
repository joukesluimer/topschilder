# Statische server met gzip voor tekst (zoals GitHub Pages)
import http.server, gzip, os, sys, functools
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path): path = os.path.join(path, "index.html")
        ext = os.path.splitext(path)[1]
        if ext in (".html", ".css", ".js", ".svg", ".json", ".xml") and os.path.isfile(path) and "gzip" in self.headers.get("Accept-Encoding", ""):
            data = gzip.compress(open(path, "rb").read(), 6)
            self.send_response(200); self.send_header("Content-Type", self.guess_type(path))
            self.send_header("Content-Encoding", "gzip"); self.send_header("Content-Length", str(len(data))); self.end_headers()
            import io; return io.BytesIO(data)
        return super().send_head()
http.server.ThreadingHTTPServer(("127.0.0.1", int(sys.argv[2])), functools.partial(H, directory=sys.argv[1])).serve_forever()

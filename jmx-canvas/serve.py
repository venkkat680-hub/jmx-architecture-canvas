import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

port = 5000
print(f"Serving JMX Canvas on port {port}")
http.server.HTTPServer(("0.0.0.0", port), Handler).serve_forever()

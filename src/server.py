from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthcheck":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello World".encode("utf-8"))


def main():
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "7860"))

    server = HTTPServer((host, port), Handler)
    print(f"listening on {host}:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST_NAME = "localhost"
PORT = 8080


class Handler(BaseHTTPRequestHandler):
    success_data = {
        "status": "running",
        "code": 200,
        "message": "Server is operational",
    }
    failure_data = {"error": "Endpoint not found"}

    def json_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/status":
            self.json_response(200, self.success_data)
        else:
            self.json_response(404, self.failure_data)

    def do_POST(self):
        self.json_response(404, self.failure_data)

    def do_PUT(self):
        self.json_response(404, self.failure_data)

    def do_PATCH(self):
        self.json_response(404, self.failure_data)

    def do_DELETE(self):
        self.json_response(404, self.failure_data)


if __name__ == "__main__":
    server = HTTPServer((HOST_NAME, PORT), Handler)
    print(f"Server started http://{HOST_NAME}:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped")

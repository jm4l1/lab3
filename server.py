from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

PORT = 8080

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        if self.path == '/favicon.ico':
            return
        resource = 'index.html' if self.path == '/' else self.path
        with open(f"public/{resource}", 'r') as html_file_reader:
            file_lines = html_file_reader.read()
            self.wfile.write(bytes(file_lines, 'utf8'))

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        message = {
            'response': "Hello " + post_body['name'],
            'date': datetime.now().strftime('%A %d, %B %Y')
        }
        self.wfile.write(bytes(json.dumps(message), "utf8"))

    def do_DELETE(self):
        self.send_response(403)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        message = "<body><div>The DELETE method is forbidden on this server.</div><body>"
        self.wfile.write(bytes(message, "utf8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
        self.end_headers()

with HTTPServer(('', PORT), handler) as server:
    print(f"Server is running")
    server.serve_forever()











from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime
# Specify a port value for your server
PORT = 8080


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # set response code
        self.send_response(200)
        self.end_headers()
        if self.path == '/favicon.ico':
            return
        resource = 'index.html' if self.path == '/' else self.path
        with open(f"public/{resource}", 'r') as html_file_reader:
            file_lines = html_file_reader.read()
            self.wfile.write(bytes(file_lines, 'utf8'))

    def do_POST(self):
        # read content length header
        content_len = int(self.headers.get('Content-Length'))
        # get content-body
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        # set response code
        self.send_response(200)
        # set headers
        self.send_header('content-type', 'application/json')
        self.end_headers()

        # set data
        message = {}
        message['response'] = "hello " + post_body['name']
        message['date'] = datetime.now().strftime("%A %d, %B %Y")

        self.wfile.write(bytes(json.dumps(message), "utf8"))

    def do_PUT(self):
        # set response code
        self.send_response(405)

        # set headers
        self.send_header('content-type', 'text/html')
        self.end_headers()

        message = "<body><div>Method Not allowed </div><body>"
        self.wfile.write(bytes(message, "utf8"))

    # implement handler for DELETE here
    def do_DELETE(self):
        self.send_response(403)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        # set data
        message = {}
        message['response'] = "You cannot do that"

        self.wfile.write(bytes(json.dumps(message), "utf8"))


with HTTPServer(('', PORT), handler) as server:
    # add log to say server is running
    print("Server is running")
    server.serve_forever()

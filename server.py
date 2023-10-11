from http.server import BaseHTTPRequestHandler, HTTPServer
import json
# Specify a port value for your server
PORT = 8080


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # set response code
        self.send_response(200)

        # set headers
        self.send_header('content-type', 'text/html')
        self.end_headers()

        # set data
        message = "<body><div>Hello, SWEN2003</div><body>"
        self.wfile.write(bytes(message, "utf8"))

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

        self.wfile.write(bytes(json.dumps(message), "utf8"))

    def do_PUT(self):
        # set response code
        self.send_response(405)

        # set headers
        self.send_header('content-type', 'text/html')
        self.end_headers()

        message = "<body><div>Method Not allowed </div><body>"
        self.wfile.write(bytes(message, "utf8"))


with HTTPServer(('', PORT), handler) as server:
    server.serve_forever()

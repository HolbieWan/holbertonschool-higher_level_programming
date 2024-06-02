#!/usr/bin/python3
"""Module compiled with Python3"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Defines the subclass SimpleHTTPRequestHandler,
    that inherites from BaseHTTPRequestHandler"""
    def do_GET(self):
        """Method that override the GET method, handles various endpoints"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode('UTF-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('UTF-8'))
        else:
            self.send_response(404)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')


if __name__ == "__main__":
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    print("serving at port", 8000)
    httpd.serve_forever()
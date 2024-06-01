#!/usr/bin/python3
"""Creating a simple server Module"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class CustomRequestHandler(BaseHTTPRequestHandler):
    """custom Handler subclass for server requests"""

    def do_GET(self):
        """Method to set custom responses for the get requests """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sample_info = {
                "version": "1.0",
                "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(sample_info).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found'")


if __name__ == "__main__":
    PORT = 8000
    Handler = CustomRequestHandler

    httpd = HTTPServer(('', 8000), Handler)
    print("serving at port", 8000)
    httpd.serve_forever()

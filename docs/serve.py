#!/usr/bin/env python3
"""HTTPS server for local PWA testing on LAN devices."""
import http.server
import ssl
import os
import subprocess
import sys

PORT = 8080
CERT = "cert.pem"
KEY = "key.pem"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists(CERT) or not os.path.exists(KEY):
    print("Generating self-signed certificate...")
    subprocess.run([
        "openssl", "req", "-x509", "-newkey", "rsa:2048",
        "-keyout", KEY, "-out", CERT,
        "-days", "365", "-nodes",
        "-subj", "/CN=flashcards"
    ], check=True)

server = http.server.HTTPServer(("0.0.0.0", PORT), http.server.SimpleHTTPRequestHandler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(CERT, KEY)
server.socket = ctx.wrap_socket(server.socket, server_side=True)

print(f"Serving HTTPS on https://0.0.0.0:{PORT}/")
print(f"On your phone, open: https://<your-lan-ip>:{PORT}/")
print("Accept the certificate warning to install the PWA.")
server.serve_forever()

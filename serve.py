import http.server
import socketserver
import os

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

socketserver.TCPServer.allow_reuse_address = True

# make sure we're in this dir
old = os.getcwd()
try:
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
except KeyboardInterrupt:
    print('Bye')
finally:
    os.chdir(old)

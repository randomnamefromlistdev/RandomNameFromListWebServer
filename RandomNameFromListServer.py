from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import simplejson
import random
from StringIO import StringIO as IO

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("index.html", "r")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def _write_and_save_response(self,data):
        self.response = data
        self.wfile.write(data) 

    def get_response(self):
        return self.response

    def do_POST(self):
        self._set_headers()
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = simplejson.loads(self.data_string)
        print "{}".format(data)
        names = data['names']
        print "{}".format(names)
        random_name = random.choice(names)
        self.send_response(200)
        self.end_headers()
        self._write_and_save_response(simplejson.dumps(random_name))
        return

def test_handler( request_text ):
    class MockRequest(object):

        def __init__(self,request_text):
            self.request_text = request_text
        
        def makefile(self, *args, **kwargs):
            test_string = ('POST / HTTP/1.1\r\n'
                           'Host: www.example.com\r\n'
                           'Content-Type: application/json; charset=utf-8\r\n'
                           'Content-Length: ' + str(len(self.request_text)) + '\r\n'
                           '\r\n'
                            )
            test_string = test_string + self.request_text
            return IO(test_string)

    class MockServer(object):
        def __init__(self, ip_port, Handler, request_text):
            self.handler = Handler(MockRequest(request_text), ip_port, self) 

        def get_response(self):
            return self.handler.get_response()

    server = MockServer(('0.0.0.0', 8888), S, request_text)
    return server.get_response()

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

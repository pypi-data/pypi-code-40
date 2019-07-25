import os
import sys
import threading
from threading import Lock

PY2 = sys.version_info[0] == 2
if PY2:
    from SocketServer import BaseRequestHandler, TCPServer, ThreadingMixIn
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
else:
    from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
    from http.server import BaseHTTPRequestHandler, HTTPServer

TCPServer.allow_reuse_address = True

HOST = "127.0.0.1"
PORT_START = sys.version_info[0] * 10000 + sys.version_info[1] * 100

current_port = PORT_START
test_lock = Lock()


class OverpyBaseRequestHandler(BaseRequestHandler):
    def handle(self):
        for data in self.get_response(self):
            self.request.send(data)

    @staticmethod
    def get_response(self):
        yield b""


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


def read_file(filename, mode="r"):
    filename = os.path.join(os.path.dirname(__file__), filename)
    return open(filename, mode).read()


def new_server_thread(handle_cls, port=None):
    global current_port
    if port is None:
        test_lock.acquire()
        port = current_port
        current_port += 1
        test_lock.release()

    server = ThreadedHTTPServer(
        (HOST, port),
        handle_cls
    )
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    return (
        "http://%s:%d" % (HOST, port),
        server
    )


def stop_server_thread(server):
    server.shutdown()
    server.server_close()

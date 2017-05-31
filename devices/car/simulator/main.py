import SimpleHTTPServer
import SocketServer
import json
import socket

from devices.car.components.car.steering import get

pre_test = None
running = None


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print self.path

        if self.path == '/controllers':
            info_car = get()
            info_car['pre_test'] = pre_test
            info_car['running'] = running
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(info_car, ensure_ascii=False))
            print 'simulator getting new value'

        else:
            f = open('.' + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()

        return


class V6Server(SocketServer.TCPServer):
    address_family = socket.AF_INET6


def start_simulator():
    print('Server listening...')
    httpd = V6Server(('', 8080), Handler)
    httpd.serve_forever()


if __name__ == "__main__":
    start_simulator()
import SimpleHTTPServer
import SocketServer
import json
import socket
from time import sleep

from devices.car.components.car.steering import get

pre_test = None
running = None
httpd = None


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
            f = open('/home/pi/rv-project/devices/car/simulator/' + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()

        return


class V6Server(SocketServer.TCPServer):
    address_family = socket.AF_INET6


def start():
    global httpd
    print('Server listening...')
    httpd = V6Server(('', 8080), Handler)
    httpd.serve_forever()



def stop():
    print 'CLOSING HTTP SERVER'
    global httpd
    #httpd.shutdown()
    #httpd.server_close()
    sleep(0.5)
    httpd.socket.close()



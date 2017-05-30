import SimpleHTTPServer
import SocketServer
import json

from devices.car.components.car.steering import get
from devices.car.main import pre_test, running


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

        else:
            f = open('.' + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()

        return


print('Server listening...')
httpd = SocketServer.TCPServer(('', 8080), Handler)
httpd.serve_forever()

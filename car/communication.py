from socket import *
from time import *
from threading import Thread

port=4173

def recv():
    s=socket(AF_INET, SOCK_DGRAM)
    s.bind(('',port))
    while True:
        print "receiving..."
        data, address = s.recvfrom(5)
        print address
        print data
        if address != gethostname():
            print data



def send():
    s2=socket(AF_INET, SOCK_DGRAM)
    s2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s2.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    while True:
        print "sending..."
        s2.sendto("im alive", ("<broadcast>",port))
        sleep(5)




thread1 = Thread(target = recv, args = ())
thread1.start()
thread2 = Thread(target = send, args = ())
thread2.start()
send()

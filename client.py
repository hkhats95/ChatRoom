import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = '127.0.0.1'
s.connect((addr, 5555))

def sendMsg():
    while True:
        s.send(bytes(input(""), 'utf-8'))

ithread = threading.Thread(target=sendMsg)
ithread.daemon = True
ithread.start()

while True:
    data = s.recv(2048)
    if not data:
        break
    print(data.decode('utf-8'))

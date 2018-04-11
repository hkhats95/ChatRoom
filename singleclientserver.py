import socket
import sys
import threading
import time

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(1)

def sendMsg(conn):
    while True:
        conn.send(bytes('server: '+input(""), 'utf-8'))

conn, addr = s.accept()
print('connected to: '+addr[0]+':'+str(addr[1]))
conn.send(str.encode('welcome, to the chat room'))
conn.send(str.encode('Enter Q to disconnect'))

ithread = threading.Thread(target=sendMsg, args=(conn,))
ithread.daemon = True
ithread.start()

while True:
    data = conn.recv(2048)
    d = data.decode('utf-8')
    if d=="Q":
        print('disconnected to: ' + addr[0] + ':' + str(addr[1]))
        conn.close()
        break
    print("client: " + data.decode('utf-8'))
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

s.listen(5)

connections = []

def threaded_client(conn, addr):
    global connections
    conn.send(str.encode('welcome, to the chat room'))
    for c in connections:
        c[0].send(str.encode(str(addr[0]) + " is connected to the chat room."))
    connections.append((conn, addr[0]))

    while True:
        data = conn.recv(2048)
        d = data.decode('utf-8')
        if d=="Q" or not data:
            connections.remove((conn, addr[0]))
            conn.close()
            for c in connections:
                c[0].send(str.encode(str(addr[0]) + " disconnected from the chat room."))
            print('disconnected to: '+addr[0]+':'+str(addr[1]))
            break
        da = str(addr[0])+": "+d

        for c in connections:
            if(c[0]!=conn):
                c[0].send(str.encode(da))

while True:
    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))
    cthread = threading.Thread(target=threaded_client, args=(conn, addr))
    cthread.daemon = True
    cthread.start()

import socket
import sys
import time

# simple echo client/server

IP = "192.168.43.41"
PORT = 5050

def create_server():
    addr = (IP, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(addr)
    server.listen(1)
    print("server is running...")
    conn, client_addr = server.accept()
    with conn:
        print('Connected by', client_addr)
        while True:
            data = conn.recv(5)
            print("recieved data from client -> " + str(data))
            # if not data: break
            conn.sendall(data)


def create_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        while True:
            s.sendall(b'Hello, world')
            data = s.recv(1024)
            print("recieved data from server: " + str(data))
            time.sleep(1)            


command = sys.argv[1]

if command == "c":
    create_client()
elif command == "s":
    create_server()
else:
    print("command is not known!")


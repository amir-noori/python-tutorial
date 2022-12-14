
import socket
import sys
import json
from json.decoder import JSONDecodeError

# simple echo client/server

IP = "192.168.43.41"
PORT = 5050


class StopServer(Exception):
    pass

def create_server():
    addr = (IP, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(addr)
    server.listen(1)
    print("server is running...")
    while True:
        conn, client_addr = server.accept()
        try:
            with conn:
                print('Connected by', client_addr)
                while True:
                    data = conn.recv(1024)
                    print("recieved data from client -> " + str(data))
                    # parse json string to object
                    
                    json_data = {}
                    result = ""

                    try:
                        result = handle_request(json.loads(data))
                    except JSONDecodeError as e:
                        # this exception handler is for malformed json requests
                        print(f"malfored request -> {e}")
                        result = b'{"resultCode": -2, "resultMessage": "bad request"}'
                    except StopServer:
                        print("stopping the server")
                        result = b'{"resultCode": 0, "resultMessage": "stopping"}'
                        conn.sendall(result)
                        return
                    conn.sendall(result)
        except ConnectionAbortedError as e:
            pass
        

def handle_request(json_data):
    command = json_data['command']
    if command == "hello":
        result = b'{"resultCode": 0, "resultMessage": "hi"}'
    elif command == "calculate":
        body = json_data["body"]
        # b'{"resultCode": 0, "resultMessage": "' + bytes(str(eval(body)), 'ascii') + '"}', 'ascii'
        result = bytes('{"resultCode": 0, "resultMessage": "' \
            + str(eval(body)) + '"}', 'ascii')
    elif command == "stop":
        raise StopServer
    else:
        result = b'{"resultCode": -1, "resultMessage": "command is not known!"}'
    return result


def create_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))

        # # correct command    
        # s.sendall(b'{"command": "hello"}')
        # data = s.recv(1024)
        # print("recieved data from server: " + str(data))

        # # unkown command
        # s.sendall(b'{"command": "test"}')
        # data = s.recv(1024)
        # print("recieved data from server: " + str(data))

        # # malformed request
        # s.sendall(b'{"command "test"}')
        # data = s.recv(1024)
        # print("recieved data from server: " + str(data))
          
        # # malformed request
        # s.sendall(b'{"command": "calculate", "body": "2 + 2"}')
        # data = s.recv(1024)
        # print("recieved data from server: " + str(data))

        request_list = [
            '{"command": "hello"}', 
            '{"command": "test"}',
            '{"command "test"}',
            '{"command": "calculate", "body": "2 + 2"}',
            '{"command": "stop"}'
        ]

        for req in request_list:
            s.sendall(bytes(req, 'ascii'))
            data = s.recv(1024)
            print("recieved data from server: " + str(data))


command = sys.argv[1]

if command == "c":
    create_client()
elif command == "s":
    create_server()
else:
    print("command is not known!")


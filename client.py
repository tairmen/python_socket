import socket
import time
import json

HOST = '35.204.109.8'  # The server's hostname or IP address
PORT = 3001        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    token = ""
    for i in range(4):
        send_data = ''
        send_bytes = b''
        if i == 0:
            send_data = '{"data": "Hello, world"}'
            send_bytes = send_data.encode()
        if i == 1:
            send_data = '{"auth": {"id": 8}}'
            send_bytes = send_data.encode()
        if i == 2:
            send_data = '{"data": "ABVGD"}'
            send_bytes = send_data.encode()
        if i == 3:
            send_data = '{"token": "' + token + '", "data": "ABVGD"}'
            send_bytes = send_data.encode()
        s.sendall(send_bytes)
        data = s.recv(1024)
        try:
            json_data = json.loads(data)
            if 'token' in json_data.keys():
                token = json_data["token"]
        except NameError:
            print("Received not json")
        print('Sended', repr(send_data))
        print('Received', repr(data))
        time.sleep(3)

    while 1:
        data = s.recv(1024)
        print('Received', repr(data))


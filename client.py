import socket
import time
import json

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 3001        # The port used by the server

class Hub:
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        self.s = sock
        self.on_listen = True
            
    
    def send_data(self, data):
        str_data = ""
        if type(data) == str:
            str_data = '"' + data + '"'
        else:
            str_data = str(data)
        send_data = '{"data": ' + str_data
        if self.token is not None:
            send_data += ', "token": "' + self.token + '"}'
        else:
            send_data += '}'
        self.send(send_data)

    def send_auth(self, id):
        str_data = str(id)
        send_data = '{"auth": {"id": ' + str_data + '}}'
        self.send(send_data)

    def send(self, str_data):
        send_bytes = str_data.encode()
        self.s.sendall(send_bytes)
        print('Sended', repr(str_data))
        self.__listen()


    def listen(self):
        while self.on_listen:
            self.__listen()
            

    def __listen(self):
        data = self.s.recv(1024)
        print('Received', repr(data))
        try:
            json_data = json.loads(data)
            if 'data' in json_data.keys():
                self.send_data("SAFFSASAF")
            if 'token' in json_data.keys():
                self.token = json_data["token"]
        except NameError:
            print("Received not json")
        


client = Hub()
time.sleep(1)
client.send_auth(8)
time.sleep(3)
client.send_data("SAFFSASAF")
client.listen()



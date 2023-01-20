import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444

clientsocket.connect((host, port))

## we can limit the sata we're getting sent - this is the max amount
message = clientsocket.recv(1024)

## we don't want to create a loop - we now need to decode the message
clientsocket.close()

print(message.decode('ascii'))
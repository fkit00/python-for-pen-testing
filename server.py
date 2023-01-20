## need to import socket module, we need to make an object that will call the socket function
##socket.sock and we use AFInet - this spesifcy the protcol 
## we are using bind to bind port and host to a socket
## we have send and recive methods and close which lets us close the socket 

import socket

server_socket = socket.socket(
    socket.AF_INET# af-INET means we can ocommunicate with ipv4
    , socket.SOCK_STREAM # this means it;s a TCP rather than UDP
)

host = socket.gethostname() ## it gets the ip adress, might throw error for windows
port = 444

## we need to bind the object - the server_socket

server_socket.bind((host, port))

server_socket.listen(1) ## i only want to listen from one 

while True: 
    clientsocket, address = server_socket.accept() ## this will accept the info coming from the client
    print(" recived connection from %s" % str(address))
    message = "Thank you for connecting to the server" +"\r\n"
    
## we haven't sent any data back yet!!!
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()

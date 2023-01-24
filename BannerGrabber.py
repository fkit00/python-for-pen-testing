## laying out the logic 

import socket 
## we want user to enter ip adresss and port 
s = socket.socket()

ip = input ("Please enter the IP: ")
port = str(input("Please enter the port: "))

s.connect((ip, int(port)))
print(s.recv(1024))  ## calling the recive and we're going to limit it to a certain number of bytes
## laying out the logic 

import socket 
## we want user to enter ip adresss and port 
#s = socket.socket()
#ip = input ("Please enter the IP: ")
#port = str(input("Please enter the port: "))
#s.connect((ip, int(port)))
#print(s.recv(1024))  ## calling the recive and we're going to limit it to a certain number of bytes

## re-write in a function 


def banner(ip,port):
    s= socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(str(s.recv(1024)).strip('b')) ## this strip uncessary output the b but this might cause some funkiness later on 


def main():
    ip = input ("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip,port)


main()    
  
import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## ipv4, sockstream spesifies the type of connection TCP not UDP
s.settimeout(5)

host = input ("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you would like to scan: "))



def portScanner(port): 
    if s.connect_ex((host, port)):## this will terminate if port is closed
           print("This port is closed")
    else:
        print("The port is open")   

portScanner(port)
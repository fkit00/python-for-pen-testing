import nmap

scanner = nmap.PortScanner()
print("Hi, here's a simple nmap automation tool")
print("<--------------------------------------->")

ip_addr = input("Please etnter the IP address you would like to scan:")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

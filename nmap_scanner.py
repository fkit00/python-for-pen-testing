import nmap

scanner = nmap.PortScanner()
print("Hi, here's a simple nmap automation tool")
print("<--------------------------------------->")

ip_addr = input("Please etnter the IP address you would like to scan:")
print("The IP you entered is: ", ip_addr)
type(ip_addr)
resp = input("""\nPlease enter the type of scan you want to run:
1) SYN ACK Scan
2)UDP Scan 
3)Comprehensive Scan \n
""")
print("You have selection option: ", resp)

if resp == '1':
    print("Nmap Verions: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')    #we want to verbose the output, and -sS means syn ack
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state)
    print(scanner[ip_addr].all_protocols())
    print("Open ports", scanner[ip_addr]['tcp'].keys()) ## this will return all the active ports 
elif resp == '2':
    print("Nmap Verions: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')    #we want to verbose the output, and -sS means syn ack
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state)
    print(scanner[ip_addr].all_protocols())
    print("Open ports", scanner[ip_addr]['udp'].keys()) ## this will return all the active ports 
elif resp == '3':
    print("Nmap Verions: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')    #we want to verbose the output, and -sS means syn ack
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state)
    print(scanner[ip_addr].all_protocols())
    print("Open ports", scanner[ip_addr]['tcp'].keys()) ## this will return all the active ports 
else:
    print("Please enter a valid option")
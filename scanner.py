#!/usr/bin/env python
import socket
import sys
from datetime import datetime
import time

#function that scans the desired host
def scan_host(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = sock.connect_ex((ip, port)) #more efficient than connect()
        sock.close()

    except socket.gaierror:
        print("[+] Hostname could not be resolved to IP. Exiting ...")

    except socket.error:
        print("[+] Couldn't connect to server ...")

    return conn

#get input from user
try:
    host = input("[+] Enter Target Host Address: ")

except KeyboardInterrupt: # Ctrl + C
    print("\n\n[+] Interrupt Requested.")
    print("[+] Leaving Your Ass ...") # fuck them, right?
    sys.exit()

#display hosts corresponding ip
host_ip = socket.gethostbyname(host)
print("\n[+] Host: %s IP: %s" % (host, host_ip))
print("[+] Scanning Has Commenced At %s ..." % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

#scan through all possible ports
for port in range(1, 65536):
    try:
        response = scan_host(host_ip, port)
        if response == 0:
            print("[+] Port %d: Open" % (port))

    except Exception:
        pass #just keep swimming

    except KeyboardInterrupt: # Ctrl + C
        print("\n\n[+] Interrupt Requested.")
        print("[+] Leaving Your Ass ...") # fuck them, right?
        sys.exit()

#calculate duration of scan and exit
stop_time = datetime.now()
duration = stop_time - start_time
print("\n[+] Scanning Finished At %s ..." % (stop_time))
print("[+] Duration: %s" % (duration))
print("[+] Merry Christmas ya filthy animal! ;)")
sys.exit()

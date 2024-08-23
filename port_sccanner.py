#!/usr/bin/python3

import socket
import sys
import sys
import threading

usage = "python3 port_scanner Target Start_port End_port"

print("+"*10)
print("Port Scanning")
print("+"*10)

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning...")


def scan_port(port):
    # print("Scanning port: ", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect_ex((target, port))
    if(not connect):
        print("port {} is open".format(port))
    else:
        print("The port number {} is close!!".format(port))
    s.close()


for port in range(start_port, end_port+1):
    thread = threading.Thread(target=scan_port, args=(port, ))
    thread.start()

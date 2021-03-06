#!/usr/bin/env python3

import socket
import time
time.sleep(1)
print("Hello world!")
print("Terminal Based LAN Chat 1.3 (Client)")
hostip = str(input("Enter the server IP. Type 0 to use a hardcoded value. (Usually localhost.)"))
if(hostip == 0):
    HOST = "127.0.0.1"
else:
    HOST = hostip

print("Connecting to server... (If server does not connect before an automatic timeout, the process will quit.)")
print("TURN ON SERVER NOW.")
time.sleep(15)
HOST = "127.0.0.1" # The server's hostname or IP address
PORT = 65432        # The port used by the server
print("\n")
print("\n")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server. Waiting to recive a message...")
    while True:
         data = s.recv(1024)
         if(len(data) != 0):
             print('Received', repr(data))
             x = input("Press 0 to quit. Press 1 to continue.")
             if(x == 1):
                 continue
             else:
                 break

            
             


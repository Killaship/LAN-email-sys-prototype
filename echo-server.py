#!/usr/bin/env python3

import socket

HOST = 'YOUR_IP'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
             
             string = input("Please enter email message.")  #this message should eventually make it to the client program, whether it be over LAN or 2 separate programs on a computer.

             arr = bytes(str(string), 'utf-8')
             conn.sendall(arr) #sending the bytes from the string
             data = conn.recv(1024)
             if not data: #idk what this is for but it looks important
                 conn.sendall(data)
                 break
                

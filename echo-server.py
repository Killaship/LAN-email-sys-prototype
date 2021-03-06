#!/usr/bin/env python3
def server():


 

     import socket
     import time
     time.sleep(1)
     print("Hello world!")
     print("Terminal Based LAN Chat 1.3 (Server)")
     hostip = str(input("Enter the host IP. Type 0 to use a hardcoded value. (Usually localhost.)"))
     if(hostip == 0):
         # Hardcoded value goes here.
         HOST = "127.0.0.1"
     else:
         HOST = hostip
     print("Waiting for client to connect...")
     HOST = "127.0.0.1"
     PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.bind((HOST, PORT))
         s.listen()
         conn, addr = s.accept()
     with conn:
         print('Connected by', addr)
         print("Tip: You can send up to 30 messages in a single session.")
         print("If you don't want that, just try to send 'quit' as a message.")
    
        # I WAS BEING LAZY DON'T @ ME!
        
         while True:
         #You can send up to 30 messages in a session.
             #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
             #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
             #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
             #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
             #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
             #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
            #things 
             string = input("Please enter email message.")
             if(string == 'quit'):
                 break
             else:
                 arr = bytes(str(string), 'utf-8')
                 conn.sendall(arr)
             


server()







# Wow, you made it to the bottom of the world. This code has as many lines as the 1.2 version of VoltOS!

#!/usr/bin/env python

import socket

# IP of serving computer
HOST = '127.0.0.1' #'169.254.207.114'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# HOST = socket.gethostname()
s.connect((HOST, PORT))

s.send(bytes('RGB 0 255 0', 'ascii'))
print("message sent")

#msg = s.recv(1024)
# print(msg.decode("utf-8"))
#!/usr/bin/env python

import socket
import sys

# IP of serving computer
HOST = '192.168.86.20' #'127.0.0.1' #'169.254.207.114'
PORT = 1234

# Connect to TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# format message from command line arguments
arguments = sys.argv
message = ''
i = 1
while i < len(arguments):
    message += arguments[i] + ' '
    i += 1
message = message[:-1]

# send the message
s.send(bytes(str(message), 'ascii'))
print("message sent: " + message)

#!/usr/bin/env python


import argparse
import socket
import time

parser = argparse.ArgumentParser(description='Send commands to light strips', usage="SendLightCommand HostAdress LightColor [options]")

parser.add_argument('HostAddress', action='store', type=str)
parser.add_argument('LightColor', choices=['red', 'green', 'blue'])

parser.add_argument('--addAddress', '-A', action='append')
parser.add_argument('--SetPort', '-P', action="store")
parser.add_argument('--Verbose', '-V', action='store_true')

args = parser.parse_args()

# combine the required and optional IP addresses into a single string
ipAddresses = args.addAddress
ipAddresses.insert(0, str(args.HostAddress))

if args.Verbose:
    if      len(ipAddresses) > 1: print("Connecting to hosts:")
    else:   print("Connecting to host:")
    for HOST in ipAddresses:
        print(HOST)

PORT = 1234
if args.SetPort is not None: PORT = int(args.SetPort)

print("Connecting to host using port: " + str(PORT))

message = str(args.LightColor)

if args.Verbose: print("Sending message: " + message)



## SOMETHING SEEMS TO BE GONG WRONG WITH THE EXCEPTIONS, SOCKETS, AND LOOP
i = 0
while i < len(ipAddresses):
    HOST = ipAddresses[i]
    try:
        # Connect to TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        # send the message
        s.send(bytes(str(message), 'ascii'))
        print("message sent: " + message)
    except:
        print("Cannot send command to host: " + HOST)
        s.close()
    i += 1
    
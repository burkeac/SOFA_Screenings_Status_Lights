#!/usr/bin/env python

import socket


def setLightColors(R, G, B):
    # program lights using 

    if 0 > R or R > 255 or 0 > G or G > 255 or 0 > B or B > 255: 
        print("invalid code value in setLightColors()")
    else:
        print(R, G, B)


# IP of computer trying to reach.
PORT = 1234
HOST = '127.0.0.1' #'129.21.144.71'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connection Established!")
    # clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    msg = clientsocket.recv(1024)
    
    #print("msg: " + msg.decode('ascii'))

    decodedMSG = msg.decode('ascii')

    if decodedMSG == 'Film Begin':
        # set lights to red
        setLightColors(255, 0, 0)
        print("lights set to red status")

    elif decodedMSG == 'Film End':
        # set lights to yellow
        setLightColors(255, 255, 0)
        print("lights set to yellow status")

    elif decodedMSG == 'Intermission':
        # set lights to green
        setLightColors(0, 255, 0)
        print("lights set to green status")

    elif decodedMSG == 'Starting Soon':
        # set lights to blue
        setLightColors(0,0,255)
        print("lights set to blue status")

    elif decodedMSG == 'No Status':
        # set lights to off
        setLightColors(0,0,0)
        print('lights set to off')

    elif decodedMSG[:3] == 'RGB':
        splitString = decodedMSG.split()
        try:
            setLightColors(int(splitString[1]), int(splitString[2]), int(splitString[3]))
        except:
            print("Can not determin RGB values")

    else: print("No state for message: " + decodedMSG)
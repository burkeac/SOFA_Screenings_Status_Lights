#!/usr/bin/env python

import socket
from gpiozero import LED
import subprocess

# this calls a subprocess to get the IP address of the PI 
Subout = subprocess.Popen(['hostname','-I'], stdout=subprocess.PIPE)

IP = str(Subout.communicate()[0])[2:][:-4]


R = LED(2)
G = LED(3)
B = LED(4)

# at start of program, turn lights off
R.off()
G.off()
B.off()

# IP of computer trying to reach.
PORT = 1234
HOST = IP # get IP from above bash exec or can use something like: '192.168.86.20'

print('Socket open at: ' + HOST + ' on port: ' + str(PORT))

#genrate and bind socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	msg = clientsocket.recv(1024)
	decodedMSG = msg.decode('ascii')

	if decodedMSG == 'Film Begin':
		# set lights to red
		G.off()
		B.off()
		R.on()

		print("lights set to red status")

	elif decodedMSG == 'Film End':
		# set lights to yellow
		B.off()
		R.on()
		G.on()
		print("lights set to yellow status")

	elif decodedMSG == 'Intermission':
		# set lights to green
		B.off()
		G.on()
		R.off()
		print("lights set to green status")

	elif decodedMSG == 'Starting Soon':
		# set lights to blue
		G.off()
		R.off()
		B.on()
		print("lights set to blue status")

	elif decodedMSG == 'No Status':
		# set lights to off
		R.off()
		G.off()
		B.off()
		print('lights set to off')

	else: print("No state for message: " + decodedMSG)

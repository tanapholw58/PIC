#!/usr/bin/env python

import socket
import base64

file = "Pic.jpg"
bytes1 = open(file,'rb').read() #��ҹ���亵�
bytes1 = base64.b64encode(bytes1) #������� base64

TCP_IP = '127.0.0.1'
TCP_PORT = 5011
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes1)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data

#!/usr/bin/env python

import socket
import base64
import os



TCP_IP = '127.0.0.1'
TCP_PORT = 5011
BUFFER_SIZE = 1024000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
os.mkdir('image_from_client')
myfile = open('image_from_client/ABC.jpg', 'wb') #�Դ��������¹���
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    data = base64.b64decode(data) #�ʹ���� base64
    myfile.write(data) #��Ң�����ŧ���
    myfile.close() #�Դ���
    
conn.close()

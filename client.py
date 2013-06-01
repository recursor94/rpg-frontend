import socket
import os
import sys

s = socket.socket()
host = socket.gethostname()
port = 9001

s.connect((host,port))

while 1:
    s.send("Hello\n")
    print s.recv(1024)
s.close()

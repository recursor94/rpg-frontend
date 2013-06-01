import socket
import os
import sys
import string

backsock = socket.socket() # socket to connect to the web back end
backhost = os.environ['HOSTNAME']
backport = 9001

backsock.connect((backhost,backport))

# Socket to connect
ircsock = socket.socket()
irc

while 1:
    s.send('Hello\n')
    print s.recv(1024)
s.close()

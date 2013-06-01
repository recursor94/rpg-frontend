import socket
import os
import sys
import string


backsock = socket.socket() # socket to connect to the web back end


def init_server_connection ():
    "Connects client bot to back-end server"

    backhost = os.environ['HOSTNAME']
    backport = 9001

    backsock.connect((backhost,backport))




while 1:
    readbuffer=readbuffer+ircsock.recv(1024)
    temp=string.split(readbuffer,"\n")
    readbuffer=temp.pop()

for line in temp:
    line=string.rstrip(line)
    line=string.split(line)

    if(line[0]=="PING"):
      ircsock.send("PONG %s\r\n" % line[1])


    #while 1:
    #backsock.send('Hello\n')
    #print backsock.recv(1024)

    #backsock.close()

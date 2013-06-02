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


    #while 1:
    #backsock.send('Hello\n')
    #print backsock.recv(1024)

    #backsock.close()

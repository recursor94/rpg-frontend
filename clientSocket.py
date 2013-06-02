import socket
import os
import sys
import string

backsock = socket.socket() # socket to connect to the web back end


def connect_to_server ():
   """Connects client bot to back-end server"""

    backhost = os.environ['HOSTNAME']
    backport = os.environ['PORT']

    backsock.connect((backhost,backport))


    #while 1:
    #backsock.send('Hello\n')
    #print backsock.recv(1024)
def close_connection():
    backsock.close()

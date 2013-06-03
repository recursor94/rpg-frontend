import socket
import os
import sys
import string


class BackEndConnection:
    """
    Class to handle socket connection to the web server
    """


    def __init__(self, hostname, port):
        self.backsock = socket.socket() # socket to connect to the web back end
        self.backsock.connect((hostname, port))

    def sendMessage(self,message):
        self.backsock.send(message)

    def closeConnection(self):
        backsock.close()

    def register(self, username):  #Register username in server
        self.sendMessage("register " + username + "\n")
        return self.backsock.recv(1024)

    

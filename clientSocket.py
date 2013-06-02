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

    def close_connection(self):
        backsock.close()

import socket
import os
import sys
import string


class BackEndConnection:
    """
    Class to handle socket connection to the web server
    """
    self.backsock = socket.socket() # socket to connect to the web back end

    def __init__(self, hostname, port):
        self.backsock.connect((hostname, port))

    def close_connection():
        backsock.close()

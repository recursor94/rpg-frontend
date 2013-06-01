import socket
import os
import sys
import string

readbuffer=""
backsock = socket.socket() # socket to connect to the web back end
ircsock = socket.socket() # socket to connect to irc channel

def init_server_connection ():
    "Connects client bot to back-end server"

    backhost = os.environ['HOSTNAME']
    backport = 9001

    backsock.connect((backhost,backport))

def init_irc_connection ():
    irchost = "mccs.stu.marist.edu"
    ircport = 6667
    NICK="battle-bot"
    IDENT="battle-bot"
    REALNAME="Your Mom"
    CHAN="#chat"
    ircsock.connect((irchost,ircport))
    ircsock.send("NICK %s\r\n" % NICK)
    ircsock.send("USER %s %s bla :%s\r\n" % (IDENT, irchost,REALNAME))
    ircsock.send("JOIN:%s\r\n" % CHAN)
    ircsock.send("PRIVMSG %s:%s\r\n" % (CHAN, "This is a test message. Prepare for imminent mortal combat"))




    #while 1:
    #backsock.send('Hello\n')
    #print backsock.recv(1024)

    #backsock.close()

#!/usr/bin/python

#twisted imports
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log
import time, sys, os
import clientSocket

class MessageLogger:
    """
    An independent logger class
    """

    def __init__(self, file):
        self.file = file

    def log(self, message):
        """Writes a message to a file"""
        timestamp = time.strftime("[%H:%M:%S]", time.localtime(time.time()))
        self.file.write('%s %s\n' % (timestamp, message))
        self.file.flush()

    def close(self):
        self.file.close()


class BattleBot(irc.IRCClient):
    """An irc bot which should handle battles and rpg logic"""

    nickname = "doofy"
    backendConnection = clientSocket.BackEndConnection(os.environ['HOSTNAME'], int(os.environ['PORT']))
    
    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        self.logger = MessageLogger(open(self.factory.filename, "a"))
        self.logger.log("[connected at %s]" %
                        time.asctime(time.localtime(time.time())))

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self)
        self.logger.log("[disconnected at %s]" %
                        time.asctime(time.localtime(time.time())))
        self.logger.close()

p
    # callbacks for events

    def signedOn(self):
        """Called when bot has succesfully signed on to server"""
        self.join(self.factory.channel)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        self.logger.log("[I have joined %s]" % channel)

    def privmsg(self, user, channel, msg):
        """This will be called when the bot receives a message"""
        user = user.split('!', 1)[0]
        self.logger.log("<%s> %s" % (user, msg))

        #Check to se if they're sending me a private message
        if channel == self.nickname:
            msg = "Hello! I see that you've sent me a private message.\
            What would you like to discuss?"
            self.msg(user, msg)
            return

        # Otherwise check to see if it is a message directed at me
        elif msg.startswith(self.nickname + ":"):
            msg = "%s: I am a simple bot" % user
            self.msg(channel, msg)
            self.logger.log("<%s> %s" % (self.nickname, msg))

    def action (self, user, channel, msg):
        """This will get called when the bot sees someone perform an action."""
        user = user.split('!', 1)[0]
        self.logger.log("* %s %s" % (user, msg))

    #irc callbacks

    def irc_NICK(self, prefix, params):
        """Called when an IRC user changes his nickname."""
        old_nick = prefix.split('!')[0]
        new_nick = params [0]
        #self.logger.log("%s is now known as %s" % (old_nick, new_nick))
        #Previous line commented out because their is already a bot that performs
        #This kind of function


class BattleBotFactory(protocol.ClientFactory):
    """A factory for Battlebots.
    A new protocol instance will be created each time we connect to the server.
    """

    def __init__(self, channel, filename):
        self.channel = channel
        self.filename = filename

    def buildProtocol(self, addr):
        p = BattleBot()
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()


if __name__ == '__main__':
    #initialize logging

    log.startLogging(sys.stdout)
    # create factory protocol and application
    f = BattleBotFactory(sys.argv[1], sys.argv[2])
    reactor.connectTCP("mccs.stu.marist.edu", 6667, f)

    # run bot
    reactor.run()

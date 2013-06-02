import socket
import sys
import string

import twisted.words.protocols
import twisted.internet
import twisted.python


class Bot(irc.IRCClient):
    """A logging IRC bot."""

    nickname = "doof"

    def connectionMade(self):
        irc.IRCCLIENT.connectionMade(self)


    def connectionLost(self, reason):
        irc.IRCCLIENT.connectionLost(self, reason)



    # callbacks for events

    def signedOn(self):
        """Called when bot has sucessfully signed on to server."""
        self.join(self.factory.channel)

    def joined(self, channel):
        """This will be called when the bot joins the channel."""


    def privmsg(self, user. channel, msg):
        """This will be called when the bot receives a message."""
        user = user.split('!', 1)[0]
        s

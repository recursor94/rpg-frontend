readbuffer=""

ircsock = socket.socket() # socket to connect to irc channel


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

    while 1:
    readbuffer=readbuffer+ircsock.recv(1024)
    temp=string.split(readbuffer,"\n")
    readbuffer=temp.pop()

for line in temp:
    line=string.rstrip(line)
    line=string.split(line)

    if(line[0]=="PING"):
      ircsock.send("PONG %s\r\n" % line[1])

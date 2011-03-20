#!/usr/bin/python

import irclib

network="irc.oftc.net"
port=6667
nick="dinobot"
ident="pybot"
realname="Bot do Fabio"
channel="#sysadms"

irclib.DEBUG = True

irc = irclib.IRC()

server = irc.server()
server.connect( network, port, nick, ircname = realname )
server.join( channel )

server.privmsg( channel, 'Querida CHEGUEI!' )


irc.process_forever()

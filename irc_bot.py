#!/usr/bin/python

import socket

network="irc.oftc.net"
port=6667
nick="pyircbot"
ident="pybot"
realname="Bot do Fabio"
channel="#sysadms"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect(( network, port ))
print irc.recv(4096)
irc.send('nick '+nick+'\r\n')
irc.send('USER %s %s %s :Python IRC\r\n' % (ident, realname, ident))
irc.send('JOIN '+channel+'\r\n')

while 1:
    line=irc.recv(1024)
    print line
    if line.find('Welcome to the OFTC Internet Relay Chat Network') != -1:
        irc.send('JOIN '+channel+'\r\n')
    if line.find('PING') != -1:
        irc.send('PONG '+line[1]+'\r\n')

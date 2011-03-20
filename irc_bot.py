#!/usr/bin/python

import sys
import ConfigParser
import irclib


def handleJoin( connection, event ):
    IRC_Bot.__init__()
    nick = event.source().split('!')[0]
    but3k4_msg = "Papai mandou lembrancas"
    if nick.find('fabio') != -1 or nick.find('miguim') != -1:
        connection.privmsg( conf['channel'], 'nick but3k4_msg' )

class IRC_Bot:
    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read( 'conf/irc_bot.conf' )

        conf = {
                    'network': None,
                    'port': None,
                    'nick': None,
                    'username': None,
                    'ircname': None,
                    'channel': None,
                    'debug': None
        }

        for key in conf.keys():
            conf[key] = self.config.get( 'irc_bot', key )
 
        try:
#            irclib.DEBUG = conf['debug']
            irc = irclib.IRC()
            server = irc.server()
            server.connect( conf['network'], int(conf['port']), conf['nick'], username = conf['username'], ircname = conf['ircname'] )
            server.join( conf['channel'] )
        except Exception, ex:
            print "Xi cagou: %s" % ex
            sys.exit(1)
        irc.add_global_handler( 'join', handleJoin ) 
        irc.process_forever()

irc_bot = IRC_Bot()

#!/usr/bin/python
#
# importando os modulos que vou utilizar
import sys
import ConfigParser
import irclib
from modules import seen


config_file = 'conf/irc_bot.conf'

class IRC_Bot:
    def __init__(self, config):
        self.file = config

    def handleJoin(self, connection, event):
        nick = event.source().split('!')[0]
        joinlog = seen.action()
        joinlog.save( "%s %s" % ("Join: ", event.source()))
        #but3k4_msg = "Papai mandou lembrancas"
        #rsampaio_msg = "!neguinho"
        #if nick.find('but3k4') != -1 or nick.find('miguim') != -1:
        #    connection.privmsg(self.conf['channel'], '%s: %s' % (nick, but3k4_msg))
        #if nick.find('rsampaio') != -1:
        #    connection.privmsg(self.conf['channel'], '%s: %s' % (nick, rsampaio_msg))
    def handleLeave(self, connection, event):
        nick = event.source().split('!')[0]
        leavelog = seen.action()
        leavelog.save( "%s %s" % ("Part: ", event.source()))

    def run(self):
        self.conf = {
            'network': None,
            'port': None,
            'nick': None,
            'username': None,
            'ircname': None,
            'channel': None,
            'debug': None
        }

        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.file)

        for key in self.conf.keys():
            self.conf[key] = self.config.get('irc_bot', key)

        try:
            #irclib.DEBUG = conf['debug']
            irc = irclib.IRC()
            server = irc.server()
            server.connect(self.conf['network'], int(self.conf['port']), self.conf['nick'], username = self.conf['username'], ircname = self.conf['ircname'] )
            server.join(self.conf['channel'])
            irc.add_global_handler('join', self.handleJoin)
            irc.add_global_handler('leave', self.handleLeave)
        except Exception, ex:
            print "Xi cagou: %s" % ex
            sys.exit(1)
        irc.process_forever()

irc_bot = IRC_Bot(config_file)
irc_bot.run()

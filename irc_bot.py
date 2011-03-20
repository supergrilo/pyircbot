#!/usr/bin/python

import ConfigParser
import irclib

config = ConfigParser.RawConfigParser()
config.read('conf/irc_bot.conf')

conf = {
        'network': None,
        'port': None,
        'nick': None,
        'username': None,
        'ircname': None,
        'debug': None
}

for key in conf.keys():
    conf[key] = config.get('irc_bot', key)

try:
    irc = irclib.IRC()
    server = irc.server()
    server.connect( conf['network'], int(conf['port']), conf['nick'], username = conf['username'], ircname = conf['ircname'] )
except Exception, ex:
    print "Xi cagou: %s" % ex
        
irc.process_forever()

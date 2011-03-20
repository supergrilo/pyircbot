#!/usr/bin/python
#
# importando os modulos que vou utilizar
import sys
import ConfigParser
import irclib

config_file = 'conf/irc_bot.conf'

# Definindo a classe IRC_BOT
class IRC_Bot:

    # Definindo o metodo de inicializacao da classe
    # Ela recebe o argumento config que nada mais e
    # que o arquivo de configuracao que ele vai ler
    # e pegar os valores
    def __init__(self, config):

        # Atribuindo o conteudo do config para a variavel
        # self.file
        self.file = config

    # Definindo o metodo join que sera executada
    # toda vez que alguem entrar no irc
    # Apesar dela ser definida com argumentos,
    # ao chamada nao deve definir nenhum argumento pois
    # ela vai herdar da classe anterior
    def handleJoin(self, connection, event):

        # Pega o event.source e pega somente o nick 
        nick = event.source().split('!')[0]

        # Define a mensagem que sera enviada
        but3k4_msg = "Papai mandou lembrancas"

        # Se o nick for fabio ou o nick for miguim, ele manda 
        # a mensagem para o canal
        if nick.find('but3k4') != -1 or nick.find('miguim') != -1:
            connection.privmsg(self.conf['channel'], '%s: %s' % (nick, but3k4_msg))

        # Definindo o metodo run que sera chamado na hora de instanciar depois
        # de ter a classe IRC_Bot instanciada
    def run(self):

        # Definindo o dicionario para atribuir os valores que pego do arquivo
        # irc_bot.conf
        self.conf = {
            'network': None,
            'port': None,
            'nick': None,
            'username': None,
            'ircname': None,
            'channel': None,
            'debug': None
        }

        # Instanciando o configpaser 
        self.config = ConfigParser.RawConfigParser()

        # Lendo o arquivo self.file
        self.config.read(self.file)

        for key in self.conf.keys():
            self.conf[key] = self.config.get('irc_bot', key)

        try:
            #irclib.DEBUG = conf['debug']

            # Instanciando a classe IRC do modulo irclib
            irc = irclib.IRC()

            # Instanciando o metdo server do objeto irc 
            server = irc.server()

            # Conectando no irc usando o metodo conect do objeto server
            # E utilizando os valores do dicionario self.conf que leu
            # as configuracoes do arquivo self.file
            server.connect(self.conf['network'], int(self.conf['port']), self.conf['nick'], username = self.conf['username'], ircname = self.conf['ircname'] )
            server.join(self.conf['channel'])
            irc.add_global_handler('join', self.handleJoin)
        except Exception, ex:
            print "Xi cagou: %s" % ex
            sys.exit(1)
        irc.process_forever()

irc_bot = IRC_Bot(config_file)
irc_bot.run()

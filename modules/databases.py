#!/usr/bin/env python

import ConfigParser
from sqlalchemy import Column, DateTime, Integer, Unicode, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = ConfigParser.RawConfigParser()
config.read('conf/irc_bot.conf')

Base = declarative_base()

class SeenLog(Base):
    __tablename__ = 'seen'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    message = Column(Unicode)
    
    def __repr__(self):
        return "SeenLog(%r)" % self.date
    
engine = create_engine('sqlite:///%s' % config.get('database', 'irc_bot'), echo=False)
Base.metadata.create_all(engine)
session = sessionmaker(engine)()
    
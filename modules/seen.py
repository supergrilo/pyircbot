#!/usr/bin/python


from modules import databases
from datetime import datetime

class action():
    def save(self, message):
        try:
            databases.session.add( databases.SeenLog( message=unicode (message.encode("utf-8")), date=datetime.now() ))
            databases.session.commit()
            return True
        except UnicodeDecodeError:
            return False
        
    def seen(self, nick):
        query = database.session.query( database.SeenLog.message, databases.SeenLog.date )
        try:
            return query.filter( databases.SeenLog.message.like( "%s!%%@%%" % unicode( nick )).order_by(database.SeenLog.desc() )).first()
        except Exception:
            return None
    
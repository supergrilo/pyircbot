#!/usr/bin/python


from modules import databases
from datetime import datetime

class action():
    def save(self, join):
        try:
            databases.session.add( databases.JoinLog( join=unicode (join.encode("utf-8")), date=datetime.now() ))
            databases.session.commit()
            return True
        except UnicodeDecodeError:
            return False
        
    def seen(self, nick):
        query = database.session.query( database.JoinLog.join, databases.JoinLog.date )
        try:
            return query.filter( databases.JoinLog.join.like( "%s!%%@%%" % unicode( nick )).order_by(database.JoinLog.desc() )).first()
        except Exception:
            return None
    
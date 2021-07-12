## database tables copied from plugin, There aren't any flags important for table creation
## as tables should not be created, only modified and read. 
from enum import unique
from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    uuid = db.Column(db.Text)
    discord = db.Column(db.Text)
    ip = db.Column(db.Text)
    bornDate = db.Column(db.Integer)
    muted = db.Column(db.Text)
    mutedForAll = db.Column(db.Boolean)

    password = db.Column(db.Text)
    rank = db.Column(db.Text)
    specials = db.Column(db.Text)
    premium = db.Column(db.Text)
    display = db.Column(db.Text)

    country = db.Column(db.Text)
    locale = db.Column(db.Text)

    points = db.Column(db.Integer)

    credits = db.Column(db.Integer)
    webToken = db.Column(db.Text)

class Stats(db.Model):
    owner = db.Column(db.Integer, primary_key=True)
    
    playTime = db.Column(db.Integer)
    silence = db.Column(db.Integer)
    built = db.Column(db.Integer)
    destroyed = db.Column(db.Integer)
    killed = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    played = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    messages = db.Column(db.Integer)
    commands = db.Column(db.Integer)
    lastDeath = db.Column(db.Integer)

class Bans(db.Model):
    value = db.Column(db.Text, unique=True)

db.create_all()


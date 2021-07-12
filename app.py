# //////////////////////////////////////////////////////////////////////////// #

# Imports

# //////////////////////////////////////////////////////////////////////////// #

import json
import os
import random
import threading
import time

from flask import *
from json import load
from flask_sqlalchemy import SQLAlchemy

# //////////////////////////////////////////////////////////////////////////// #

# Database config

# //////////////////////////////////////////////////////////////////////////// #

# the config file structure
"""
{
    "user": "",
    "password": "",
    "host": "",
    "db_name": "",
    "key": ""
}
"""
# load config, create connection uri
# note: you also have to create the database you are connecting tp with 'psql' command
db_config = load(open("config/db.json"))
uri = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['db_name']}"

# //////////////////////////////////////////////////////////////////////////// #

# Flask config

# //////////////////////////////////////////////////////////////////////////// #


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.secret_key = db_config['key']
db = SQLAlchemy(app)

# //////////////////////////////////////////////////////////////////////////// #

# Database tables

# //////////////////////////////////////////////////////////////////////////// #

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
    value = db.Column(db.Text, primary_key=True)

db.create_all() # this up should be started after plugin incase we are using fresh database

# //////////////////////////////////////////////////////////////////////////// #

# Page functions

# //////////////////////////////////////////////////////////////////////////// #

@app.route("/")
def index():
    return render_template("index.html")

# //////////////////////////////////////////////////////////////////////////// #

# Error pages

# //////////////////////////////////////////////////////////////////////////// #


@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404


# //////////////////////////////////////////////////////////////////////////// #

# Run site

# //////////////////////////////////////////////////////////////////////////// #


if __name__ == "__main__":
    app.run(ssl_context=("adhoc"),  # Creates a simple ssl cert and self signs. Not usable for production
            host="0.0.0.0",  # Listen on all available ips
            port=443
            )

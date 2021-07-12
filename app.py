# //////////////////////////////////////////////////////////////////////////// #

# Imports

# //////////////////////////////////////////////////////////////////////////// #

import json
import os
import random
import threading
import time

import pymongo
from flask import *
from json import load
from flask_sqlalchemy import SQLAlchemy

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

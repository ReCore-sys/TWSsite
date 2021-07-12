# This is a base demendency that should be imported by everithing.
# It provides loaded config files, flask app and database objects.

from flask import Flask
from flask.templating import render_template
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

app = Flask(__name__)

# init db
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.secret_key = db_config['key']
db = SQLAlchemy(app)
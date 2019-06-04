from flask import Flask
from pony.orm import Database, db_session
from config.environment import db_uri

app = Flask(__name__, static_folder='dist')

db = Database()
db.bind('postgres', db_uri)

# pylint: disable=W0611,C0413
from config import routes

from models.Entry import Entry, EntrySchema

db.generate_mapping(create_tables=True)

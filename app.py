from flask import Flask
from pony.orm import Database, db_session

app = Flask(__name__)

db = Database()
db.bind('postgres', 'postgres://localhost:5432/hiddengem-db')

# pylint: disable=W0611,C0413
from config import routes

from models.Entry import Entry, EntrySchema

db.generate_mapping(create_tables=True)

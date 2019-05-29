from flask import Blueprint, abort
from pony.orm import db_session
from app import db
from marshmallow import ValidationError
# pylint: disable=W0611, C0413
from models.Entry import Entry, EntrySchema

router = Blueprint(__name__, 'entries')

@router.route('/entries', methods=['GET'])
@db_session
def index():
    entry_schema = EntrySchema(many=True)
    entries = Entry.select()
    return entry_schema.dumps(entries), 200

@router.route('/entries/<int:entry_id>', methods=['GET'])
@db_session
def show(entry_id):
    entry_schema = EntrySchema()
    entry = Entry.get(id=entry_id)
    return entry_schema.dumps(entry)

    if not entry:
        abort(404)

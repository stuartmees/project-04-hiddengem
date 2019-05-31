from flask import Blueprint, abort, jsonify, request, g
from pony.orm import db_session
from app import db
from marshmallow import ValidationError
# pylint: disable=W0611, C0413
from models.Entry import Entry, EntrySchema
from lib.secure_route import secure_route

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
    if not entry:
        abort(404)

    return entry_schema.dumps(entry), 200

@router.route('/entries', methods=['POST'])
@db_session
@secure_route
def create():
    entry_schema = EntrySchema()

    try:
        data = entry_schema.load(request.get_json())
        entry = Entry(**data, created_by=g.current_user)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return entry_schema.dumps(entry), 201

@router.route('/entries/<int:entry_id>', methods=['PUT'])
@secure_route
@db_session
def update(entry_id):
    entry_schema = EntrySchema()
    entry = Entry.get(id=entry_id)

    if not entry:
        abort(404)

    try:
        data = entry_schema.load(request.get_json())
        entry.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return entry_schema.dumps(entry), 201

@router.route('/entries/<int:entry_id>', methods=['DELETE'])
@secure_route
@db_session
def delete(entry_id):
    entry = Entry.get(id=entry_id)

    if not entry:
        abort(404)

    try:
        entry.delete()
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return jsonify({'message': 'Entry deleted'}), 201

from pony.orm import Required, Set
from marshmallow import Schema, fields
from app import db

class State(db.Entity):
    name = Required(str)
    entries = Set('Entry')

class StateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    entries = fields.Nested('EntrySchema', dump_only=True, many=True, excludes=('category',))

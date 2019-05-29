from pony.orm import Required, Optional
from marshmallow import Schema, fields
from app import db

class Entry(db.Entity):
    title = Required(str)
    description = Required(str)
    town = Required(str)
    state = Required('State')
    category = Required('Category')
    website = Optional(str)
    photo = Optional(str)
    lng = Required(float)
    lat = Required(float)

class EntrySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    town = fields.String(required=True)
    state = fields.String(required=True)
    state = fields.Nested('StateSchema', exclude=('entries',), dump_only=True)
    state_id = fields.Int(load_only=True)
    category = fields.Nested('CategorySchema', exclude=('entries',), dump_only=True)
    category_id = fields.Int(load_only=True)
    website = fields.String()
    photo = fields.String()
    lng = fields.Float(required=True)
    lat = fields.Float(required=True)

from pony.orm import Required, Set
from marshmallow import Schema, fields
from app import db


class Category(db.Entity):
    name = Required(str)
    entries = Set('Entry')

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    entries = fields.Nested('EntrySchema', many=True, exclude=('category',), dump_only=True)

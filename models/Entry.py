from pony.orm import Required, Optional
from marshmallow import Schema, fields, post_load
from app import db

from .State import State
from .Category import Category

class Entry(db.Entity):
    title = Required(str)
    description = Required(str)
    location = Required(str)
    state = Required('State')
    category = Required('Category')
    website = Optional(str)
    photo = Optional(str)
    lng = Required(float)
    lat = Required(float)
    created_by = Optional('User')

class EntrySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True, allow_null=False, error_messages={'required': 'Please enter a title'})
    description = fields.String(required=True, allow_null=False, error_messages={'required': 'Please write a description'})
    location = fields.String(required=True, allow_null=False, error_messages={'required': 'Please enter an a location'})
    state = fields.Nested('StateSchema', exclude=('entries',), dump_only=True)
    state_id = fields.Int(load_only=True)
    category = fields.Nested('CategorySchema', exclude=('entries',), dump_only=True)
    category_id = fields.Int(load_only=True, required=True, allow_null=False, error_messages={'required': 'Please select a category'})
    website = fields.String()
    photo = fields.String()
    lng = fields.Float(required=True)
    lat = fields.Float(required=True)
    created_by = fields.Nested('UserSchema', exclude=('entries',))

    @post_load
    def load_category(self, data):
        data['category'] = Category.get(id=data['category_id'])
        del data['category_id']

        return data

    @post_load
    def load_state(self, data):
        data['state'] = State.get(id=data['state_id'])
        del data['state_id']

        return data

from flask import Blueprint, abort, jsonify, request, g
from pony.orm import db_session
from app import db
from marshmallow import ValidationError
# pylint: disable=W0611, C0413
from models.State import State, StateSchema
from lib.secure_route import secure_route

router = Blueprint(__name__, 'state')

@router.route('/states', methods=['GET'])
@db_session
def index():
    state_schema = StateSchema(many=True)
    states = State.select()

    return state_schema.dumps(states), 200

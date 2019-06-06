from flask import Blueprint, request, jsonify
from models.User import User, UserSchema
from app import db
from pony.orm import db_session
from marshmallow import ValidationError

router = Blueprint('auth', __name__)

@router.route('/register', methods=['POST'])
@db_session
def register():
    schema = UserSchema()

    try:
        data = schema.load(request.get_json())
        user = User(**data)
        db.commit()
    except ValidationError as error:
        return jsonify({'error': error.messages}), 422

    return jsonify({
        'message': 'Registation successful. Welcome to Hidden Gem.',
        'token': user.generate_token()
    })


@router.route('/login', methods=['POST'])
@db_session
def login():
    data = request.get_json()

    if not data.get('email') or data.get('email') == '':
        return jsonify({'error': 'You need to enter some details!'}), 422

    if data.get('password') != data.get('password_confirmation'):
        return jsonify({'error': 'The passwords do not match. Please try again.'}), 401

    user = User.get(email=data.get('email'))



    if not user or not user.is_password_valid(data.get('password')):
        return jsonify({'error': 'Sorry we cannot recognise your details. Please try again.'}), 401

    return jsonify({
        'message': f'Welcome back to Hidden Gem, {user.username}',
        'token': user.generate_token()
    })

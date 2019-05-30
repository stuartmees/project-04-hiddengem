from flask import Blueprint, abort, jsonify, request, g
from pony.orm import db_session
from app import db
from marshmallow import ValidationError
# pylint: disable=W0611, C0413
from models.Category import Category, CategorySchema
from lib.secure_route import secure_route

router = Blueprint(__name__, 'categories')

@router.route('/categories', methods=['GET'])
@db_session
def index():
    category_schema = CategorySchema(many=True)
    categories = Category.select()

    return category_schema.dumps(categories), 200

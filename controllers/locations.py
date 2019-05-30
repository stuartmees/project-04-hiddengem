import os
import requests
from flask import Blueprint, Response, jsonify
from pony.orm import db_session

router = Blueprint('locations', __name__)

@router.route('/entries/locations/<string:location>', methods=['GET'])
@db_session
def index(location):
    simon = requests.get('https://maps.googleapis.com/maps/api/place/autocomplete/json',
        params={
            'key':'AIzaSyBUFdiKiC6U2O51XLOzj-1G2U1sbAcZRMA',
            'input':location
            }
    )

    return jsonify(simon.json())

@router.route('/entries/locations/gps/<string:location_id>', methods=['GET'])
@db_session
def gps(location_id):
    simon = requests.get('https://maps.googleapis.com/maps/api/place/details/json',
        params={
            'key':'AIzaSyBUFdiKiC6U2O51XLOzj-1G2U1sbAcZRMA',
            'placeid':location_id
            }
    )

    return jsonify(simon.json())

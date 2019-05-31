import requests
from flask import Blueprint, Response, jsonify
from pony.orm import db_session
from config.environment import google_geo_key

router = Blueprint('locations', __name__)

@router.route('/locations/<string:location>', methods=['GET'])
@db_session
def index(location):
    req = requests.get('https://maps.googleapis.com/maps/api/place/autocomplete/json',
        params={
            'key': google_geo_key,
            'input':location
            }
    )

    return jsonify(req.json())

@router.route('/locations/details/<string:location_id>', methods=['GET'])
@db_session
def gps(location_id):
    req = requests.get('https://maps.googleapis.com/maps/api/place/details/json',
        params={
            'key': google_geo_key,
            'placeid':location_id
            }
    )

    return jsonify(req.json())

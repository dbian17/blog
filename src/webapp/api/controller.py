import sys
sys.path.insert(0, '.')

from flask import Flask
from flask import render_template
from flask import request

from api.view_loading import request_parser
from api.view_loading import map_view_loader
from api.service_client.dynamo import dynamo_service_client

app = Flask(__name__)

def display_name(place_name):
    return place_name.replace("-", " ").title()

app.jinja_env.globals.update(display_name = display_name)

@app.route('/', methods=['GET'])
@app.route('/map', methods=['GET'])
def load_map():
    map_pins = map_view_loader.load(dynamo_service_client.get_places())
    return render_template('map.html', map_pins=map_pins)

@app.route('/list', methods=['GET'])
def load_list():
    places = dynamo_service_client.get_places()
    places.sort(key = lambda place: place.rating, reverse=True)
    return render_template('place_list/place_list.html', places=places)

@app.route('/review', methods=['GET'])
def load_review_submission():
    return render_template('review_form.html')

@app.route('/place/<place_name>', methods=['GET'])
def get_place(place_name):
    place = dynamo_service_client.get_place(place_name)
    return render_template('place.html', place=place, place_name=place_name)

@app.route('/place', methods=['POST'])
def add_place():
    new_place = request_parser.parse_place(request)
    dynamo_service_client.add_place(new_place)
    return "receive"
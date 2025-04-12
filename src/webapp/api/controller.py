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
    # go in reverse order so top places load last
    map_pins = map_view_loader.load(dynamo_service_client.get_all_ranked_place_data(descending=False))
    return render_template('map.html', map_pins_data=map_pins)

@app.route('/list', methods=['GET'])
def load_list():
    places_data = dynamo_service_client.get_all_ranked_place_data()
    return render_template('place_list/place_list.html', places=places_data)

@app.route('/review', methods=['GET'])
def load_review_submission():
    return render_template('review_form.html')

@app.route('/place/<place_name>', methods=['GET'])
def get_place(place_name):
    place_data = dynamo_service_client.get_place_data(place_name)
    place_review = dynamo_service_client.get_place_review(place_name)
    return render_template('place.html', place_data=place_data, place_review=place_review, place_name=place_name)

@app.route('/place', methods=['POST'])
def add_place():
    new_place = request_parser.parse_place(request)
    dynamo_service_client.add_place(new_place)
    return "receive"
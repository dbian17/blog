import sys
sys.path.insert(0, '.')

from flask import Flask
from flask import render_template
from flask import request

import user_agents

from api.view_loading import request_parser
from api.view_loading import map_view_loader
from api.view_loading import view_helper
from api.service_client.dynamo import dynamo_service_client

app = Flask(__name__)

app.jinja_env.globals.update(display_name = view_helper.get_displayble_name)

@app.route('/', methods=['GET'])
@app.route('/map', methods=['GET'])
def load_map():
    # go in reverse order so top places load last
    map_pins = map_view_loader.load(dynamo_service_client.get_all_ranked_place_data(descending=True))
    return render_template('map.html', map_pins_data=map_pins)

@app.route('/list', methods=['GET'])
def load_list():
    places_data = dynamo_service_client.get_all_ranked_place_data()
    is_desktop = user_agents.parse(request.user_agent.string).is_pc
    return render_template('place_list/place_list.html', places=places_data, is_desktop=is_desktop)

@app.route('/review', methods=['GET'])
def load_review_submission():
    return render_template('review_form.html')

@app.route('/review/<place_name>', methods=['GET'])
def load_existing_review_submission(place_name):
    place_data = dynamo_service_client.get_place_data(place_name)
    place_review = dynamo_service_client.get_place_review(place_name)
    return render_template('review_form.html', place_data=place_data, place_review=place_review)

@app.route('/place/<place_name>', methods=['GET'])
def get_place(place_name):
    place_data = dynamo_service_client.get_place_data(place_name)
    place_review = dynamo_service_client.get_place_review(place_name)
    return render_template('place.html', place_data=place_data, place_review=place_review, place_name=place_name)

@app.route('/place', methods=['POST'])
def add_place():
    new_place_data = request_parser.parse_place_data(request)
    new_place_review = request_parser.parse_place_review(request)
    dynamo_service_client.add_place(new_place_data, new_place_review)
    return "receive"
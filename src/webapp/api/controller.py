from flask import Flask
from flask import render_template
from flask import request

from api.view_loading import request_parser
from api.service_client.dynamo import dynamo_service_client


app = Flask(__name__)

@app.route('/', methods=['GET'])
def load_page():
    places = dynamo_service_client.get_places()
    return render_template('index.html', places=places)

@app.route('/review', methods=['GET'])
def load_review_submission():
    return render_template('review_form.html')

@app.route('/place', methods=['POST'])
def add_place():
    place = request_parser.parse_place(request)
    dynamo_service_client.add_place(place)
    return "receive"

from flask import Flask
from flask import render_template
from flask import request
from view_loading import view_loader
from view_loading import request_parser
from service_client.dynamo import dynamo_service_client


app = Flask(__name__)

@app.route('/')
def load_page():
    places = dynamo_service_client.get_places()
    return render_template('index.html', places=places)

@app.route('/place', methods=['POST'])
def add_place():
    place = request_parser.parse_place(request.data)
    dynamo_service_client.add_place(place)
    return "receive"
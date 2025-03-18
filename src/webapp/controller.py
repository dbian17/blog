from flask import Flask
from flask import render_template
from flask import request
from view_loading import view_loader
from view_loading import request_parser
from service_client.dynamo import dynamo_service_client


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    example_place = view_loader.load(name)
    return render_template('index.html', place=example_place)

@app.route('/place', methods=['POST'])
def add_place():
    place = request_parser.parse_place(request.data)
    dynamo_service_client.add_place(place)
    return "receive"
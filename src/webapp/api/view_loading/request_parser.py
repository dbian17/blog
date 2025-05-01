from flask import request
import simplejson as json

from api.view_model.place_data import PlaceData
from api.view_model.place_review import PlaceReview

# Parse request body into place data object. Assumes place object is json string in request payload
def parse_place_data(request: request):
    payload_dict = json.loads(request.data)
    place_data = PlaceData(**payload_dict['place_data'])
    return place_data

# Parse request body into place review object. Assumes place object is json string in request payload
def parse_place_review(request: request):
    payload_dict = json.loads(request.data)
    place_review = PlaceReview(**payload_dict['place_review'])
    return place_review
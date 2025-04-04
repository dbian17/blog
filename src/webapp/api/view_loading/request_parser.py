from flask import request
import simplejson as json

from api.view_model.place import Place

# Parse request body into place object. Assumes place object is json string in request payload
def parse_place(request: request):

    place_dict = json.loads(request.data)
    place = Place(**place_dict)
    return place
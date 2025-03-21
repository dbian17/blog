from flask import request
from view_model.place import Place
import simplejson as json

# Parse request body into place object
# 1. Check if parameters in body
# 2. Check if parameters in form
def parse_place(request: request):
    if request.form:
        place = Place(**request.form.to_dict())
    else:
        place_dict = json.loads(request.data)
        place = Place(**place_dict)
    return place
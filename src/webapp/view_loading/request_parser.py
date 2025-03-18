from view_model.place import Place
from types import SimpleNamespace

import json

# Parse request body into place object
def parse_place(request_body: str):
    place_dict = json.loads(request_body)
    place = Place(**place_dict)
    return place
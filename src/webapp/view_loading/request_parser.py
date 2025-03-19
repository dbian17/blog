from view_model.place import Place
import simplejson as json

# Parse request body into place object
def parse_place(request_body: str):
    place_dict = json.loads(request_body)
    return Place(**place_dict)
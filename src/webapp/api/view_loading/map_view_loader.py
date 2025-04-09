from api.view_model.place import Place
import simplejson as json

def create_map_pin_dict(place: Place):
    map_pin = {}
    map_pin['name'] = place.name
    map_pin['coordinates'] = place.coordinates
    return map_pin

def load(places: list[Place]):
    return [create_map_pin_dict(place) for place in places]
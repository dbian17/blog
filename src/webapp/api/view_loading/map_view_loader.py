from api.view_model.place import Place
import simplejson as json

def create_map_pin_dict(place: Place):
    place_map_pins = []
    if place.coordinates:
        for i in range(len(place.coordinates)//2):
            map_pin = {}
            map_pin['name'] = place.name
            map_pin['rating'] = place.rating
            map_pin['coordinates'] = place.coordinates[i*2: i*2+2]
            place_map_pins.append(map_pin)
    return place_map_pins

def load(places: list[Place]):
    all_map_pins = []
    for place in places:
        all_map_pins.extend(create_map_pin_dict(place))        
    return all_map_pins
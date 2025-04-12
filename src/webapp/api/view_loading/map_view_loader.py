from api.view_model.place_data import Place_Data

def create_map_pin_dict(place_data: Place_Data):
    place_map_pins = []
    if place_data.coordinates:
        for i in range(len(place_data.coordinates)//2):
            map_pin = {}
            map_pin['name'] = place_data.name
            map_pin['rating'] = place_data.rating
            map_pin['coordinates'] = place_data.coordinates[i*2: i*2+2]
            place_map_pins.append(map_pin)
    return place_map_pins

def load(place_data: list[Place_Data]):
    all_map_pins = []
    for place in place_data:
        all_map_pins.extend(create_map_pin_dict(place))        
    return all_map_pins
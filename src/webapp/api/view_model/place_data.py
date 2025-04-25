import simplejson as json
from decimal import Decimal

from api.view_model.place import Place

class Place_Data:

    def __init__(self, name: str, rating: float = 0, types: list[str] = None, tagline: str = None, coordinates: list[float] = None):
        self.name = name.lower().replace(" ", "-")
        
        if rating:
            self.rating = Decimal(str(rating))
        else:
            self.rating = None
        
        if types:
            self.types = types
        else:
            self.types = []
        
        if tagline:
            self.tagline = tagline
        else:
            self.tagline = None

        if coordinates:
            self.coordinates = [Decimal(str(coordinate)) for coordinate in coordinates]
        else:
            self.coordinates = None

    def get_from_place(place: Place):
        print(place)
        return Place_Data(name=place.name, rating=place.rating, types=place.types, tagline=place.tagline, coordinates=place.coordinates) 


    def __repr__(self):
        return json.dumps(self.__dict__)
    
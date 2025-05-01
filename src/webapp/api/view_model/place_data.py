import simplejson as json
from decimal import Decimal

from api.view_model.place import Place

class PlaceData:

    def __init__(self, name: str, rating: float = 0, types: list[str] = None, tagline: str = None, coordinates: list[float] = None, city: str = None, country: str = None):
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

        if city:
            self.city = city
        else:
            self.city = None

        if country:
            self.country = country
        else:
            self.country = None

    def get_from_place(place: Place):
        return PlaceData(name=place.name, rating=place.rating, types=place.types, tagline=place.tagline, coordinates=place.coordinates, city=place.city, country=place.country) 


    def __repr__(self):
        return json.dumps(self.__dict__)
    
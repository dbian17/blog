import simplejson as json
from decimal import Decimal

# Rename to place_request_model?
class Place:

    def __init__(self, name: str, rating: float = 0, types: list[str] = None, review: str = None, tagline: str = None, coordinates: list[float] = None, city: str = None, country: str = None):
        self.name = name.lower().replace(" ", "-")
        
        if rating:
            self.rating = Decimal(str(rating))
        else:
            self.rating = None
        
        self.types = types
        self.review = review
        self.tagline = tagline

        if coordinates:
            self.coordinates = [Decimal(str(coordinate)) for coordinate in coordinates]
        else:
            self.coordinates = None

        self.city = city
        self.country = country

    def __repr__(self):
        return json.dumps(self.__dict__)
    
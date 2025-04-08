import simplejson as json
from decimal import Decimal

class Place:

    def __init__(self, name: str, rating: float = 0, types: list[str] = None, review: str = None, tagline: str = None):
        self.name = name.lower().replace(" ", "-")
        
        if rating:
            self.rating = Decimal(str(rating))
        self.types = types
        self.review = review
        self.tagline = tagline

    def __str__(self):
        return json.dumps(self.__dict__)
    
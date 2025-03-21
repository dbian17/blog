import simplejson as json
from decimal import Decimal

class Place:

    def __init__(self, name: str, rating: float, types: list[str], review: str):
        self.name = name.lower().replace(" ", "-")
        self.rating = Decimal(str(rating))
        self.types = types
        self.review = review

    def __str__(self):
        return json.dumps(self.__dict__)
    
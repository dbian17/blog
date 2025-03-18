import json

class Place:

    def __init__(self, name, rating, types, review):
        self.name = name
        self.rating = rating
        self.types = types
        self.review = review

    def __repr__(self):
      return "Place: " + json.dumps(self.__dict__)
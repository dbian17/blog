import simplejson as json

from api.view_model.place import Place

class PlaceReview:

    def __init__(self, name: str, review: str):
        self.name = name.lower().replace(" ", "-")
        self.review = review

    def get_from_place(place: Place):
        return PlaceReview(name=place.name, review=place.review)

    def __repr__(self):
        return json.dumps(self.__dict__)
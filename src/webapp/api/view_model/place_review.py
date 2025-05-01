import simplejson as json

class PlaceReview:

    def __init__(self, name: str, review: str = None):
        self.name = name.lower().replace(" ", "-")
        if review:
            self.review = review
        else:
            self.review = None

    def __repr__(self):
        return json.dumps(self.__dict__)
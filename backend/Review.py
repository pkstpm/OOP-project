import datetime

class Review:

    id = 0

    date = datetime.datetime.now()

    def __init__(self, rating, name):
        self.__rating = rating
        self.__name = name
        self.__date = Review.date.strftime("%x")
        self.__review_id = Review.id
        Review.id += 1

    @property
    def rating(self):
        return self.__rating
    @property
    def name(self):
        return self.__name
    @property
    def date(self):
        return self.__date
    @property
    def review_id(self):
        return self.__review_id
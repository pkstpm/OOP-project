import datetime

date = datetime.datetime.now()

class Review:

    id = 0

    def __init__(self, rating, name, account_id):
        self.__rating = rating
        self.__name = name
        self.__date = date.strftime("%x")
        self.__account_id = account_id
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
    def account_id(self):
        return self.__account_id
    @property
    def review_id(self):
        return self.__review_id
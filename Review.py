class Review:
    ID = 0

    def __init__(self, rating, comment):
        self.__rating = rating
        self.__comment = comment
        self.__review_id = Review.ID
        Review.ID += 1

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def set_rating(self, rating):
        self.__rating = rating
        return self.__rating
    
    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def set_comment(self, comment):
        return self.__comment
    
    @property
    def review_id(self):
        return self.__review_id
    
    def __str__(self) -> str:
        return str({self.review_id})

class Review:
    def __init__(self, rating, comment):
        self.__rating = rating
        self.__comment = comment

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def set_rating(self,rating):
        self.__rating = rating
        return self.__rating
    
    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def set_comment(self,comment):
        self.__comment = comment
        return self.__comment
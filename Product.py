from Review import *
class Product:
    ID = 0

    def __init__(self, name, price, promotion_price, overview, quantity, status = "available"):
        self._name = name
        self._price = price
        self._promotion_price = promotion_price
        self._overview = overview
        self._quantity = quantity
        self._status = status
        self._review = []
        self._product_id = Product.ID
        Product.ID += 1


    @property
    def name(self):
        return self._name
    @name.setter
    def set_name(self, name):
        self._name = name
        return self._name
    
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def set_quantity(self, quantity):
        self._quantity = quantity
        return self._quantity

    @property
    def price(self):
        return self._price
    @price.setter
    def set_price(self, price):
        self._price = price
        return self._price
    
    @property
    def promotion_price(self):
        return self._promotion_price
    @promotion_price.setter
    def set_promotion_price(self, promotion_price):
        self._promotion_price = promotion_price
        return self._promotion_price

    @property
    def status(self):
        return self._status
    @status.setter
    def set_status(self, status):
        self._status = status
        return self._status
    
    @property
    def overview(self):
        return self._overview
    @overview.setter
    def set_overview(self, overview):
        self._overview = overview
        return self._overview
    
    @property
    def review(self):
        return self._review
    @review.setter
    def set_review(self, review):
        self._review = review
        return self._review
    

    def reduce_quantity(self, quantity):
        if self._quantity < quantity:
            raise Exception(f"Insufficient quantity of {self.name}")
        self._quantity -= quantity

    def add_review(self, rating, comment):
        new_review = Review(rating,comment)
        self.reviews.append(new_review)

    def remove_review(self,reviews):
        self.reviews.remove(reviews)

    def average_rating(self):
        if len(self.reviews) == 0:
            return 0
        else:
            total_rating = sum([review.rating for review in self.reviews])
            return total_rating/len(self.reviews)
    
    def view_product(self):
        return f"Name: {self.name}\nDescription: {self.overview}\nPrice: {self.price}\nAverage Rating: {self.average_rating()}"

class Keyboard(Product):
    def __init__(self, name, price, promotion_price, overview, quantity, keyboard_switch, keyboard_keycap, keys, casecolor, status="available"):
        super().__init__(name, price, promotion_price, overview, quantity, status)
        self.__keyboard_keycap = keyboard_keycap
        self.__keyboard_switch = keyboard_switch
        self.__keys = keys
        self.__casecolor = casecolor

    @property
    def keyboard_keycap(self):
        return self.__keyboard_keycap
    
    @property
    def keyboard_switch(self):
        return self.__keyboard_switch
    
    @property
    def keys(self):
        return self.__keys
    
    @property
    def casecolor(self):
        return self.__casecolor

class Switch(Product):
    def __init__(self, name, price, promotion_price, overview, quantity, variation, spring_weight, type_switch, status="available"):
        super().__init__(name, price, promotion_price, overview, quantity, status)
        self.__variation = variation
        self.__spring_weight = spring_weight
        self.__type_switch = type_switch

    @property
    def variation(self):
        return self.__variation
    
    @property
    def spring_weight(self):
        return self.__variation
    
    @property
    def type_switch(self):
        return self.__type_switch
class Keycap(Product):
    def __init__(self, name, price, promotion_price, overview, quantity, kit, profile, type_keycap, status="available"):
        super().__init__(name, price, promotion_price, overview, quantity, status)
        self.__kit = kit
        self.__profile = profile
        self.__type_keycap = type_keycap

    @property
    def kit(self):
        return self.__kit
    
    @property
    def profile(self):
        return self.__profile
    
    @property
    def type_keycap(self):
        return self.__type_keycap
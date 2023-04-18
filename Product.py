class Product:
    id = 0

    def __init__(self, name, price, promotion_price, overview, quantity, category, status = "available"):
        self._name = name
        self._price = price
        self._promotion_price = promotion_price
        self._overview = overview
        self._quantity = quantity
        self._category = category
        self._status = status
        self._review = []
        self._product_id = Product.id
        Product.id += 1

    @property
    def name(self):
        return self._name
    @name.setter
    def set_name(self, name):
        self._name = name
        return self._name
    
    @property
    def price(self):
        return self._price
    @price.setter
    def set_price(self, price):
        self._price = price

    @property
    def promotion_price(self):
        return self._promotion_price
    @promotion_price.setter
    def set_promotion_price(self, promotion_price):
        self._promotion_price = promotion_price
        return self._promotion_price
    
    @property
    def overview(self):
        return self._overview
    @overview.setter
    def set_overview(self, overview):
        self._overview = overview
        return self._overview
    
    @property
    def quantity(self):
        return self.quantity
    @quantity.setter
    def set_quatity(self, quantity):
        self._quantity = quantity
        return self._quantity
    
    @property
    def category(self):
        return self._category
    @category.setter
    def set_category(self, category):
        self._category = category
        return self._category
    
    @property
    def status(self):
        return self._status
    @status.setter
    def set_status(self, status):
        self._status = status
        return self._status

class Keyboard(Product):
    def __init__(self, name, price, promotion_price, overview, quantity, keyboard_switch, keyboard_keycap, keys, casecolor, status="available"):
        super().__init__(name, price, promotion_price, overview, quantity, "keyboard", status)
        self.__keyboard_switch = keyboard_switch
        self.__keyboard_keycap = keyboard_keycap
        self.__keys = keys
        self.__casecolor = casecolor

    @property
    def keyboard_switch(self):
        return self.__keyboard_switch
    @keyboard_switch.setter
    def set_keyboard_switch(self, keyboard_switch):
        self.__keyboard_switch = keyboard_switch
        return self.__keyboard_switch
    
    @property
    def keyboard_keycap(self):
        return self.__keyboard_keycap
    @keyboard_keycap.setter
    def set_keyboard_keycap(self, keyboard_keycap):
        self.__keyboard_keycap = keyboard_keycap
        return self.__keyboard_keycap
    
    @property
    def keys(self):
        return self.__keys
    @keys.setter
    def set_keys(self, keys):
        self.__keys = keys

    @property
    def casecolor(self):
        return self.__casecolor
    @casecolor.setter
    def set_casecolor(self, casecolor):
        self.__casecolor = casecolor
        return self.__casecolor
    
class Keycap(Product):
    def __init__(self, name, price, promotion_price, overview, quantity, variation, spring_weight, type_switch, status="available"):
        super().__init__(name, price, promotion_price, overview, quantity, "keycap", status)
        self.__variation = variation
        self.__spring_weight = spring_weight
        self.__type_switch = type_switch

    @property
    def variation(self):
        return self.__variation
    @variation.setter
    def set_variation(self, variation):
        self.__variation = variation
        return self.__variation
    
    @property
    def spring_weight(self):
        return self.__spring_weight
    @spring_weight.setter
    def set_spring_weight(self, spring_weight):
        self.__spring_weight = spring_weight
        return self.__spring_weight
    
    @property
    def type_switch(self):
        return self.__type_switch
    @type_switch.setter
    def set_type_switch(self, type_switch):
        self.__type_switch = type_switch
        return self.__type_switch
    
class Switch(Product):
    def __init__(self, name, price, promotion_price, overview, quantity, kit, profile, type_keycap, status="available"):
        super().__init__(name, price, promotion_price, overview, quantity, "switch", status)
        self.__kit = kit
        self.__profile = profile
        self.__type_keycap = type_keycap

    @property
    def kit(self):
        return self.__kit
    @kit.setter
    def set_kit(self, kit):
        self.__kit = kit
        return self.__kit
    
    @property
    def profile(self):
        return self.__profile
    @profile.setter
    def set_profile(self, profile):
        self.__profile = profile
        return self.__profile
    
    @property
    def type_keycap(self):
        return self.__type_keycap
    @type_keycap.setter
    def set_type_keycap(self, type_keycap):
        self.__type_keycap = type_keycap
        return self.__type_keycap
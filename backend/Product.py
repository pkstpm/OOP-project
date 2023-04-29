class Product:

    id = 0

    def __init__(self, name, price, overview, quantity, promotion_price = None, category = None, status = "available"):
        self._name = name
        self._price = price
        self._overview = overview
        self._promotion_price = promotion_price
        self._quantity = quantity
        self._category = category
        self._status = status
        self._product_id = Product.id
        Product.id += 1

    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def overview(self):
        return self._overview
    @property
    def quantity(self):
        return self._quantity
    @property
    def promotion_price(self):
        return self._promotion_price
    @property
    def category(self):
        return self._category
    @property
    def status(self):
        return self._status
    @property
    def product_id(self):
        return self._product_id
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        return self._name
    @price.setter
    def price(self, new_price):
        self._price = new_price
        return self._price
    @overview.setter
    def overview(self, new_overview):
        self._overview = new_overview
        return self._overview
    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity = new_quantity
        return self._quantity
    @promotion_price.setter
    def promotion_price(self, new_promotion_price):
        self._promotion_price = new_promotion_price
        return self._promotion_price
    @category.setter
    def category(self, new_category):
        self._category = new_category
        return self._category
    @status.setter
    def status(self, new_status):
        self._status = new_status
        return self._status
    
class Keyboard(Product):
    def __init__(self, name, price, overview, quantity, keyboard_switch, keyboard_keycap, keys, casecolor, promotion_price=None, status="available"):
        super().__init__(name, price, overview, quantity, promotion_price, 'keyboard', status)
        self.__keyboard_switch = keyboard_switch
        self.__keyboard_keycap = keyboard_keycap
        self.__keys = keys
        self.__casecolor = casecolor
    
    @property
    def keyboard_switch(self):
        return self.__keyboard_switch
    @property
    def keyboard_keycap(self):
        return self.__keyboard_keycap
    @property
    def keys(self):
        return self.__keys
    @property
    def casecolor(self):
        return self.__casecolor
    
    @keyboard_switch.setter
    def keyboard_switch(self, new_keyboard_swicth):
        self.__keyboard_switch = new_keyboard_swicth
        return self.__keyboard_switch
    @keyboard_keycap.setter
    def keyboard_keycap(self, new_keyboard_keycap):
        self.__keyboard_keycap = new_keyboard_keycap
        return self.__keyboard_keycap
    @keys.setter
    def keys(self, new_keys):
        self.__keys = new_keys
        return self.__keys
    @casecolor.setter
    def casecolor(self, new_casecolor):
        self.__casecolor = new_casecolor
        return self.__casecolor
    
class Keycap(Product):
    def __init__(self, name, price, overview, quantity, variation, spring_weight, type_switch, promotion_price = None, status="available"):
        super().__init__(name, price, overview, quantity, promotion_price, 'keycap', status)
        self.__variation = variation
        self.__spring_weight = spring_weight
        self.__type_switch = type_switch

    @property
    def variation(self):
        return self.__variation
    @property
    def spring_weight(self):
        return self.__spring_weight
    @property
    def type_switch(self):
        return self.__type_switch
    
    @variation.setter
    def variation(self, new_variation):
        self.__variation = new_variation
        return self.__variation
    @spring_weight.setter
    def spring_weight(self, new_spring_weight):
        self.__spring_weight = new_spring_weight
        return self.__spring_weight
    @type_switch.setter
    def type_switch(self, new_type_switch):
        self.__type_switch = new_type_switch
        return self.__type_switch
    
class Switch(Product):
    def __init__(self, name, price, overview, quantity, kit, profile, type_keycap, promotion_price=None, status="available"):
        super().__init__(name, price, overview, quantity, promotion_price, 'switch', status)
        self.__kit = kit
        self.__profile =profile
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
    
    @kit.setter
    def kit(self, new_kit):
        self.__kit = new_kit
        return self.__kit
    @profile.setter
    def profile(self, new_profile):
        self.__profile = new_profile
        return self.__profile
    @type_keycap.setter
    def type_keycap(self, new_type_keycap):
        self.__type_keycap = new_type_keycap
        return self.__type_keycap
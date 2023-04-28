class DiscountCode:
    def __init__(self, code, discount_percentage):
        self.__code = code
        self.__discount_percentage = discount_percentage
        

    @property
    def code(self):
        return self.__code
    @code.setter
    def set_code(self,code):
        self.code = code


    @property
    def discount_percentage(self):
        return self.__discount_percentage
    @discount_percentage.setter
    def set_discount_percentage(self,discount_percentage):
        self.discount_percentage = discount_percentage




        
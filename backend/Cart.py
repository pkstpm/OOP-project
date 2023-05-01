from Product import *

class Item:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    @property
    def product(self):
        return self.__product
    @property
    def quantity(self):
        return self.__quantity
    
    @product.setter
    def product(self, new_product):
        self.__product = new_product
        return self.__product
    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity
        return self.__quantity

class Cart:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, new_items):
        self.__items = new_items
        return self.__items
    
   
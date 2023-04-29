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
    
    def calculate_price(self):
        price = 0
        if self.product.promotion_price:
            price = self.product.promotion_price * self.quantity
            return price
        else:
            price = self.product.price * self.quantity
            return price

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
    
    def add_product_to_cart(self, product, quantity=1):
        if product.check_status():
            if product.reduce_quantity(quantity):
                item = self.check_product(product)
                if item:
                    item.quantity += quantity
                    return self.items
                else:
                    new_item = Item(product,quantity)
                    self.items.append(new_item)
                    return self.items
                
    def remove_product_from_cart(self, product):
        item = self.check_product(product)
        if item:
            item.product.add_quantity(item.quantity)
            self.items.remove(item)
            return self.items

    def check_product(self, product):
        for item in self.items:
            if product == item.product:
                return item

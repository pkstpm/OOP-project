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
            price += self.product.promotion_price * self.quantity
            return price
        else:
            price += self.product.price * self.quantity
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
    
    def add_product_to_cart(self, product, quantity = 1):
        if product.check_status() == True:
            if product.reduce_quantity(quantity) == True:
                for item in self.items:
                    if item.product.product_id == product.product_id:
                        item.quantity += quantity
                        return item
                new_item = Item(product,quantity)
                self.items.append(new_item)
                return new_item
    
    def remove_product_from_cart(self, product_id):
        for item in self.items:
            if product_id == item.product.product_id:
                item.product.add_quantity(item.quantity)
                self.items.remove(item)
                return self.items
            
    def clear_cart(self):
        self.items = []
        return self.items
            
    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.calculate_price()
        return total_price
            
    def view_cart(self):
        if not self.items:
            return {"message":"Your cart is empty"}
        else:
            result = [{"name":item.product.name, "quantity":item.quantity, "price":item.calculate_price()} for item in self.items]
            total_price = {"total_price":self.calculate_total_price()}
            result.append(total_price)
            return result
        
    def get_cart(self):
        return self.items


    
   
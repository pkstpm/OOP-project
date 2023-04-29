from Product import *

class ProductCatalog:
    def __init__(self):
        self.__products = []

    @property
    def products(self):
        return self.__products
    @products.setter
    def products(self, new_products):
        self.__products = new_products
        return self.__products
    
    def add_product(self, product):
        if isinstance(product,Product):
            self.products.append(product)
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
        try:
            self.products.append(product)
            return product
        except:
            return False
        
    def search_product_by_name(self, name):
        result = []
        for product in self.products:
            if name.lower() in product.name.lower() or name.lower() in product.category.lower():
                result.append(product)
        return result
    
    def search_product_by_category(self, name, category):
        result = []
        for product in self.products:
            if category == product.category and name.lower() in product.name.lower():
                result.append(product)
        return result
    
    def view_catalog(self):
        return self.products
    
    def get_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
             
    
    
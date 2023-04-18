from Product import *

class ProductCatalog:
    
    def __init__(self):
        self.product_catalog = []
        

    def add_product_to_catalog(self, product):
        self.product_catalog.append(product)

    def search_product_by_name(self,name):
        for product in self.product_catalog:
            if product.name == name:
                return product
            else:
                return None
        
    def search_product_by_category(self,category):
        matching_product_catalog = []
        for product in self.product_catalog:
            if (product._category == category):
                matching_product_catalog.append(product)
        return matching_product_catalog
    
    def view_catalog(self):
        return self.product_catalog
    
from Product import *

class ProductCatalog:
    
    def __init__(self):
        self.products = []
        

    def add_product_to_catalog(self, product):
        self.products.append(product)

    def search_product_by_name(self,name):
        for product in self.products:
            if product.name == name:
                return product
            else:
                return None
        
    def search_product_by_category(self,category):
        matching_products = []
        for product in self.products:
            if (product._category == category):
                matching_products.append(product)
        return matching_products
        
        
    

    
# Create a new product catalog
catalog = ProductCatalog()

catalog.add_product_to_catalog(Keyboard('Keyboard 1', 'KB001', 100.0, 80.0, 'A high-quality mechanical keyboard', 10, 'Cherry MX Brown', 'DSA', 104, 'Black'))
catalog.add_product_to_catalog(Switch('Switch 1', 'SW001', 2.0, 1.5, 'A tactile mechanical switch', 100, 'Tactile', 60, 'MX-compatible'))
catalog.add_product_to_catalog(Keycap('Keycap 1', 'KC001', 50.0, 40.0, 'A set of keycaps for mechanical keyboards', 20, 'Base', 'Cherry', 'Sculpted'))
catalog.add_product_to_catalog(Keycap('Keycap 2', 'KC001', 50.0, 40.0, 'A set of keycaps for mechanical keyboards', 20, 'Base', 'Cherry', 'Sculpted'))

# Search for keyboards
# keyboardlist = []
# keyboard = catalog.search_product_by_category(Keyboard)
# for keyboard in keyboard:
#     keyboardlist.append(keyboard)
# print(keyboardlist)

# # Search for switches
# switchlist = []
# switch = catalog.search_product_by_category(Switch)
# for switch in switch:
#     switchlist.append(switch)
# print(switchlist)

# # Search for keycaps
# keycaplist = []
# keycap = catalog.search_product_by_category(Keycap)
# for keycap in keycap:
#     keycaplist.append(keycap)
# print(keycaplist)

# item = catalog.search_product_by_name("Keyboard 1")
# print(item)
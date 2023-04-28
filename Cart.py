from Product import *
from ProductCatalog import *
from DiscountCode import *
class Cart:
    def __init__(self):
        self.items = {}
    
    def add_product(self, product, quantity = 1):
        if product in self.items.keys():
            self.items[product] += quantity
            for pro in procat.product_catalog:
                if pro.name == product:
                    pro.quantity -= quantity
        else:
            self.items.update({product : quantity})
        
        
    
    def remove_product(self, product, quantity):
        if product in self.items:
            if self.items[product] > quantity:
                self.items[product] -= quantity
            else:
                del self.items[product]
    
    def clear_cart(self):
        self.items = {}
        print("Cart cleared.")

    
    def view_cart(self):
        for product, quantity in self.items.items():
            print(f"Product ID: {product.name}, Quantity: {quantity}")
        # print (self.items)
        # print (list(map(list,self.items.items())))
        # print (list(self.items.keys()))
    
    def calculate_price(self):
        total_price = 0
        for product ,quantity in self.items.items():
            total_price += product.price * quantity
        #print (total_price)
        return total_price
            # total_price += product.price * quantity
        # return total_price

        

            
        
product1 = Product("key001",2000,2000,"blahblah1",20,"keyboard")
product2 = Product("key002",3000,1500,"blahblah",20,"keyboard")
procat = ProductCatalog()
procat.add_product_to_catalog(product1)
procat.add_product_to_catalog(product2)
#procat.view_catalog()

cart = Cart()

cart.add_product(product1, 2)
cart.add_product(product2, 3)
cart.add_product(product1, 2)
# procat.view_catalog()
cart.remove_product(product2, 4)

#cart.view_cart()

# cart.clear_cart()
#




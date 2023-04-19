from Product import *

# Define Cart class
class Cart:
    def __init__(self, cart_id):
        self.cart_id = cart_id
        self.items = {}
    
    def add_product(self, product, quantity = 1):
        if product.name in self.items:
            self.items[product.name] += quantity
        else:
            self.items[product.name] = quantity
    
    def remove_product(self, product, quantity):
        if product.name in self.items:
            if self.items[product.name] > quantity:
                self.items[product.name] -= quantity
            else:
                del self.items[product.name]
    
    def clear_cart(self):
        self.items = []
        print("Cart cleared.")
    
    def view_cart(self):
        print(f"Cart ID: {self.cart_id}")
        for product_id, quantity in self.items.items():
            print(f"Product ID: {product_id}, Quantity: {quantity}")
    
        

product1 = Product("key001","2000","2000","blahblah1","20","keyboard")
product2 = Product("key002","3000","2000","blahblah","20","keyboard")

cart = Cart("12345")

cart.add_product(product1, 2)
cart.add_product(product2, 3)
cart.add_product(product1, 2)

cart.view_cart()

cart.remove_product(product2, 1)

cart.view_cart()

cart.clear_cart()

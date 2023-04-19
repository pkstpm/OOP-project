class Product:
    id = 0

    def __init__(self, name, price, promotion_price, overview, quantity, category, status = "available"):
        self._name = name
        self._price = price
        self._promotion_price = promotion_price
        self._overview = overview
        self._quantity = quantity
        self._category = category
        self._status = status
        self._review = []
        self._product_id = Product.id
        Product.id += 1
    
    @property
    def name(self):
        return self._name
    @name.setter
    def set_name(self, name):
        self._name = name
        return self._name
    
    @property
    def price(self):
        return self._price
    @price.setter
    def set_price(self, price):
        self._price = price


# Define Cart class
class Cart:
    def __init__(self):
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
        for product_id, quantity in self.items.items():
            print(f"Product ID: {product_id}, Quantity: {quantity}")
        # print (self.items)
        # print (list(map(list,self.items.items())))
        # print (list(self.items.keys()))
        
        


    
        

product1 = Product("key001","2000","2000","blahblah1","20","keyboard")
product2 = Product("key002","3000","2000","blahblah","20","keyboard")

cart = Cart()

cart.add_product(product1, 2)
cart.add_product(product2, 3)
cart.add_product(product1, 2)

#cart.view_cart()

cart.remove_product(product2, 1)

cart.view_cart()

#cart.clear_cart()

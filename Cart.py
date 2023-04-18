from Product import *
class Cart:
    def __init__(self, cart_id):
        self._items = []
        self._card_id = cart_id
    
    def add_item(self, product, quantity=1):
        for i in range(len(self._items)):
            if self._items[i][0] == product:
                self._items[i] = (product, self._items[i][1] + quantity)
                return
        self._items.append((product, quantity))

    def remove_item(self, product):
        for item in self._items:
            if item[0] == product:
                self._items.remove(item)
                return
        print("Product not found in the cart.")

    def get_total_price(self):
        total_price = 0
        for item in self._items:
            total_price += item[0].get_price() * item[1]
        return total_price
    
    def view_cart(self):
        if len(self._items) == 0:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self._items:
                print("- " + item[item] + ": " + item[item][1])

product1 = Product("key002","2000","2000","blahblah1","20","keyboard")
product2 = Product("key001","3000","2000","blahblah","20","keyboard")




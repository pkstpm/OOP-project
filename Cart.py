from Product import *
class Cart:
    def __init__(self, cart_id):
        self.cart_id = cart_id
        self.items = []

    def add_item(self, name, quantity=1):
        for item in self.items:
            if item.product.name == name:
                item.quantity += quantity
                break
        else:
            self.items.append({name : quantity})
            print(self.items)

    def remove_item(self, item):
        for cart_item in self.items:
            if cart_item.item == item:
                self.items.remove(cart_item)
                print(f"{item.name} removed from the cart.")
                break
        else:
            print(f"{item.name} is not in the cart.")

    def view_items(self):
        print("Items in the cart:")
        for cart_item in self.items:
            print(f"{cart_item.item.name} (quantity: {cart_item.quantity})")

    def clear_cart(self):
        self.items = []
        print("Cart cleared.")

    def total_price(self):
        total = 0
        for cart_item in self.items:
            total += cart_item.item.price * cart_item.quantity
        return total

    def view_cart(self):
        print(f"Cart ID: {self.cart_id}")
        self.view_items()
        print(f"Total Price: ${self.total_price()}")


product1 = Product("key002","2000","2000","blahblah1","20","keyboard")
product2 = Product("key001","3000","2000","blahblah","20","keyboard")

cart = Cart("100001")
cart.add_item("key002",2)
cart.add_item("key002",2)



    
    def view_cart(self):
        if len(self._items) == 0:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self._items:
                print("- " + item[item] + ": " + item[item][1])

product1 = Product("key002","2000","2000","blahblah1","20","keyboard")
product2 = Product("key001","3000","2000","blahblah","20","keyboard")




from Cart import *
from Order import *

class Account:
    def __init__(self, username ,password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, new_password):
        self._password = new_password
        return self._password
    
class Admin(Account):

    id = 'admin'

    def __init__(self, username, password):
        super().__init__(username, password)
        self.__id = Admin.id

    @property
    def id(self):
        return self.__id
    
class Customer(Account):
    id = 0

    def __init__(self, username, password, email, name):
        super().__init__(username, password)
        self.__email = email
        self.__name = name
        self.__address = ''
        self.__history_purchase = []
        self.__cart = Cart()
        self.__orders = []
        self.__account_id = Customer.id
        Customer.id += 1

    @property
    def email(self):
        return self.__email
    @property
    def name(self):
        return self.__name
    @property
    def address(self):
        return self.__address
    @property
    def history_purchase(self):
        return self.__history_purchase
    @property
    def cart(self):
        return self.__cart
    @property
    def orders(self):
        return self.__orders
    @property
    def account_id(self):
        return self.__account_id
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        return self.__name
    @address.setter
    def address(self, new_address):
        self.__address = new_address
        return self.__address
    @history_purchase.setter
    def history_purchase(self, new_history_purchase):
        self.__history_purchase = new_history_purchase
        return self.__history_purchase
    @cart.setter
    def cart(self, new_cart):
        self.__cart = new_cart
        return self.__cart
    @orders.setter
    def orders(self, new_orders):
        self.__orders = new_orders
        return self.__orders
    
    def make_order(self):
        new_orders = Order(self.cart.calculate_total_price(),self.username)
        for item in self.cart.items:
            product = item.product
            quantity = item.quantity
            price = item.calculate_price()
            item = {"product":product.name,"quantity":quantity,"price":price}
            new_orders.order_item.append(item)
        self.cart.clear_cart()
        self.orders.append(new_orders)
        address = {"addresss":self.address}
        self.orders.append(address)
        return new_orders
    
    def get_order(self, order_id):
        for order in self.orders:
            if order_id == order.order_id:
                return order
            
    def edit_profile(self, name, address):
        self.name = name
        self.address = address

    def add_history_purchase(self, order):
        self.history_purchase.append(order)
import datetime

date = datetime.datetime.now()

class Order:

    id = 0

    def __init__(self, total_price, username):
        self.__order_item = []
        self.__total_price = total_price
        self.__username = username
        self.__status = "Not Paid"
        self.__order_id = Order.id
        Order.id += 1

    @property
    def order_item(self):
        return self.__order_item
    @property
    def total_price(self):
        return self.__total_price
    @property
    def username(self):
        return self.__username
    @property
    def status(self):
        return self.__status
    @property
    def order_id(self):
        return self.__order_id
    
    @order_item.setter
    def order_item(self, new_order_item):
        self.__order_item = new_order_item
        return self.__order_item
    @total_price.setter
    def total_price(self, new_total_price):
        self.__total_price = new_total_price
        return self.__total_price
    @status.setter
    def status(self, new_status):
        self.__status = new_status
        return self.__status

    def view_order(self):
        pass
    
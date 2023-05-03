import datetime

date = datetime.datetime.now()

class Order:

    id = 0

    def __init__(self, order_item, username, address):
        self.__order_item = order_item
        self.__username = username
        self.__address = address
        self.__status = "Not Paid"
        self.__order_id = Order.id
        Order.id += 1

    @property
    def order_item(self):
        return self.__order_item
    @property
    def username(self):
        return self.__username
    @property
    def status(self):
        return self.__status
    @property
    def address(self):
        return self.__address
    @property
    def order_id(self):
        return self.__order_id
    
    @order_item.setter
    def order_item(self, new_order_item):
        self.__order_item = new_order_item
        return self.__order_item
    @status.setter
    def status(self, new_status):
        self.__status = new_status
        return self.__status
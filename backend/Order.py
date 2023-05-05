import datetime

date = datetime.datetime.now()

class Order:

    id = 0

    def __init__(self, order_item, total_price):
        self.__order_item = order_item
        self.__total_price = total_price
        self.__payment = None
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
    def payment(self):
        return self.__payment
    
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
    @payment.setter
    def payment(self, new_payment):
        self.__payment = new_payment
        return self.__payment
    @status.setter
    def status(self, new_status):
        self.__status = new_status
        return self.__status
    
    def view_order(self):
        result = [{"name":item.product.name, "product_id":item.product_id, "quantity":item.quantity, "price":item.calculate_price()} for item in self.order_item]
        return result

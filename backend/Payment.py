from abc import ABC , abstractclassmethod

import datetime

date = datetime.datetime.now()
class Payment(ABC):
    @abstractclassmethod
    def pay(self, order):
        pass

class ShopPay(Payment):
    def pay(self, order):
        order.status = "Paid"
        return order

class Paypal(Payment):
    def pay(self, order):
        order.status = "Paid"
        return order

class GooglePay(Payment):
    def pay(self, order):
        order.status = "Paid"
        return order
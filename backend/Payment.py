from abc import ABC , abstractclassmethod

import datetime

date = datetime.datetime.now()
class Payment(ABC):
    @abstractclassmethod
    def pay(self, order):
        pass

class ShopPay(Payment):
    def pay(self, order):
        if order.status == "Paid":
            return {"message":"this order already pay"}
        else:
            order.status = "Paid"

class Paypal(Payment):
    def pay(self, order):
        if order.status == "Paid":
            return {"message":"this order already pay"}
        else:
            order.status = "Paid"

class GooglePay(Payment):
    def pay(self, order):
        if order.status == "Paid":
            return {"message":"this order already pay"}
        else:
            order.status = "Paid"
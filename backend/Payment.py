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
            order.payment = "Shoppay"
            return {"message":"Success","order":order}

class Paypal(Payment):
    def pay(self, order):
        if order.status == "Paid":
            return {"message":"this order already pay"}
        else:
            order.status = "Paid"
            order.payment = "Paypal"
            return {"message":"Success","order":order}

class GooglePay(Payment):
    def pay(self, order):
        if order.status == "Paid":
            return {"message":"this order already pay"}
        else:
            order.status = "Paid"
            order.payment = "GooglePay"
            return {"message":"Success","order":order}
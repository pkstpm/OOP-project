from Account import *
from Accountlist import *
from Product import *
from ProductCatalog import *
from Cart import *
from Review import *
from Payment import *
from Order import *

product_catalog = ProductCatalog()
account_list = AccountList()
shoppay = ShopPay()
paypal = Paypal()
googlepay = GooglePay()

keyboard1 = Keyboard(name='Keyboard1',price= 100.0,promotion_price= 80.0, overview='A high-quality mechanical keyboard', quantity=10, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard2 = Keyboard(name='Keyboard2',price= 80.0,promotion_price= 75.0, overview='A high-quality mechanical keyboard', quantity=5, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard3 = Keyboard(name='Keyboard3',price= 120.0,promotion_price= 110.0, overview='A high-quality mechanical keyboard', quantity=2, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard4 = Keyboard(name='Keyboard4',price= 150.0,promotion_price= 120.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard5 = Keyboard(name='Keyboard5',price= 130.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=6, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard6 = Keyboard(name='Keyboard6',price= 50.0,promotion_price= 15.0, overview='A high-quality mechanical keyboard', quantity=9, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard7 = Keyboard(name='Keyboard7',price= 450.0,promotion_price= 400.0, overview='A high-quality mechanical keyboard', quantity=3, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard8 = Keyboard(name='Keyboard8',price= 650.0,promotion_price= 500.0, overview='A high-quality mechanical keyboard', quantity=7, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard9 = Keyboard(name='Keyboard9',price= 70.0,promotion_price= 40.0, overview='A high-quality mechanical keyboard', quantity=18, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard10 = Keyboard(name='Keyboard10',price= 1000.0,promotion_price= 990.0, overview='A high-quality mechanical keyboard', quantity=1, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')

keycap1 = Keycap(name="Keycap1", price=110,promotion_price= 100.0, overview="oooo", quantity=4, kit="12", profile="abc", type_keycap="DSA")
keycap2 = Keycap(name="Keycap2", price=90,promotion_price= 85.0, overview="oooo", quantity=5, kit="12", profile="abc", type_keycap="DSA")
keycap3 = Keycap(name="Keycap3", price=100,promotion_price= 80.0, overview="oooo", quantity=4, kit="12", profile="abc", type_keycap="DSA")
keycap4 = Keycap(name="Keycap4", price=120, overview="oooo", quantity=6, kit="12", profile="abc", type_keycap="DSA")
keycap5 = Keycap(name="Keycap5", price=150, overview="oooo", quantity=7, kit="12", profile="abc", type_keycap="DSA")

switch1 = Switch(name="Switch1", price=60,promotion_price= 50.0, overview="o", quantity=9, variation=None, spring_weight=20, type_switch="linear")
switch2 = Switch(name="Switch2", price=50,promotion_price= 40.0, overview="o", quantity=5, variation=None, spring_weight=20, type_switch="linear")
switch3 = Switch(name="Switch3", price=40,promotion_price= 30.0, overview="o", quantity=2, variation=None, spring_weight=20, type_switch="linear")
switch4 = Switch(name="Switch3", price=30,promotion_price= 20.0, overview="o", quantity=2, variation=None, spring_weight=20, type_switch="linear")
switch5 = Switch(name="Switch3", price=20,promotion_price= 10.0, overview="o", quantity=2, variation=None, spring_weight=20, type_switch="linear")

admin1 = Admin(username="admin1",password="admin1")
admin1 = Admin(username="admin2",password="admin2")
admin1 = Admin(username="admin3",password="admin3")

customer1 = Customer(username="Pongsapat", password="1234", email="65010660@kmitl.ac.th", name="Poon")
cart1 = customer1.cart

customer2 = Customer(username="Anucha", password="6969", email="kmitl.ac.th", name="Jacky")


review1 = Review(rating=1,name="Poon",account_id=0)
review2 = Review(rating=2,name="Poon",account_id=0)
review3 = Review(rating=3,name="Poon",account_id=0)
review4 = Review(rating=4,name="Poon",account_id=0)
review5 = Review(rating=5,name="Poon",account_id=0)

product_catalog.add_product(keyboard1)
product_catalog.add_product(keyboard2)
product_catalog.add_product(keyboard3)
product_catalog.add_product(keyboard4)
product_catalog.add_product(keyboard5)
product_catalog.add_product(keyboard6)
product_catalog.add_product(keyboard7)
product_catalog.add_product(keyboard8)
product_catalog.add_product(keyboard9)
product_catalog.add_product(keyboard10)
product_catalog.add_product(keycap1)
product_catalog.add_product(keycap2)
product_catalog.add_product(keycap3)
product_catalog.add_product(keycap4)
product_catalog.add_product(keycap5)
product_catalog.add_product(switch1)
product_catalog.add_product(switch2)
product_catalog.add_product(switch3)
product_catalog.add_product(switch4)
product_catalog.add_product(switch5)

keyboard1.add_review(review1)
keyboard1.add_review(review3)
keyboard1.add_review(review5)
keyboard1.add_review(review2)
keyboard1.add_review(review5)
keyboard1.add_review(review4)
keyboard1.add_review(review5)

account_list.add_account(customer1)
account_list.add_account(customer2)


customer1.make_order()

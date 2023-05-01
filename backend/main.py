from Account import *
from Accountlist import *
from Product import *
from ProductCatalog import *
from Cart import *
from Review import *

product_catalog = ProductCatalog()

product1 = Product(name="Product1", price=100, promotion_price=None, overview='good', quantity=3, category='keyboard')
product2 = Product(name="Product2", price=200, promotion_price=None, overview='good', quantity=3, category='keyboard')
product3 = Product(name="Product3", price=300, promotion_price=None, overview='good', quantity=3, category='keyboard')
product4 = Product(name="Apple", price=400, promotion_price=None, overview='good', quantity=3, category='keyboard')

keyboard1 = Keyboard(name='Keyboard1',price= 100.0,promotion_price= 80.0, overview='A high-quality mechanical keyboard', quantity=10, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard2 = Keyboard(name='Keyboard2',price= 80.0,promotion_price= 75.0, overview='A high-quality mechanical keyboard', quantity=5, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard3 = Keyboard(name='Keyboard3',price= 120.0,promotion_price= 110.0, overview='A high-quality mechanical keyboard', quantity=2, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard4 = Keyboard(name='Keyboard4',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard5 = Keyboard(name='Keyboard5',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
keyboard6 = Keyboard(name='Keyboard6',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')

keycap1 = Keycap(name="Keycap1", price=10, overview="oooo", quantity=4, kit="12", profile="abc", type_keycap="DSA")

switch1 = Switch(name="Switch1", price=5, overview="o", quantity=3, variation=None, spring_weight=20, type_switch="linear")

product_catalog.add_product(product1)
product_catalog.add_product(product2)
product_catalog.add_product(product3)
product_catalog.add_product(product4)
product_catalog.add_product(keyboard1)
product_catalog.add_product(keyboard2)
product_catalog.add_product(keyboard3)
product_catalog.add_product(keyboard4)
product_catalog.add_product(keyboard5)
product_catalog.add_product(keyboard6)
product_catalog.add_product(keycap1)
product_catalog.add_product(switch1)


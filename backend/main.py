from Account import *
from Accountlist import *
from Cart import *
from Product import *
from ProductCatalog import *
from Review import *

catalog = ProductCatalog()
accountlist = AccountList()

product1 = Product(name="Product1", price=100, promotion_price=None, overview='good', quantity=3, category='keyboard')
product2 = Product(name="Product2", price=200, promotion_price=None, overview='good', quantity=3, category='keyboard')
product3 = Product(name="Product3", price=300, promotion_price=None, overview='good', quantity=3, category='keyboard')
product4 = Product(name="Apple", price=400, promotion_price=None, overview='good', quantity=3, category='keyboard')

Keyboard1 = Keyboard(name='Keyboard1',price= 100.0,promotion_price= 80.0, overview='A high-quality mechanical keyboard', quantity=10, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard2 = Keyboard(name='Keyboard2',price= 80.0,promotion_price= 75.0, overview='A high-quality mechanical keyboard', quantity=5, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard3 = Keyboard(name='Keyboard3',price= 120.0,promotion_price= 110.0, overview='A high-quality mechanical keyboard', quantity=2, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard4 = Keyboard(name='Keyboard4',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard5 = Keyboard(name='Keyboard5',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard6 = Keyboard(name='Keyboard6',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')

account1 = Customer("user",1234,"poon","P")
accountlist.add_account(account1)

account2 , cart2 = accountlist.register("1234",1234,1234,1234,1234)
ac1 , c1 = accountlist.login("user", 1234)


catalog.add_product(product1)
catalog.add_product(product2)
catalog.add_product(product3)
catalog.add_product(product4)
catalog.add_product(Keyboard)
catalog.add_product(Keyboard1)
catalog.add_product(Keyboard2)
catalog.add_product(Keyboard3)
catalog.add_product(Keyboard4)
catalog.add_product(Keyboard5)

cart2.add_product_to_cart(Keyboard1,3)
cart2.add_product_to_cart(Keyboard2)
cart2.add_product_to_cart(Keyboard3)
cart2.add_product_to_cart(Keyboard4)
cart2.add_product_to_cart(Keyboard5)
cart2.add_product_to_cart(Keyboard6)

cart2.remove_product_from_cart(Keyboard1)

review1 = Review(5,"ad")
review2 = Review(4,"ad")
review3 = Review(3,"ad")
review4 = Review(2,"ad")

product1.add_review(review1)
product1.add_review(review2)
product1.add_review(review3)
product1.add_review(review4)
product1.remove_review(1)

catalog.search_product('Key')

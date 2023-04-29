from Account import *
from Accountlist import *
from Cart import *
from DiscountCode import *
from Order import *
from Payment import *
from Product import *
from ProductCatalog import *
from Review import *

catalog = ProductCatalog()

Keyboard1 = Keyboard(name='Keyboard1',price= 100.0,promotion_price= 80.0, overview='A high-quality mechanical keyboard', quantity=10, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard2 = Keyboard(name='Keyboard2',price= 80.0,promotion_price= 75.0, overview='A high-quality mechanical keyboard', quantity=5, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard3 = Keyboard(name='Keyboard3',price= 120.0,promotion_price= 110.0, overview='A high-quality mechanical keyboard', quantity=2, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard4 = Keyboard(name='Keyboard4',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard5 = Keyboard(name='Keyboard5',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')
Keyboard6 = Keyboard(name='Keyboard6',price= 150.0,promotion_price= 100.0, overview='A high-quality mechanical keyboard', quantity=8, keyboard_switch='Cherry MX Brown', keyboard_keycap='DSA',keys= 104, casecolor='Black')

Keycap1 = Keycap('Keycap 1', 50.0, 45.0, 'A set of keycaps for mechanical keyboards', 20, 'Base', 'Cherry', 'Sculpted')
Keycap2 = Keycap('Keycap 2', 100.0, 90.0, 'A set of keycaps for mechanical keyboards', 10, 'Base', 'Cherry', 'Sculpted')
Keycap3 = Keycap('Keycap 3', 70.0, 60.0, 'A set of keycaps for mechanical keyboards', 40, 'Base', 'Cherry', 'Sculpted')
Keycap4 = Keycap('Keycap 4', 150.0, 120.0, 'A set of keycaps for mechanical keyboards', 30, 'Base', 'Cherry', 'Sculpted')

Switch1 = Switch('Switch1', 40, 35, 'A tactile mechanical switch', 100, 'Tactile', 60, 'MX-compatible')
Switch2 = Switch('Switch2', 90, 70, 'A tactile mechanical switch', 150, 'Tactile', 60, 'MX-compatible')
Switch3 = Switch('Switch3', 50, 40, 'A tactile mechanical switch', 200, 'Tactile', 60, 'MX-compatible')


catalog.add_product_to_catalog(Keyboard1)
catalog.add_product_to_catalog(Keyboard2)
catalog.add_product_to_catalog(Keyboard3)
catalog.add_product_to_catalog(Keyboard4)
catalog.add_product_to_catalog(Keyboard5)
catalog.add_product_to_catalog(Keyboard6)
catalog.add_product_to_catalog(Keycap1)
catalog.add_product_to_catalog(Keycap2)
catalog.add_product_to_catalog(Keycap3)
catalog.add_product_to_catalog(Keycap4)
catalog.add_product_to_catalog(Switch1)
catalog.add_product_to_catalog(Switch2)
catalog.add_product_to_catalog(Switch3)

Keyboard1.add_review(5, "asjodn")
Keyboard1.add_review(4, "asjodn")
Keyboard1.add_review(3, "asjodn")


account_list = Accountlist()

jack = Customer("jkj", "1234", "akeraanucha1@gmail.com", "Jack")
tai = Customer("tai", "4321", "taitai@gmail.com", "Tai")
poon = Admin("poon", "555", "poonpoon@gmail.com", "Poon")
poon = Admin("poon", "555", "poonpoon@gmail.com", "Poon")
poon = Admin("poon", "555", "poonpoon@gmail.com", "Poon")

account_list.add_account(jack)
account_list.add_account(tai)
account_list.add_account(poon)

account_list.login("poon","555")

account_list.login("poon","554")

account_list.login("jkj","1234")

account_list.create_account("jkj","444","444","chomchom@gmail.com", "Chompoo")

account_list.create_account("chom","555","444","chomchom@gmail.com", "Chompoo")

account_list.create_account("chom","444","444","chomchom@gmail.com", "Chompoo")
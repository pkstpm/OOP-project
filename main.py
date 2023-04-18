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

catalog.add_product_to_catalog(Keyboard('Keyboard 1', 'KB001', 100.0, 80.0, 'A high-quality mechanical keyboard', 10, 'Cherry MX Brown', 'DSA', 104, 'Black'))
catalog.add_product_to_catalog(Switch('Switch 1', 'SW001', 2.0, 1.5, 'A tactile mechanical switch', 100, 'Tactile', 60, 'MX-compatible'))
catalog.add_product_to_catalog(Keycap('Keycap 1', 'KC001', 50.0, 40.0, 'A set of keycaps for mechanical keyboards', 20, 'Base', 'Cherry', 'Sculpted'))
catalog.add_product_to_catalog(Keycap('Keycap 2', 'KC001', 50.0, 40.0, 'A set of keycaps for mechanical keyboards', 20, 'Base', 'Cherry', 'Sculpted'))
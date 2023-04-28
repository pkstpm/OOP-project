from DiscountCode import *
class Account:
    def __init__(self, username, password, email,name):
        self._username = username
        self._password = password
        self._email = email
        self._name = name

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, new_password):
        self._password = new_password
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

class Admin(Account):
    ID ="admin"
    def __init__(self, username, password, email, name):
        super().__init__(username, password, email,name)
        self.__admin_name = "Admin_" + name
        self.__id = Admin.ID
        self.__code_list = []
    
    @property
    def name(self):
        return self.__admin_name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def code_list(self):
        return self.__code_list
    @code_list.setter
    def set_code_list(self, code_list):
        self.__code_list = code_list
        return self.__code_list
    
    def add_discount_code(self,code):
        self.code_list.append(code)

class Customer(Account):
    ID = 0
    def __init__(self, username, password, email, name):
        super().__init__(username, password, email, name)
        self.__address = ""
        self.__shipping_status = []
        self.__history_purchase = []
        self.__point = 0
        self.__id = Customer.ID
        Customer.ID += 1
        
    @property
    def id(self):
        return self.__id
    
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, new_address):
        self.__address = str(new_address)
        
    @property
    def shipping_status(self):
        return self.__shipping_status
    
    @property
    def history_purchase(self):
        return self.__history_purchase
    
    @property
    def point(self):
        return self.__point
    
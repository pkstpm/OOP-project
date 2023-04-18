class Account:
    def __init__(self, username, password, email,name):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__name = name

    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @property
    def email(self):
        return self.__email

    @property
    def name(self):
        return self.__name
    
    @password.setter
    def password(self, new_password):
        self.__password = new_password
        
    @email.setter
    def email(self, new_email):
        self.__email = new_email
        
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    

class Admin(Account):
    ID ="admin"
    def __init__(self, username, password, email, name):
        super().__init__(username, password, email,name)
        self.__admin_name = "Admin_" + name
        self.__id = Admin.ID
    
    @property
    def name(self):
        return self.__admin_name
    
    @property
    def id(self):
        return self.__id

class Customer(Account):
    ID = 0
    def __init__(self, username, password, email,name):
        super().__init__(username, password, email, name)
        self._address = ""
        self._shipping_status = []
        self._history_purchase = []
        self._point = 0
        self._id = Customer.ID
        Customer.ID += 1
        
    @property
    def id(self):
        return self._id
    
    @property
    def address(self):
        return self._address
    
    @property
    def shipping_status(self):
        return self._shipping_status
    
    @property
    def history_purchase(self):
        return self._history_purchase
    
    @property
    def point(self):
        return self._point
    
    @address.setter
    def address(self, new_address):
        self._address = str(new_address)
        
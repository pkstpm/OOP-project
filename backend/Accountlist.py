from Account import *

class AccountList:
    def __init__(self):
        self.__accounts = []

    @property
    def accounts(self):
        return self.__accounts
    @accounts.setter
    def accounts(self, new_accounts):
        self.__accounts = new_accounts
        return self.__accounts
    
    def add_account(self, account):
        if isinstance(account,Account):
            self.accounts.append(account)
            return self.accounts
        
    def register(self, username ,password, check_password, email, name):
        if self.verify_account(username,password,check_password,email):
            new_account = Customer(username,password,email,name)
            return new_account , new_account.cart

    def verify_account(self, username, password, check_password, email):
        if self.check_account(username, email):
            if self.check_password(password, check_password):
                return True
            
        return False
   
    def check_password(self, password, check_password):
        if password == check_password:
            return True
        else:
            return False

    def check_account(self, username, email):
        for account in self.accounts:
            if account.username == username or account.email == email:
                return False
            
        return True
    
    def login(self, username, password):
        for account in self.accounts:
            if account.username == username and account.password == password:
                return account , account.cart
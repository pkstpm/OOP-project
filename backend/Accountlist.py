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
    
    def get_account(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
    
    def add_account(self, account):
        try:
            self.accounts.append(account)
            return account
        except:
            return False
        
    def verify_account(self, username, email):
        for account in self.accounts:
            if username == account.username or email == account.email:
                return False
        return True
    
    def verify_login(self, username, password):
        for account in self.accounts:
            if username == account.username and password == account.password:
                return account
            
    def check_password(self, password, check_password):
        if password == check_password:
            return True
        return False
            
        
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
    
    def add_account(self ,account):
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
            
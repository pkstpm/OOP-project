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
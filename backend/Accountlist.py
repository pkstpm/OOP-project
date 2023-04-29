class AccountList:
    def __init__(self):
        self.__accounts = []

    @property
    def accounts(self):
        return self.__accounts
    @accounts.setter
    def account_list(self, new_accounts):
        self.__accounts = new_accounts
        return self.__accounts
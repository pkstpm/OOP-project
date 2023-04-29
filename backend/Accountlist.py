class AccountList:
    def __init__(self):
        self.__account_list = []

    @property
    def account_list(self):
        return self.__account_list
    @account_list.setter
    def account_list(self, new_account_list):
        self.__account_list = new_account_list
        return self.__account_list
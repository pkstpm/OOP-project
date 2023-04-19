from Account import *

class Accountlist:
    def __init__(self):
        self.account_list=[]
        
    def get_account_list(self):
        return self.account_list
        
    def add_account(self, account):
        self.account_list.append(account)
        
    def create_account(self,username,password,check_password,email, name):
        if(self.check_correct(username)):
            if(password == check_password):
                self.account_list.append(Customer(username,password,email,name))
                return f"register successfully!!"
            else:
                return f"plese check your password again!!"
        else:
            return f"username had been use!!"
        
    def check_correct(self, username):
        if self.account_list != []:
            for account in self.account_list:
                if account.username == username:
                    return False
                else:
                    return True
        else:
            return True
    
    def login(self,username,password):
        for account in self.account_list:
            if username == account.username and password == account.password:
                if account.id == "admin":
                    return "HI ADMIN!!!"
                else:
                    return "welcome everyone let's shoppinggggg"
        return "please try again!!!"
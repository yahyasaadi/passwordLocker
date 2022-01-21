# Class to hold user accounts

class Account:
    
    def __init__(self, userName, password):
        """
        Class that generates new instances of accounts
        """

        self.username = userName
        self.password = password

    userAccounts = []
    def save_account(self):
        """
        This method saves every new user's account info 
        """
        return Account.userAccounts.append(self)

"""
Testing below as I go
"""
# newAccount = Account("yahyasaadi", "1234")
# print(len(Account.userAccounts), "users list is now empty")
# newAccount.save_account()

# Another one
# newAccount2 = Account("yussufsaadi", "4321")
# newAccount.save_account()
# print("USers account now has ", len(Account.userAccounts))
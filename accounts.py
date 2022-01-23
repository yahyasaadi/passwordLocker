# Class to hold user accounts

class Account:
    
    def __init__(self, userName, password):
        """
        Class that generates new instances of accounts
        """

        self.userName = userName
        self.password = password

    userAccounts = []
    def save_account(self):
        """
        This method saves every new user's account info 
        """
        return Account.userAccounts.append(self)


    @classmethod
    def username_exists(cls, username):
        """
        This alerts the user if a username has been taken and asks them
        to create another one
        """
        for account in cls.userAccounts:
            if account.userName == username:
                return "Username already taken. Please try another one."
        return "Yes you can user that as a username"


    def delete_account(self):
        """
        This method delete an account 
        """
        return Account.userAccounts.remove(self)


    @classmethod
    def display_accounts(cls):
        return cls.userAccounts



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
from accounts import Account
from passwords import Password

# fucntion to create new method
def create_account(usrname, password):
    account = Account(usrname, password)
    return account


# fucntion to save new accounts
def save_account(account):
    account.save_account()

# function to delete an account
def del_account(account):
    account.delete_account()




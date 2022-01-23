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


# function to check if a username exists
def checkIfUsernameExists(username):
    return Account.username_exists(username)


# fucntion to display account
def displayAccount():
    return Account.display_accounts()


def main():
    print("Welcome To PassWordLocker. What is your name?")
    user = input()

    print(f"{user}, please sign up and lets get started.")

    while True:
        print("Use these short codes : ca - create a new account, sp - save a password, dp - display passwords")
        answer = input().lower()

        if answer == 'ca':
            print('*'*15)

            print("Username: ")
            username = input()

            print("Password: ")
            pword = input()

            save_account(create_account(username, pword))
            print(f"The account for {username} has been made.")

if __name__ == '__main__':
    main()


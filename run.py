#!/usr/bin/env python3

from accounts import Account
from passwords import Password

"""
Fucntions accessing the Account class
"""
# fucntion to create new method
def create_account(username, password):
    account = Account(username, password)
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



"""
Fucntions accessing the Password class
"""

def create_password(sitename, username, password):
    new_password = Password(sitename, username, password)
    return new_password


# fucntion to save new passwords
def save_password(password):
    password.save_password()


# function to delete a password
def del_password(password):
    password.delete_password()


# fucntion to display passwords
def display_password():
    return Password.display_password()


# fucntion to display passwords
def generate_password():
    return Password.generate_pw()


def main():
    print("Welcome To PassWordLocker. What is your name?")
    user = input()

    print(f"{user}, please sign up and lets get started.")

    while True:
        print("Use these short codes : ca - create a new account, sp - save a password, dp - display passwords, ex - exit")
        answer = input().lower()

        if answer == 'ca':
            print('*'*15)

            print("Username: ")
            username = input()

            print("Password: ")
            pword = input()

            save_account(create_account(username, pword))
            print(f"The account for {username} has been made.")

        elif answer == 'sp':
            print('*'*15)

            print("Sitename, eg Instagram: ")
            sitename = input()

            print("Your username for the site: ")
            username = input()
            # Trying password generate
            print("Do you want a generate password? y = yes or n = no")
            generate_pass = input()
            if generate_pass == 'y':
                generated = generate_password()
                print("This is your generated password ", generated)
                save_password(create_password(sitename, username, generated))
            else:
                print("Your password for the site: ")
                pword = input()

                save_password(create_password(sitename, username, pword))
            print(f"Your password for {sitename} has been saved.")
        
        
        elif answer == 'dp':
            print('*'*15)
            print('\n')
            if display_password():
                for password in display_password():
                    print(f"{password.siteName} {password.user_name} {password.pass_word}")
                    print('\n')
            else:
                print('You have saved passwords.')

        elif answer == 'ex':
            print('Exiting the application...')
            break

        else:
            print("Please choose an option.")



if __name__ == '__main__':
    main()


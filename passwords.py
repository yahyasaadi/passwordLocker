# Passwords class
import random

from pyrfc3339 import generate
class Password:

    def __init__(self, siteName, user_name, pass_word):
        """
        Class that generates new instances of accounts
        """

        self.siteName = siteName
        self.user_name = user_name
        self.pass_word = pass_word

    passwords = []
    def save_password(self):
        '''
        Method to save a password to a list
        '''
        return Password.passwords.append(self)

    
    @classmethod
    def display_password(cls):
        '''
        This method returns the password list
        '''
        return cls.passwords


    def delete_password(self):
        '''
        Method to delete a password from the list
        '''
        return Password.passwords.remove(self)

    
    random_pass = "abcdefghijklmnopqrstuvwxyz0123456789"
    @classmethod
    def generate_pw(cls):
        '''
        Added a method to generate a random password for the user
        '''
        generated_password = ''.join((random.choice(cls.random_pass) for i in range(8)))
        return generated_password






# TESTING PART
pw = Password("IG", "yahyasaadi", "1234")
# pw.save_password()
# pw2 = Password("TW", "yahya", "1234")
# pw2.save_password()
# print(len(Password.passwords))
print(Password.generate_pw())
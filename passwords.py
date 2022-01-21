# Passwords class
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
        return cls.passwords[0]


    def delete_password(self):
        '''
        Method to delete a password from the list
        '''
        return Password.passwords.remove(self)


# TESTING PART
# pw = Password("IG", "yahyasaadi", "1234")
# pw.save_password()
# pw2 = Password("TW", "yahya", "1234")
# pw2.save_password()
# print(len(Password.passwords))
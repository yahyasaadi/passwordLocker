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

    
    def delete_password(self):
        '''
        Method to delete a password from the list
        '''
        return Password.passwords.remove(self)
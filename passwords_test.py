import unittest
from passwords import Password


class TestAccount(unittest.TestCase):
    
    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_password = Password("Instagram", "yahyanoor", "1234")

    
    # The first test
    def test_init(self):
        """
        test_init test case to test if the object is initialized propely
        """

        self.assertEqual(self.new_password.siteName, "Instagram")
        self.assertEqual(self.new_password.user_name, "yahyanoor")
        self.assertEqual(self.new_password.pass_word, "1234")


    # The Second Test
    def test_save_account(self):
        """
        test_save_account is a test case to see if an account object is saved into the account list
        """
        self.new_password.save_password()
        self.assertEqual(len(Password.passwords), 1)

    
    def tearDown(self):
        """
        This method clear up after a test case is done
        """
        Password.passwords = []
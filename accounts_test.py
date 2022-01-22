import unittest
from accounts import Account

class TestAccount(unittest.TestCase):
    
    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_account = Account("yahyanoor", "1234")


    # The first test
    def test_init(self):
        """
        test_init test case to test if the object is initialized propely
        """

        self.assertEqual(self.new_account.userName, "yahyanoor")
        self.assertEqual(self.new_account.password, "1234")


    # The Second Test
    def test_save_account(self):
        """
        test_save_account is a test case to see if an account object is saved into the account list
        """
        self.new_account.save_account()
        self.assertEqual(len(Account.userAccounts), 1)


    def tearDown(self):
        """
        This method clear up after a test case is done
        """
        Account.userAccounts = []



if __name__ == '__main__':
    unittest.main()
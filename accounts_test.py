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
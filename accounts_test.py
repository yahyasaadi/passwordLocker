import unittest
from accounts import Account

class TestAccount(unittest.TestCase):
    
    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_account = Account("yahyanoor", "1234")
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
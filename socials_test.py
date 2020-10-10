import unittest
from socials import Credentials

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''

        self.new_socials = Credentials('Instagram','Felista_Kiriinya','Felista1#')

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_socials.account_name,'Instagram')
        self.assertEqual(self.new_socials.username,'Felista_Kiriinya') 
        self.assertEqual(self.new_socials.password,'Felista1#')

    def test_save_account(self):

        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''

        self.new_socials.save_account()
        self.assertEqual(len(Credentials.account_list),1)
         



if __name__ == '__main__':
    unittest.main()            
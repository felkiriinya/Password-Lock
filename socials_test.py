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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Credentials.account_list=[]

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

    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''    

        self.new_socials.save_account()
        test_account =  Credentials('Twitter','felkiriinya','Tomorrow1£')
        test_account.save_account()

        self.assertEqual(len(Credentials.account_list),2) 
    
    def test_delete_account(self):
        '''
        test_delete_account test case to test if the account object is removed from
         the account list
         '''
        self.new_socials.save_account() 
        test_account =  Credentials('Twitter','felkiriinya','Tomorrow1£')
        test_account.save_account()
        
        self.new_socials.delete_account()
        self.assertEqual(len(Credentials.account_list),1)
    
    def test_display_accounts(self):
        '''
        test method that returns a list of all accounts added
        '''
        self.assertEqual(Credentials.display_accounts(),Credentials.account_list)

if __name__ == '__main__':
    unittest.main()            
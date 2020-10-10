import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    This is a test class that defines test cases for the user class behaviours

    Args:
        unittest.Testcase: class that helps in creating test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Felista','Felista1#')
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list=[]
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'Felista')  
        self.assertEqual(self.new_user.password,'Felista1#')  
    
    def test_save_user(self):
        '''
        test_save_user to check if we can save our user object to our users_list
        '''
        self.new_user.save_user()
        test_user =User ('username','password')
        test_user.save_user()
        self.assertEqual(len(User.users_list),2)

if __name__ == '__main__':
    unittest.main()            
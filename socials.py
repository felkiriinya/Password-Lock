class Credentials:

    '''
    class that generates new instances of account names and their credentials
    '''

    account_list=[]

    def __init__(self,account_name,username,password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: new user  social account name
            username: new user username
            password: new user password
        '''
        self.account_name=account_name
        self.username=username
        self.password=password


    def save_account(self):

        '''
        save_account method saves accounts objects into the contact_list
        '''
        Credentials.account_list.append(self)

    def delete_account(self):
        '''
        delete_account method deletes account objects saved in the account_list
        '''
        Credentials.account_list.remove(self)

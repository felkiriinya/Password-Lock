class User:
    '''
    Class that generates new instances of users.
    '''
     
    users_list = []

    def __init__(self, username, password):

        '''
        __init__ method helps define our objects properties

        Args:
            username: login's username for a new user
            password: login:s password for a new user
        '''

        self.username = username
        self.password = password

    def save_user(self):

        '''
        Method used to save user objects into the users list
        '''

        User.users_list.append(self)
#!/usr/bin/env python3.8

from user import User
from socials import Credentials
import random
import string

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_new_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def create_social_account(accountname,username,password):
    '''
    Function to create a new account
    '''
    new_account= Credentials(account_name,username,password)
    return new_account

def delete_social_account(socials):
    '''
    function to delete an account
    '''
    socials.delete_account()          

def display_accounts():
    '''
    Function that returns all the saved 
    '''
    return Credentials.display_accounts()

def main():
    print("WELCOME TO YOUR PERSONAL PASSWORD LOCKER")
    print("What is your name?")
    print('\n')
    user_name= input()
    print('\n')
    print(f"Hello {user_name}! You can use these short codes to navigate through")
    print('\n')

    while True:

        print('cc - Create a new password locker account')
        print('lg - Log in into your created account')
        print('ex - Exit your password locker account')

        short_code = input().lower()

        if short_code == 'cc':
            print('Create your password locker account')
            print("-"*10)

            print('Username...')
            username = input()

            print('Password...')
            password = input()

            save_new_user(create_user(username,password))

            print ('\n')
            print(f'Congratulations {username} your account has been successfully created!')

            print ('\n')
            print('You can now log in using the username and password created')

            print('Username...')
            login_username = input()

            print('Password...')
            login_password = input()

            if username != login_username or password != login_password:
                print('Invalid Username or password!')
                print('Re-enter your username....')
                login_username = input()

                print('Re- enter your password....')
                login_password = input()

            else :
                 print ('\n')
                 print(f'Hello {login_username}. Welcome to your password locker account!')
                 print ('\n')

        elif short_code == 'lg':
             
                print('Log in to your existing account')
                print('Username....')
                lg_username = input()

                print('Password....')
                lg_password = input()

                if lg_username != 'Felista' and lg_password != 'Felista1#':
                    print('The account does not exist, please create an account')
                else:
                    print(f'Hello {lg_username}. Welcome to your password locker account!')
                    print ('\n')

if __name__ == '__main__':

    main()
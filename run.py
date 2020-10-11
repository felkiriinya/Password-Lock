#!/usr/bin/env python3.8

from user import User
from socials import Credentials
import random

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

def delete_social_account(socials)
    '''
    function to delete an account
    '''
    socials.delete_account()          

def display_accounts()
    '''
    Function that returns all the saved 
    '''
    return Credentials.display_accounts()

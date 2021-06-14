# import sys
# sys.path.append("tests/test_base")
from tests.test_base import BaseTest,db
from market.models import User, Item
from flask import request
from flask_login import current_user
# from market.__init__ import db


class TestRegister(BaseTest):
    
    def test_valid_register_success(self):
        with self.app:
            response = self.app.post('/register', data=dict(
                username='Kevin', email_address='ok@gmail.com',
                password1='python', password2='python'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Account created successfully! You are now logged in as Kevin', response.data)
           
    def test_invalid_registeration(self):
        with self.app:
            response = self.app.post('/register', data=dict(
                username='kevin', email_address='test@gmail.com',
                password1='python', password2='qwerty'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"There was an error with creating a user: ", response.data)
            
           

class TestLogin(BaseTest):
    def test_valid_login(self):
        with self.app:
            response = self.app.post('/register', data=dict(
                username='jeff', email_address='okay@gmail.com',
                password1='python1', password2='python1'
            ), follow_redirects=True)
            
            response = self.app.post('/login', data=dict(
                username='jeff', password='python1'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Success! You are logged in as: jeff', response.data)
            user = db.session.query(User).filter_by(username='jeff').first()
            self.assertTrue(user)
            
    def test_invalid_login(self):
        with self.app:
            response = self.app.post('/login', data=dict(
                username='hulk', password='123456'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Username and password are not match! Please try again', response.data)
            


            

class TestLogout(BaseTest):
    def test_(self):
        with self.app:
            response = self.app.post('/register', data=dict(
                username='steve', email_address='okays@gmail.com',
                password1='python1', password2='python1'
            ), follow_redirects=True)
            
            response = self.app.post('/login', data=dict(
                username='steve', password='python1'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Success! You are logged in as: steve', response.data)
            user = db.session.query(User).filter_by(username='steve').first()
            self.assertTrue(user)
            #logs user out
            response = self.app.get('/logout', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'You have been logged out!', response.data)
            
    
    
            #redirects to logout page
            self.assertIn('/home', request.url)
            self.assertFalse(current_user.is_active)


# class TestMarket(BaseTest):
#     def test_can_purchase(self):
#         with self.app:
            
            
           
           







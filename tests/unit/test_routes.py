# import sys
# sys.path.append("tests/test_base")
from tests.test_base import BaseTest, db
# from market.__init__ import db
from market.models import User, Item
from flask import request
from flask_login import current_user, AnonymousUserMixin


class TestHome(BaseTest):
    
    def test_route(self):
        with self.app:
            response = self.app.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    def test_route_home(self):
        with self.app:
            # response = self.app.get('/home', follow_redirects=True)
            # self.assertEqual(response.status_code, 200)
            response = self.app.get('/home', follow_redirects=True)
            self.assertIn('/home', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Jim Shaped Coding Market', response.data)
            
            
class TestMarket(BaseTest):
    
    def test_route_market(self):
        with self.app:
            response = self.app.get('/market', follow_redirects=True)
            # self.assertIn('/market', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Login', response.data)
            
            
class TestRegister(BaseTest):
    def test_register_route(self):
        with self.app:
            response = self.app.get('/register', follow_redirects=True)
            self.assertIn('/register', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Create your Account', response.data)
            self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))
            
    
    
    #def test_user_registeration(self):
    #     with self.app:
    #         response = self.app.post('/register', data=dict(
    #             username='kevin', email_address='test@gmail.com',
    #             password1='python', password2='python'
    #         ), follow_redirects=True)
    #         self.assertIn(b'Account created successfully! You are now logged in as kevin', response.data)
    #         self.assertEqual(response.status_code, 200)
    #         user = User.query.filter_by(email_address='test@gmail.com').first()
    #         self.assertTrue(user)
    
 
 
class TestLogin(BaseTest):
    def test_login_route(self):
        with self.app:
            response = self.app.get('/login', follow_redirects=True)
            self.assertIn('/login', request.url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Please Login', response.data)
 
            

          
          
            
            
            
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
    def test_logout(self):
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


class TestMarket(BaseTest):
    def test_can_purchase(self):
        with self.app:
           
            
            response = self.app.post('/register', data=dict(username='test4', email_address='test3@test.com', password1='password', password2='password'), follow_redirects=True)
            self.assertEqual(current_user.get_id(), '1')
            user = db.session.query(User).filter_by(username='test4').first()
            user.budget = 5000
            db.session.commit()
            # check if user budget is 5000
            self.assertEqual(user.budget, 5000)
            
            # create item save to db
            item = Item(name='paper', price=1200, barcode='testing', description='white')
            db.session.add(item)
            db.session.commit()
            result = db.session.query(Item).filter_by(name="paper").first()
            self.assertTrue(result)
            
            # buy item in market
            response = self.app.post('/market',data=dict(purchased_item='paper') ,follow_redirects=True)
            
            
            self.assertIn(b'Congratulations! You purchased paper for 1200$', response.data)


    def test_can_not_purchase(self):
        with self.app:
           
            
            response = self.app.post('/register', data=dict(username='test5', email_address='test5@test.com', password1='password', password2='password'), follow_redirects=True)
            self.assertEqual(current_user.get_id(), '1')
            user = db.session.query(User).filter_by(username='test5').first()
            user.budget = 1000
            db.session.commit()
            # check if user budget is 1000
            self.assertEqual(user.budget, 1000)
            
            # create item save to db
            item = Item(name='paper', price=1200, barcode='testing', description='white')
            db.session.add(item)
            db.session.commit()
            result = db.session.query(Item).filter_by(name="paper").first()
            self.assertTrue(result)
            
            # buy item in market
            response = self.app.post('/market',data=dict(purchased_item='paper') ,follow_redirects=True)
            
            
            self.assertIn(b"Unfortunately, you don&#39;t have enough money to purchase paper!", response.data)


    def test_can_sell(self):
        with self.app:
            self.app.post('/register', data=dict(username='test6', email_address='test6@test.com', password1='password', password2='password'), follow_redirects=True)
            self.assertTrue(current_user.is_active)
            self.assertIn('/market', request.url)
            
            self.assertTrue(current_user.get_id(), '1')
            user = db.session.query(User).filter_by(username='test6').first()
            self.assertEqual(user.username, 'test6')
            
            item = Item(id=1, name='paper', price=1200, barcode='testing', description='white', owner=1)
            db.session.add(item)
            db.session.commit()
            self.assertTrue(user.items, 'paper')
            response = self.app.post('/market', data=dict(sold_item='paper') ,follow_redirects=True)
            self.assertIn(b"Congratulations! You sold paper back to market!", response.data)


    def test_can_not_sell(self):
        with self.app:
           
            
            self.app.post('/register', data=dict(username='test7', email_address='test7@test.com', password1='password', password2='password'), follow_redirects=True)
            self.assertTrue(current_user.is_active)
            self.assertIn('/market', request.url)
            
            self.assertTrue(current_user.get_id(), '1')
            user = db.session.query(User).filter_by(username='test7').first()
            self.assertEqual(user.username, 'test7')
            
            item = Item(id=1, name='paper', price=1200, barcode='testing', description='white')
            db.session.add(item)
            db.session.commit()
            self.assertEqual(user.items, [])
            response = self.app.post('/market', data=dict(sold_item='paper') ,follow_redirects=True)
            self.assertIn(b"Something went wrong with selling paper", response.data)





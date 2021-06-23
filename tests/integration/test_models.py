import sys
sys.path.append("tests/test_base")
from tests.test_base import BaseTest
from market.models import User, Item
from market.__init__ import db

class TestModels(BaseTest):
    def test_user_crud(self):
        with self.app_context:
            user = User(username='qwerty', email_address='test@gmail.com', password_hash='password')
            
            result = db.session.query(User).filter_by(username='qwerty').first()
            self.assertIsNone(result)
            
            db.session.add(user)
            db.session.commit()
            
            result = db.session.query(User).filter_by(username='qwerty').first()
            self.assertIsNotNone(result)
            # assert note in db.session
            
            db.session.delete(user)
            db.session.commit()
            
            result = db.session.query(User).filter_by(username='qwerty').first()
            self.assertIsNone(result)
            
            
    def test_item_crud(self):
        with self.app_context:
            item = Item(name='paper', price=15, barcode='white', description='test')
            
            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNone(result)
            
            db.session.add(item)
            db.session.commit()
            
            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNotNone(result)
            # assert note in db.session
            
            db.session.delete(item)
            db.session.commit()
            
            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNone(result)
            
    def test_can_sell_method(self):
        with self.app_context:
            response = self.app.post('/register', data=dict(
                username='kevin', email_address='okay1@gmail.com',
                password1='password', password2='password'), follow_redirects=True)
            user = db.session.query(User).filter_by(username='kevin').first()
            self.assertTrue(user)
            
            response1 = self.app.post('/register', data=dict(
                username='carl', email_address='okay2@gmail.com',
                password1='password', password2='password'), follow_redirects=True)
            user1 = db.session.query(User).filter_by(username='carl').first()
            self.assertTrue(user1)
            
            
            item = Item(id=1, name="vans", price=2000, barcode=123456, description="white", owner=1)
            db.session.add(item)
            db.session.commit()
            
            items = db.session.query(Item).filter_by(name="vans")

              
            self.assertTrue(items)

               
            self.assertTrue(user.can_sell(item_obj=item))

                
            self.assertFalse(user1.can_sell(item_obj=item))
        
        
        
    def test_password_setter(self):
        with self.app_context:
            self.app.post('/register', data=dict(
                username='steve', email_address='okays@gmail.com',
                password1='password', password2='password'), follow_redirects=True)
            user = db.session.query(User).filter_by(username='steve').first()
            self.assertNotEqual(user.password, 'password')
            print(user.password)
            
            
            
    def test_password_correction(self):
        with self.app_context:
            self.app.post('/register', data=dict(
                username='steves', email_address='okayss@gmail.com',
                password1='password', password2='password'), follow_redirects=True)
            user = db.session.query(User).filter_by(username='steves').first()
            # self.assertEqual(user)
            
            password_hash = User.check_password_correction(user, 'password')
            self.assertTrue(password_hash)

                # Logging in with an incorrect password
            password_hash1 = User.check_password_correction(user, "passwords")
            self.assertFalse(password_hash1)
            
            
          
    def test_item_buy_method(self):
        with self.app_context:
            self.app.post('/register', data=dict(id=1,
                username='jeff', email_address='okay3@gmail.com',
                password1='password', password2='password'), follow_redirects=True)
            
            
            
            item = Item( name="time", price=100, barcode=123457, description="numbers", owner=4)
            db.session.add(item)
            db.session.commit()
            
            
            user = db.session.query(User).filter_by(username='jeff').first()

            user.budget = 1500
            db.session.commit()

            item.buy(user)

            self.assertEqual(user.budget, 1400)
            self.assertEqual(item.owner, 1)
            # items = db.session.query(Item).filter_by(name="time").first()

            # items.buy(user)
            # self.assertTrue(items)  
            
            # self.assertEqual(user.budget, 1400)
            # self.assertEqual(item.owner, user.id)
            
            # item.sell(user)
            # self.assertEqual(user.budget, 1500)
            # self.assertEqual(item.owner, None)
            
    
    def test_item_sell_method(self):
        with self.app_context:
            self.app.post('/register', data=dict(id=1,
                username='jeff', email_address='okay3@gmail.com',
                password1='password', password2='password'), follow_redirects=True)
            
            
            
            item = Item(id=1, name="time", price=200, barcode=123457, description="numbers")
            db.session.add(item)
            db.session.commit()
            
            
            user = db.session.query(User).filter_by(username='jeff').first()

            user.budget = 1400
            db.session.commit()

            item.sell(user)

            self.assertEqual(user.budget, 1600)
            self.assertEqual(item.owner, None)
    
            
            
            
            
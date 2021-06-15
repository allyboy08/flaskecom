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
        item = User(username='qwert', email_address='test@gmail.com', password_hash='passwords', budget=2000, items=['paper']).can_sell(
            Item(name='paper', price=1000, barcode='white', description='test')
        )
        # self.assertTrue(item)
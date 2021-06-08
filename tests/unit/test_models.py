from unittest import TestCase
from market.models import User, Item


class TestModels(TestCase):
    def test_user(self):
        user = User(username='qwerty', email_address='test@gmail.com', password_hash='password')
        
        self.assertEqual(user.username, 'qwerty', "this the username")
        self.assertEqual(user.email_address, 'test@gmail.com', "testing email")
        self.assertEqual(user.password_hash, 'password', "test password")
        
        
    def test_item(self):
        item = Item(name='paper', price=15, barcode='white', description='test')
        
        self.assertEqual(item.name, 'paper', "this the name")
        self.assertEqual(item.price, 15)
        self.assertEqual(item.barcode, 'white')
        self.assertEqual(item.description, 'test')

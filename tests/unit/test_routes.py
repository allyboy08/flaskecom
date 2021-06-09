# import sys
# sys.path.append("tests/test_base")
from tests.test_base import BaseTest
from market.__init__ import db
from market.models import User
from flask import request


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
            
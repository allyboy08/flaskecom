from tests.test_base import BaseTest, db
from market.__init__ import db
from market.models import User
from flask import request
from flask_login import current_user, AnonymousUserMixin
from market.forms import RegisterForm

class TestRegister(BaseTest):
    def test_valid_username(self):
        with self.app:
            user = User(username='qwerty', email_address='test@gmail.com', password_hash='password')
            pass
            
            

# Test in integration


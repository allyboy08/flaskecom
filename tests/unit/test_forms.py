from tests.test_base import BaseTest
from market.__init__ import db
from market.models import User
from flask import request
from flask_login import current_user, AnonymousUserMixin


class TestRegister(BaseTest):
    def test_register_form(self):
        with self.app:
            user = User(username='qwerty', email_address='test@gmail.com', password_hash='password')




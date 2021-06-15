from tests.test_base import BaseTest, db
from market.__init__ import db
from market.models import User
from flask import request
from flask_login import current_user, AnonymousUserMixin
from market.forms import RegisterForm

class TestRegister(BaseTest):
    def test_valid_username(self):
        with self.app:
            # user = User(username='qwerty', email_address='test@gmail.com', password_hash='password')
            response = self.app.post('/register', data=dict(
                username='ken', email_address='okay1@gmail.com',
                password1='python1', password2='python1'
            ), follow_redirects=True)
            user = db.session.query(User).filter_by(username='ken').first()
            self.assertTrue(user)
            valid_error = 'Username already exists! Please try a different username'
            self.assertTrue('Username already exists! Please try a different username', valid_error)
            
    def test_valid_email(self):
        with self.app:
            # user = User(username='qwerty', email_address='test@gmail.com', password_hash='password')
            response = self.app.post('/register', data=dict(
                username='paul', email_address='okay2@gmail.com',
                password1='python1', password2='python1'
            ), follow_redirects=True)
            user = db.session.query(User).filter_by(email_address='okay2@gmail.com').first()
            self.assertTrue(user)
            valid_error = 'Email Address already exists! Please try a different email address'
            self.assertTrue('Email Address already exists! Please try a different email address', valid_error)
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/medicare'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'my_secret_key'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/medicare_test'
    TESTING = True
    WTF_CSRF_ENABLED = False

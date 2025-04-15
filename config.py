class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/medicare'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # This will log all database operations
    SECRET_KEY = 'my_secret_key'

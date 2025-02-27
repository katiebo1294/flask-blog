import os

class Config:
	SECRET_KEY = '9adaa3b46c68320cce53f962cc2d7ac7' #terminal: python3, import secrets, secrets.token_hex(16)
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
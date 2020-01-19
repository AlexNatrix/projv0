import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:j200320rr@localhost/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [] #UBERI ETO EBLAN
    POSTS_PER_PAGE = 3

"""
set MAIL_SERVER = smtp.gmail.com
set MAIL_PORT = 465
set MAIL_USE_SSL = True
set MAIL_USERNAME = 
set MAIL_PASSWORD = 
"""
"""
python -m smtpd -n -c DebuggingServer localhost:8025
$ set FLASK_APP=runner.py
$ set FLASK_DEBUG=1
$ set MAIL_SERVER=localhost
$ set MAIL_PORT=8025
$ flask run
"""



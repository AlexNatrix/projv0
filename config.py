import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [] #UBERI ETO EBLAN
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = 'trnsl.1.1.20200122T180450Z.00e4d4a94fca15fb.3f0d1d69f055b5e7d0cfa23baf6d07391bf07a94'
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
        #os.environ.get('MS_TRANSLATOR_KEY')
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
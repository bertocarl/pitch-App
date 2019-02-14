import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY ='bertocarl'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://berto:fiddlediddle@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://berto:fiddlediddle@localhost/pitch'

    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://berto:fiddlediddle@localhost/pitch_test'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}



import os

class Config:
    """
    General configuration parent class
    contains configuration used in both production and development stages
    """

   #uploads path
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    # email configuration settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")       
    # enable CSRF secret key
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_USERNAME = 'gabrielcoder247'
    MAIL_PASSWORD = '@dushanbe2015'
    SECRET_KEY = '12345'
    #database url setup
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gabrielcoder:dushanbe2015@localhost/healthblog'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gabrielcoder:dushanbe2015@localhost/healthblog'
    DEBUG = True
#server configuration settings

config_options = {
'development':DevConfig,
'production':ProdConfig
} 
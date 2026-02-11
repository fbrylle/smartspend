import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() in ['true', '1', 't']
    SQLALCHEMY_DATABASE_URI='sqlite:///database.db'


class ProductionConfig(Config):
    DEBUG=False
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)



config_options = {
    'development': DevelopmentConfig,
    'production' : ProductionConfig
}
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() in ['true', '1', 't']
    SQL_ALCHEMY_DATABASE_URI='sqlite:///database.db'


class ProductionConfig(Config):
    DEBUG=False
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config_options = {
    'development': DevelopmentConfig,
    'production' : ProductionConfig
}
from flask import Flask
from .routes import main_app
from .extensions import db, bcrypt, migrate, login_manager, csrf
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():

    app = Flask(__name__)

    db_url = os.getenv('DATABASE_URL')

    if db_url and db_url.startswith('postgres://'):
        db_url = db_url.replace('postgres://', 'postgresql://', 1) 

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY', 'dev_key_sample')

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    with app.app_context():
        from . import models


    app.register_blueprint(main_app)


    return app
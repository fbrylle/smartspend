from flask import Flask
from .routes import main_app
from .extensions import db, bcrypt, migrate, login_manager, csrf
import os
from dotenv import load_dotenv
from config import config_options

load_dotenv()


def create_app():

    app = Flask(__name__)

    env = os.environ.get('FLASK_ENV', 'development')

    app.config.from_object(config_options[env])

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    


    app.register_blueprint(main_app)


    return app
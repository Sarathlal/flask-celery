from flask import Flask, request, session, redirect, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv
from config import Config
from celery import Celery
import os

basedir = os.path.abspath(os.path.dirname(__file__))

login_manager = LoginManager()

mail = Mail()

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app():
    app = Flask(__name__)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    from myapp.models import db
    db.init_app(app)

    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)
    login_manager.init_app(app)
    mail.init_app(app)

    celery.conf.update(app.config)

    # with app.app_context():
        # # Register blueprints
        # register_blueprints(app)

    app.app_context().push()

    # Register blueprints
    register_blueprints(app)

    db.create_all()

    return app


### Helper Functions ###
def register_blueprints(app):
    from myapp.auth import auth_blueprint
    from myapp.main import main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint)

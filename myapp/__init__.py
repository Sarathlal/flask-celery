from flask import Flask, request, session, redirect, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import os
basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from myapp.models import db
    db.init_app(app)

    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)

    # with app.app_context():
    #     from myapp.plugin.routes import plugin
    #     app.register_blueprint(plugin)

    #     db.create_all()

    app.app_context().push()
    from myapp.plugin.routes import plugin
    app.register_blueprint(plugin)

    db.create_all()    

    return app

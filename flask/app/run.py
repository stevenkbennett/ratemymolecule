import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
mail = Mail()
bootstrap = Bootstrap()

def create_app():
    """Flask app generator funciton."""
    app = Flask(__name__)
    app.debug = True
    if app.debug:
        from configlocal import Config
        app.config.from_object(Config)
    else:
        from config import Config
        app.config.from_object(Config)

    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)

    from auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/app.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(
              logging.Formatter('{asctime} {levelname}: {message} \
              [in {pathname}:{lineo}]'))
            file_handler.setLevel(logging.INFO)
            app.logger.info('RateMyMolecule startup...')
    return app

from models import *
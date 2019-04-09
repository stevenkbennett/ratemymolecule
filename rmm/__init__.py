
from flask_mail import Mail
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from . import auth

def create_app(config_class=Config):
    app = Flask(__name__)
    login = LoginManager(app)
    login.login_view = 'login'
    app.config.from_object(Config)

    # File handling and logging.
    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/rmm.log',
                                           maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
                                  '%(asctime)s %(levelname)s: %(message)s'
                                  '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.info('RMM Startup.')

    bootstrap = Bootstrap(app)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db, render_as_batch=True)

    mail = Mail(app)

    app.register_blueprint(auth.bp)

    return app

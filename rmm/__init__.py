from flask_mail import Mail
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
mail = Mail()
bootstrap = Bootstrap()

def create_app(config_class=Config):
    """Flask app generator funciton."""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)

    from rmm.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from rmm.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        ...
    return app



from rmm import models

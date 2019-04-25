from flask_mail import Mail
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

mail = Mail(app)

from . import auth
app.register_blueprint(auth.bp)

from rmm import routes, models

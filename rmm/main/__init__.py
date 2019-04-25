from flask import Blueprint

bp = Blueprint('main', __name__)

from rmm.main import routes

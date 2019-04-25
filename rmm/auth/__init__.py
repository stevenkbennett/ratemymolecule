from flask import Blueprint

bp = Blueprint('auth', __name__)

from rmm.auth import routes

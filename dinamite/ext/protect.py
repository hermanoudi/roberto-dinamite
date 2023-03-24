from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt


def init_app(app):
    CSRFProtect(app)
    Bcrypt(app)
import bcrypt
from flask import Flask
from dinamite.ext import configuration

# from flask_wtf.csrf import CSRFProtect
# from flask_bcrypt import Bcrypt


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app


# csrf = CSRFProtect(app)
# bcrypt = Bcrypt(app)


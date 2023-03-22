import os

SECRET_KEY = "vasco"

SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'root',
        servidor = 'localhost',
        database = 'dinamite'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
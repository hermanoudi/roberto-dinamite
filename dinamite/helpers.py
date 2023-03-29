from email import message
from multiprocessing.reduction import send_handle
import os

from click import password_option
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, PasswordField, SubmitField, validators

from dinamite.config import UPLOAD_PATH

upload_path = ''

class FormService(FlaskForm):
    name = StringField('Nome do Serviço', [validators.DataRequired(), validators.Length(min=1, max=200)])
    price = DecimalField('Valor por unidade de medida', [validators.DataRequired(), validators.NumberRange(min=0.1, message='Value cannot be negative')])
    unit = StringField('Unidade de Medida', [validators.DataRequired(), validators.Length(min=1, max=30)])
    salvar = SubmitField('Salvar')


class FormUser(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=1, max=30)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

def reload_file(id):
    print(f"CAMINHO UPLOAD {UPLOAD_PATH}")
    for file_name in os.listdir(UPLOAD_PATH):
        if f'services{id}' in file_name:
            return file_name

    return 'default-drilling-icon.png'

def remove_file(id):
    arquivo = reload_file(id)
    if arquivo != 'default-drilling-icon.png':
        os.remove(os.path.join(UPLOAD_PATH, arquivo))


def init_app(app):
    upload_path = app.configuration.UPLOAD_PATH



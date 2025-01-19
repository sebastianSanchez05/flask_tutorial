from flask_wtf import FlaskForm
from wtforms.fields import *

class LoginFormModel(FlaskForm):
    nombre = StringField('Nombre')
    contraseña = PasswordField('Contraseña')
    submit = SubmitField('Nombre')
    
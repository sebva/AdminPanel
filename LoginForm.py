from wtforms import Form, PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
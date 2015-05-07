from flask.ext.babel import lazy_gettext
from wtforms import Form, PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField(lazy_gettext('Username'), validators=[DataRequired()])
    password = PasswordField(lazy_gettext('Password'), validators=[DataRequired()])
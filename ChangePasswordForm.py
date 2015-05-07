from flask.ext.babel import lazy_gettext
from wtforms import Form, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class ChangePasswordForm(Form):
    old_password = PasswordField(lazy_gettext('Current password'), validators=[DataRequired()])
    new_password = PasswordField(lazy_gettext('New password'), validators=[
        DataRequired(),
        Length(min=8, message=lazy_gettext('Password too short'))
    ])
    new_password_2 = PasswordField(lazy_gettext('New password (again)'), validators=[
        DataRequired(),
        EqualTo('new_password', message=lazy_gettext('Passwords must match'))
    ])
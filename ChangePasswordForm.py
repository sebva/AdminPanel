from wtforms import Form, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class ChangePasswordForm(Form):
    old_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=8, message='Password too short')])
    new_password_2 = PasswordField('New password (again)',
                                   validators=[DataRequired(), EqualTo('new_password', message='Passwords must match')])
from flask.ext.babel import lazy_gettext
from wtforms import PasswordField, Form, SelectField, StringField, DateField
from wtforms.validators import DataRequired, Length, URL, Optional, EqualTo
from wtforms_components import PhoneNumberField, EmailField, Email

class NewEmployeeForm(Form):
    name = StringField(lazy_gettext('Name'), validators=[DataRequired()])
    email = EmailField(lazy_gettext('E-mail'), validators=[DataRequired(), Email()])
    password = PasswordField(lazy_gettext('Password'), validators=[
        DataRequired(),
        Length(min=4, message=lazy_gettext('Password too short'))
    ])
    password2 = PasswordField(lazy_gettext('Password (again)'), validators=[
        DataRequired(),
        EqualTo('password')
    ])
    tel_number = PhoneNumberField(lazy_gettext('Tel. number'),
                                  country_code='CH', display_format='national', validators=[Optional()])
    mobile_number = PhoneNumberField(lazy_gettext('Mobile number'),
                                  country_code='CH', display_format='national', validators=[Optional()])
    gender = SelectField(lazy_gettext('Gender'), choices=[
        ('male', lazy_gettext('Male')),
        ('female', lazy_gettext('Female'))
    ])
    birthdate = DateField(lazy_gettext('Birth date'), format='%d.%m.%Y', validators=[Optional()])
    website = StringField(lazy_gettext('Website'), validators=[URL(), Optional()])

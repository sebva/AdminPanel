from wtforms import PasswordField, Form, SelectField, StringField, DateField
from wtforms.validators import DataRequired, Length, URL, Optional, EqualTo
from wtforms_components import PhoneNumberField, EmailField, Email

class NewEmployeeForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, message='Password too short')])
    password2 = PasswordField('Password (again)', validators=[DataRequired(), EqualTo('password')])
    tel_number = PhoneNumberField('Tel. number', country_code='CH', display_format='national', validators=[Optional()])
    mobile_number = PhoneNumberField('Mobile number', country_code='CH', display_format='national', validators=[Optional()])
    gender = SelectField('Gender', choices=(('male', 'Male'), ('female', 'Female')))
    birthdate = DateField('Birth date', format='%d.%m.%Y', validators=[Optional()])
    website = StringField('Website', validators=[URL(), Optional()])

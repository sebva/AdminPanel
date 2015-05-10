from flask.ext.babel import lazy_gettext
from wtforms import Form, SelectField


class UpdateStatusForm(Form):
    status = SelectField(lazy_gettext('Status'), choices=[
        ('NEW', lazy_gettext('New')),
        ('ACCEPTED', lazy_gettext('In progress')),
        ('FIXED', lazy_gettext('Fixed')),
        ('REJECTED', lazy_gettext('Rejected'))
    ])
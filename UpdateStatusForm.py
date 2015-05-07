from flask.ext.babel import lazy_gettext
from wtforms import Form, SelectField


class UpdateStatusForm(Form):
    status = SelectField(lazy_gettext('Status'), choices=[
        ('new', lazy_gettext('New')),
        ('in_progress', lazy_gettext('In progress')),
        ('fixed', lazy_gettext('Fixed')),
        ('rejected', lazy_gettext('Rejected'))
    ])
from wtforms import Form, SelectField


class UpdateStatusForm(Form):
    status = SelectField('Status', choices=[
        ('new', 'New'), ('in_progress', 'In progress'), ('fixed', 'Fixed'), ('rejected', 'Rejected')
    ])
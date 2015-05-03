# coding=utf-8

from flask import Flask, render_template, url_for, redirect, request, flash
from flask_bootstrap import Bootstrap
from suds.client import Client as SudsClient

from ChangePasswordForm import ChangePasswordForm
from LoginForm import LoginForm
from LoginManager import login_required, check_login, login_user, logout, get_current_user, change_password, \
    get_current_organization
from NewEmployeeForm import NewEmployeeForm


app = Flask(__name__)
app.debug = True
app.secret_key = "\n\xebU\x9b\x8a\x1aO\x91\x15\x84\xbe\x1dx\xccD\xba\x16\x94\xc5\xa4\x03'\xe5\x16"
Bootstrap(app)

url = 'http://46.101.157.31:8888/eRepair/Services?wsdl'
client = SudsClient(url=url, cache=None)
service = client.service

# region Routes
@app.route("/login", methods=["GET", "POST"])
def login_action():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = check_login(service, form.username.data, form.password.data)
        if user is not None:
            login_user(service, user)
            return redirect(url_for('index_action'))
        else:
            flash('Invalid credentials', category='warning')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_action():
    logout()
    return redirect(url_for('login_action'))


def get_session_args():
    return {
        'organization': get_current_organization(),
        'user': get_current_user()
    }


@app.route('/')
@login_required
def index_action():
    args = {}
    args.update(get_session_args())
    return render_template('index.html', **args)


@app.route('/map')
@login_required
def map_action():
    args = {}
    args.update(get_session_args())
    return render_template('map.html', **args)


@app.route('/details/<object_id>')
@login_required
def details_action(object_id):
    args = {}
    args.update(get_session_args())
    return render_template('details.html', **args)


@app.route('/users', methods=['GET', 'POST'])
@login_required
def users_action():
    form = NewEmployeeForm(request.form)
    if request.method == 'POST' and form.validate():
        new_employee = {
            'oremail': get_current_organization()['email'],
            'name': form.data['name'],
            'email': form.data['email'],
            'password': form.data['name'],
            'gender': form.data['gender'],
            'website': form.data['website']
        }
        if form.data['tel_number'] is not None:
            new_employee['tel_number'] = form.data['tel_number'].e164
        if form.data['mobile_number'] is not None:
            new_employee['mobile_number'] = form.data['mobile_number'].e164
        if form.data['birthdate'] is not None:
            new_employee['birthdate'] = str(form.data['birthdate'])

        result = service.addEmployee(newEmployee=new_employee)
        if result > 0:
            flash('Employee successfully added', category='success')
            form = NewEmployeeForm()
        else:
            flash('There was a problem adding the employee, please verify your input and try again', category='error')

    employees = service.getAllEmployees(OrganizationEmail=get_current_organization()['email'])
    args = {
        'employees': [dict(x) for x in employees],
        'form': form
    }
    args.update(get_session_args())
    return render_template('users.html', **args)


@app.route('/change_password', methods=["GET", "POST"])
@login_required
def change_password_action():
    form = ChangePasswordForm(request.form)
    if request.method == 'POST':
        if form.validate():
            if change_password(service, get_current_user()['email'], form.old_password.data, form.new_password.data):
                flash("Password successfully changed!", category='success')
        else:
            flash('Please check your input', category='warning')

    args = {'form': form}
    args.update(get_session_args())
    return render_template('change_password.html', **args)

# endregion

if __name__ == '__main__':
    app.run()

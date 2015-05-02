# coding=utf-8

from flask import Flask, render_template, url_for, redirect, request, flash
from flask_bootstrap import Bootstrap
from suds.client import Client as SudsClient

from ChangePasswordForm import ChangePasswordForm
from LoginForm import LoginForm
from LoginManager import login_required, check_login, login_user, logout, get_current_user, change_password


app = Flask(__name__)
app.debug = True
app.secret_key = "\n\xebU\x9b\x8a\x1aO\x91\x15\x84\xbe\x1dx\xccD\xba\x16\x94\xc5\xa4\x03'\xe5\x16"
Bootstrap(app)

url = 'http://46.101.157.31:8888/eRepair/Services?wsdl'
client = SudsClient(url=url, cache=None)
service = client.service

# region Routes
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = check_login(service, form.username.data, form.password.data)
        if user is not None:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', category='warning')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_action():
    logout()
    return redirect(url_for('login'))


def get_session_args():
    return {
        'organization': u'Ville de Neuchâtel',
        'user': get_current_user()
    }


@app.route('/')
@login_required
def index():
    args = {}
    args.update(get_session_args())
    return render_template('index.html', **args)


@app.route('/map')
@login_required
def map():
    args = {}
    args.update(get_session_args())
    return render_template('map.html', **args)


@app.route('/details/<object_id>')
@login_required
def details(object_id):
    args = {}
    args.update(get_session_args())
    return render_template('details.html', **args)


@app.route('/users')
@login_required
def users():
    args = {}
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

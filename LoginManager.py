# coding=utf-8
from functools import wraps

from flask import session, redirect, url_for


def check_login(service, username, password):
    user = service.employeeLogIn(employeeName=username, Password=password)
    if user is not None:
        return dict(user)
    else:
        return None


def change_password(service, email, old_password, new_password):
    return True
    # return service.changeEmployeePassword(**{'E-mail': email, 'oldPassword': old_password, 'newPassword': new_password})


def login_user(service, user):
    session['logged_in'] = True
    session['user'] = user
    session['organization'] = dict(service.getRelatingOrganization(employeeEmail=user['email']))


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            if session['logged_in']:
                return func(*args, **kwargs)
        except KeyError:
            pass
        return redirect(url_for('login_action'))

    return decorated_view


def get_current_user():
    return session['user']


def get_current_organization():
    return session['organization']

def logout():
    session['logged_in'] = False
    session['user'] = None
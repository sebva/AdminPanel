from functools import wraps

from flask import session, redirect, url_for


def check_login(service, username, password):
    if username == 'toto' and password == 'pass':
        return {'name': username, 'pass': password, 'email': 'toto@example.com'}
    else:
        return None
    # return service.userLogIn(userName=username, Password=password)


def change_password(service, email, old_password, new_password):
    return True
    # return service.changeEmployeePassword(**{'E-mail': email, 'oldPassword': old_password, 'newPassword': new_password})

def login_user(user):
    session['logged_in'] = True
    session['user'] = user


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            if session['logged_in']:
                return func(*args, **kwargs)
        except KeyError:
            pass
        return redirect(url_for('login'))

    return decorated_view


def get_current_user():
    return session['user']


def logout():
    session['logged_in'] = False
    session['user'] = None
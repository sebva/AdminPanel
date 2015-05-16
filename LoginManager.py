# coding=utf-8
from functools import wraps

from flask import session, redirect, url_for


def check_login(service, username, password):
    """
    Check if the username/password couple is valid
    :param service: A reference on the WSDL service endpoint
    :param username: The username
    :param password: The password
    :return: Information about the user if login is successful, None otherwise
    """
    user = service.employeeLogIn(employeeName=username, Password=password)
    if user is not None:
        return dict(user)
    else:
        return None


def change_password(service, email, old_password, new_password):
    """
    Change the password associated to the provided employee
    :param service: A reference on the WSDL service endpoint
    :param email: The e-mail associated to the employee
    :param old_password: The old password
    :param new_password: The new password
    :return: True if successful, False otherwise
    """
    return service.changeEmployeePassword(**{'E-mail': email, 'oldPassword': old_password, 'newPassword': new_password})


def login_user(service, user):
    """
    Store the login information in a session variable
    :param service: A reference on the WSDL service endpoint
    :param user: The user information returned by check_login
    """
    session['logged_in'] = True
    session['user'] = user
    session['organization'] = dict(service.getRelatingOrganization(employeeEmail=user['email']))


def login_required(func):
    """
    Wrapper to place on routes where the user must be logged in to access
    """

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
    """
    Get the information of the logged in user
    :return: The information as a dict
    """
    return session['user']


def get_current_organization():
    """
    Get the information about the organization of the logged in user
    :return: The information as a dict
    """
    return session['organization']


def logout():
    """
    Log out the user
    """
    session['logged_in'] = False
    session['user'] = None

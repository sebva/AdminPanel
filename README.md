# Admin panel of the E-Repair system

This repository hosts the Admin Panel component of the E-Repair system. E-Repair is a project developed during the 
E-Government Frameworks course taught at the [University of Neuchâtel](http://www.unine.ch). It is a system tailored
for swiss municipalities. It will enable swiss residents to report objects that need to be repaired to the responsible 
municipality.

This Admin Panel is used by municipality employees to receive and update repairment requests.

As of the time of writing, a live demo is available at https://erepair.herokuapp.com

## Usage

The application is designed to run on Python 2.7. The easiest way to install the dependencies is by using virtualenv 
and pip. To do so, install pip and virtualenv if needed (use your favorite search engine for further guidance), and 
then execute the following commands in the folder where this readme is located:

```shell
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python AdminPanel.py
```

You will then be able to access the application by using the address provided in the console output.

For subsequent launches, only the following commands need to be issued:

```shell
$ source venv/bin/activate
$ python AdminPanel.py
```

## Architecture

The admin panel is a [Flask](http://flask.pocoo.org/) application. It connects to the backend service with the WSDL 
protocol using the [Flask-Spyne](https://pypi.python.org/pypi/Flask-Spyne/0.2) library.

The application code is primarily concentrated in the [AdminPanel.py](./AdminPanel.py) file. Each form that can be sent 
by a user is created using WTForms, and has a dedicated file ending in ...Form.py. The 
[LoginManager](./LoginManager.py) is a collection of functions related to login concerns. The [static](./static) 
directory hosts the static files (CSS/JS/Images). The [templates](./templates) directory hosts the HTML templates.

The template engine is provided by Flask, and is [jinja2](http://jinja.pocoo.org/). The 
[base.html](./templates/base.html) file is extended by every other template file and contains the basic structure of 
the UI. We use the [Bootstrap 3](http://getbootstrap.com/) framework through the 
[Flask-Bootstrap](https://github.com/mbr/flask-bootstrap/) library.

## Internationalization

i18n capabilities are provided by [Flask-Babel](https://pythonhosted.org/Flask-Babel/). To mark a string for
translation, it has to be surrounded by _() like that:
 
```python
_('String to translate')
```

In a jinja2 template file, the following construct can be used:

```html+jinja
{% trans %}String to translate{% endtrans %}
```

When a string is marked as translatable or is changed, the [messages.pot](./messages.pot) file and all per-language 
.po files have to be updated. The following commands will generate them:

```shell
$ pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
$ pybabel update -i messages.pot -d translations
```

After that, translators can add their translations to .po files. For example, a French translator will modify 
[translations/fr/LC_MESSAGES/messages.po](./translations/fr/LC_MESSAGES/messages.po). When the translations are ready,
they need to be compiled to .mo files:

```shell
$ pybabel compile -d translations
```

## Screenshots

Login page

<img src="https://dl.dropboxusercontent.com/u/31349479/erepair-screenshots/login.png" width=728px>

Index page for logged in user

<img src="https://dl.dropboxusercontent.com/u/31349479/erepair-screenshots/index.png" width=728px>

Map of pending interventions

<img src="https://dl.dropboxusercontent.com/u/31349479/erepair-screenshots/map.png" width=728px>

Employee management

<img src="https://dl.dropboxusercontent.com/u/31349479/erepair-screenshots/users.png" width=728px>

Password change

<img src="https://dl.dropboxusercontent.com/u/31349479/erepair-screenshots/password.png" width=728px>

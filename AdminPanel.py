# coding=utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from suds.client import Client as SudsClient

app = Flask(__name__)
app.debug = True
Bootstrap(app)

url = 'http://46.101.157.31:8888/eRepair/Services?wsdl'
client = SudsClient(url=url, cache=None)
service = client.service

template_args = {
    'organization': u'Ville de Neuchâtel'
}

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    args = {}
    args.update(template_args)
    return render_template('index.html', **args)

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/details/<object_id>')
def details(object_id):
    return render_template('details.html')

@app.route('/users')
def users():
    return render_template('users.html')

if __name__ == '__main__':
    app.run()

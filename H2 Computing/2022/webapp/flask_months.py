import flask
from flask import url_for
app = flask.Flask(__name__)

NAMES = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

@app.route('/home')
def home():
    return 'Home'

@app.route('/issue')
def error():
    return ('', 500)

@app.route('/')
def index():
    return '<h1>Welcome!</h1> <b>Hello,</b> <i>World!</i>'


@app.route('/<int:month>/')
def name_month(month):
    if month in range(1, 13):
        return f'Month {month}: {NAMES[month-1]}'
    return 'Invalid month'


@app.route('/compare/<float:temp>/')
def compare_temp(temp):
    if temp > 35.5:
        return 'It\'s hot!'
    if temp < 25.5:
        return 'It\'s cold!'
    return 'It\'s normal!'


@app.route('/greet/')
def greet():
    return 'Hello!'

@app.route('/greet/<name>/')
def greet_name(name):
    return 'Hello, {}!'.format(name)

@app.route('/data/', methods=['POST'])
def post_data():
    return 'You are using POST'
@app.route('/data/', methods=['GET'])
def get_data():
    return 'You are using GET'


# How to implement changed url

@app.route('/new_url/')
def moved_index():
    return 'You have reached the new URL!'


@app.route('/iemb')
def iemb():
    return flask.redirect(url_for('moved_index'))
# End of implementation for changed url


if __name__ == '__main__':
    app.run(port=11111)
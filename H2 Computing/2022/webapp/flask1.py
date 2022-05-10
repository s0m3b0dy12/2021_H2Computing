import flask

app = flask.Flask(__name__)


@app.route('/report')
def generate_report():
    return 'Everything is awesome'


@app.route('/readme.txt')
def readme():
    return 'READ ME'


@app.route('/')
def index():
    return 'Routed to index()'


@app.route('/css')
def css():
    return 'Routed to css()'


# Case-sensitive note
"""
Routes are case sensitive so 
http://127.0.0.1:5000/CSS instead of 
http://127.0.0.1:5000/css 
will lead to a 404 error
"""


@app.route('/no_slash')
def no_slash():
    return 'Routed to no_slash()'


@app.route('/optional_slash/')
def optional_slash():
    return 'Routed to optional_slash()'


# Trailing slashes note
"""
A request's path and a route's path must match exactly for the route to be chosen. This includes trailing slashes
so 
# http://127.0.0.1:5000/css/
is not the same as 
# http://127.0.0.1:5000/css

However, when flask fails to find a route for a path that does not end with a slash it will append a slash to the path
and try again before displaying the 404 error if path not found

On that note, flask does not try to remove the slash
"""


@app.route('/one/')
@app.route('/one/two/')
@app.route('/three/two/one')
def multiple():
    return 'Routed to multiple()'
# Multiple routing
"""
Routing multiple paths to the same function can be done like the above
"""


@app.route('/string/<s>/')
def string_variable(s):
    # The path by default takes in string
    return f'Routed to string_variable({s})'


@app.route('/integer/<int:i>/') # <int:i> is how we write code to allow the program to anticipate integers
def integer_variable(i):
    return f'Routed to integer_variable({i})'
# This does not include negative integers as '-' is not recognised as integer so the integers have to be positive

@app.route('/post_only/', methods=['POST'])
def post_only():
    return 'Routed to post_only()'
# Using of methods
"""
GET method is used to retrieve data from a server without making changes to the server data
POST method is used to submit or make changes to data in the server 
The above method will show a "Method not allowed" error as a POST request would need to be accessed by
submitting a HTML form.
"""


if __name__ == "__main__":
    app.run()
    # 5000 is the default port number defined by flask

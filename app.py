#!/home/flask/venv/bin/python
from flask import Flask, send_from_directory, render_template, jsonify, request, Response
import os
from functools import wraps

app = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated



# Index Page.

@app.route('/')
def index():
    return "Hello, World! Welcome to TrinketStore!"
#@app.route('/static/data.txt/writeto/<write>')
#def writeto(write):
#    with open("static/data.txt", "a") as myfile:
#         myfile.write("%s\n" % write)
#    return "True"


# Reading .txt file.
@app.route('/static/<path:path>')
def send_file(path):
    return send_from_directory(os.path.join(app.root_path, 'static'), path)

## Demonstration of HTML and favicon usage.

#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', name=name)

def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


@app.route("/data.txt/secuwrite/<write>", methods=["GET"])
def secuwrite(write):
    if request.remote_addr == "104.196.5.121":
        with open("static/data.txt", "a") as myfile:
            myfile.write("%s\n" % write)
	    return "True"
    else:
	return "You're going have to be more creative than <i>that.<i>"

# Run server.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)


# Extras


## Name page: input collection practice using https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

#@app.route('/hello/<name>')
#def hello_name(name):
#    return "Hello, {}!".format(name)
#
#@app.route('/user/<username>')
#def show_user_profile(username):
#    # show the user profile for that user
#    return 'User %s' % username # This official way, from Flask, is probably better.

## Server shutdown.
#
#def shutdown_server():
#    func = request.environ.get('werkzeug.server.shutdown')
#    if func is None:
#        raise RuntimeError('Not running with the Werkzeug Server')
#    func()


#from flask import request

#@app.route('/shutdown', methods=['POST']) # Okay, I figured it out. While this could be a GET, `curl -X POST [url]:[port]/shutdown` will do it really well.

#def shutdown():
#    shutdown_server()
#    return 'Server shutting down...'

# Favicon

#import os
#from flask import send_from_directory

# Favicon setup.

#@app.route('/static/favicon.ico')
#def favicon():
#    return send_from_directory(os.path.join(app.root_path, 'static'),
#                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

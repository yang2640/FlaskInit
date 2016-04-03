from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# dynamic route, the rounts to have dynamic (user-defined variable)
@app.route('/usr/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' % (name)


# contexts only available to current thread
# application contexts: current_app, g
# Request context: request and session
# request: encapsulates the cotents of HTTP request
# session: user session, dictionary, between requests
@app.route('/useragent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % (user_agent)

# make response by make_response function, and return
@app.route('/response')
def responseTest():
    response = make_response('<h1>Carry a cookie !</h1>')
    response.set_cookie('answer', '10')
    return response


# redirect
@app.route('/redirect')
def redirectTest():
    return redirect('http://www.google.com')
# abort
@app.route('/abort')
def abort_test():
    abort(404)
    return '<h1>Hello !</h1>'


if __name__ == '__main__':
    manager.run()

from flask import Flask
from flask import request

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)

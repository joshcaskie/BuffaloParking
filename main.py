#https://bottlepy.org/docs/dev/tutorial.html
from bottle import Bottle, run, get, post, request
import functions

app = Bottle()

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/bob")
def bob():
    return "Bob says hi!"

@app.route('/display-lots')
def lots():
    return functions.display_lots()

# get "Gets" something from the Server and sends it to the Client
@app.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" /> 
        </form>
    '''
#The <type="submit"> is the button that's used for the form submission!
#In the first line, method="post" is recognized by the bottle!

# post grabs data from the client!
@app.post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if functions.check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


run(app, host='localhost', port=8080, debug=True)
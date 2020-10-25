#https://bottlepy.org/docs/dev/tutorial.html
from bottle import Bottle, run, get, post, request, redirect, static_file
import functions
import json

app = Bottle()

#Front End calls!!
@app.get('/')
def lot_submit():
    return static_file(filename="homepage.html", root="")
@app.get('/frontend.js') #include JS in server
def frontend_js():
    return static_file(filename="frontend.js", root="")
@app.get('/display-current')
def display():
    #print("It's working!")
    ans = functions.display_lots()
    return json.dumps(ans)
    #return "yurdddd"



@app.post('/')
def lot_grab():
    #Use a dynamic route!
    lot = request.forms.get("lot")
    redirect("/" + lot) #better way to do this? Formatting strings?

@app.route('/fargo')
def fargo():
    lot = "fargo"
    return "Welcome to Fargo!"

@app.route('/jarvis')
def jarvis():
    lot = "jarvis"
    return "Welcome to Jarvis!"


run(app, host='localhost', port=8080, debug=True)
#https://bottlepy.org/docs/dev/tutorial.html
from bottle import Bottle, run, get, post, request, redirect, static_file
import functions
import html

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
    return functions.display_lots()


@app.post('/')
def lot_grab():
    #Use a dynamic route!
    lot = request.forms.get("lot")
    lot = html.escape(lot) #https://docs.python.org/3/library/html.html
    if lot == "Fargo" or lot == "Jarvis":
        redirect("/" + lot) #better way to do this? Formatting strings?
    else:
        return "<h2> Not a parking lot </h2>"


@app.get('/Fargo')
def fargo():
    lot = "fargo"
    return '''Welcome to Fargo Lot! </br>
        <form action='/fargo-parked' method="post">
            <input value="Park" type="submit" />
        </form>
    '''
@app.post('/fargo-parked')
def fargo_parked():
    functions.enter_lot("fargo")
    return '''Welcome to Fargo Lot! </br>
        <form action='/fargo-leave' method="post">
            <input value="Leave" type="submit" />
        </form>
    '''
@app.post('/fargo-leave')
def fargo_leave():
    functions.leave_lot("fargo")
    return "Thank you for parking at Fargo!"



@app.route('/Jarvis')
def jarvis():
    lot = "jarvis"
    return '''Welcome to Jarvis Lot! </br>
        <form action='/jarvis-parked' method="post">
            <input value="Park" type="submit" />
        </form>
    '''
@app.post('/jarvis-parked')
def jarvis_parked():
    functions.enter_lot("jarvis")
    return '''Welcome to Jarvis Lot! </br>
        <form action='/jarvis-leave' method="post">
            <input value="Leave" type="submit" />
        </form>
    '''
@app.post('/jarvis-leave')
def jarvis_leave():
    functions.leave_lot("jarvis")
    return "Thank you for parking at Jarvis!"


run(app, host='localhost', port=8080, debug=True)
def check_login(username, password):
    x = True
    if username != "josh":
        x = False
    if password != "josh":
        x = False
    return x

# JSON --> https://docs.python.org/3/library/json.html
import json
#json.dumps(_) --> puts INTO json
#json.parse(_) --> takes OUT of json


#Database --> https://docs.python.org/3/library/sqlite3.html
import sqlite3
data = sqlite3.connect('parking.db')
d = data.cursor()

d.execute('''CREATE TABLE parkinglots (name, size)''')

d.execute("INSERT INTO parkinglots VALUES ('fargo',100)")
d.execute("INSERT INTO parkinglots VALUES ('jarvis',200)")

data.commit()
data.close()

def display_lots():
    parking = sqlite3.connect('parking.db')
    p = parking.cursor()

    lots = p.execute("SELECT * FROM parkinglots")

    ans = ""

    for i in lots:
        ans = ans + json.dumps(i) + "\n"

    parking.commit()
    parking.close()

    return ans
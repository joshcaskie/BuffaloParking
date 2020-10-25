# JSON --> https://docs.python.org/3/library/json.html
#json.dumps(_) --> puts INTO json
#json.loads(_) --> takes OUT of json
import json


#Database --> https://docs.python.org/3/library/sqlite3.html
import sqlite3
data = sqlite3.connect('parking.db')
d = data.cursor()

d.execute("DROP TABLE parkinglots") #Temporary solution to not having the parking lots insert EVERY time
d.execute('''CREATE TABLE IF NOT EXISTS parkinglots (name, size)''')

d.execute("INSERT INTO parkinglots VALUES ('fargo',100)")
d.execute("INSERT INTO parkinglots VALUES ('jarvis',200)")

#test = d.execute("SELECT * FROM parkinglots")
#for i in test:
    #print({i[0]:i[1]})

data.commit()
data.close()

def display_lots():
    parking = sqlite3.connect('parking.db')
    p = parking.cursor()

    lots = p.execute("SELECT * FROM parkinglots")

    ans = {}

    for i in lots:
        ans[i[0]] = i[1]; #This should make it easier for the JS side --> convert to Object

    parking.commit()
    parking.close()

    return json.dumps(ans)
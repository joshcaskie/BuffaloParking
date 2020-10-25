# BuffaloParking
UBHacking 2020

There's a LOT of room for improvement but here's a first attempt at a parking tracker for UB. 
(Except for this semester because of COVID-19) Parking has been a problem at UB for many years so I wanted to create a way to reduce the tension surrounding it.

Potential improvements:
* Much better user-interface. This is just bare HTML.
* Better security and usability (i.e., at the moment, users can park their cars, close out of the app, and never mark the car as unparked). 
* Use a better database than SQLite.
* Live refresh on the page when things change. 
* Hosting on a web site.
* Deploy in a mobile app.
* Have use of Siri or HandsFreeLink in some fashion so while driving, users can ask "where's the closest parking lot to my location" and be given directions.
* Or potentially even include sensors at the entrances of parking lots to track the number of cars that go in and out since some users will probably use the app to find empty spots but then not mark they have parked.
* etc.

Edge cases that need implementation:
* Hitting 0 spots
* Having spots go upwards above the limit due to security and design flaws
* etc.

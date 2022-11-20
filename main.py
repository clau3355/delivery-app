import os

from flask import Flask, request, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBXo-OEh8h8LtwbjdK5FVTkIEQi6q5Cass"
GoogleMaps(app)
    
@app.route('/')

def my_map(): 
   
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )

    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )

    return render_template('prueba_mapa.html', mymap=mymap, sndmap=sndmap)



# commit nuevo

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

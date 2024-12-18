from flask import Flask, request, jsonify, render_template
from geopy.distance import geodesic
import overpass as op
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/find_stores", methods=["POST"])
def find_stores():
    """
    Find nearby stores with photos using Google Places API.
    """
    data = request.get_json()
    user_latitude = data["latitude"]
    user_longitude = data["longitude"]

    # Fetch stores with photos

    #stores_with_photos = op.fetch_nearby_stores_with_photos(user_latitude, user_longitude)
    stores_with_photos = op.fetch_nearby_stores_with_photos(29.993464398658432, 31.310755687526143)

    # Add Google Maps links to each store
    for store in stores_with_photos:
        store["google_maps_link"] = f"https://www.google.com/maps/dir/{user_latitude},{user_longitude}/{store['location'][0]},{store['location'][1]}"

    return jsonify(stores_with_photos)

if __name__ == "__main__":
    app.run(debug=True)

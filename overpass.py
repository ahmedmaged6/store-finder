import requests

def fetch_nearby_stores_with_photos(latitude, longitude, radius=1000, place_type="store"):
    """
    Fetch nearby stores using Google Places API and include photos.
    :param latitude: Latitude of the user's location.
    :param longitude: Longitude of the user's location.
    :param radius: Search radius in meters.
    :param place_type: Type of place to search for.
    :return: A list of stores with name, location, address, and photos.
    """
    api_key = "AIzaSyDSi3oBKowwDjoKHe1l5GkWpajXWC7qm6k"  # Replace with your Google Maps API key
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{latitude},{longitude}",
        "radius": radius,
        "type": place_type,
        "key": api_key,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        stores = []
        for place in data.get("results", []):
            photo_url = None
            # Check if photos are available
            if "photos" in place:
                photo_reference = place["photos"][0]["photo_reference"]
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
            stores.append({
                "name": place["name"],
                "location": (
                    place["geometry"]["location"]["lat"],
                    place["geometry"]["location"]["lng"]
                ),
                "address": place.get("vicinity", "Address not available"),
                "photo_url": photo_url,
            })
        return stores
    else:
        print("Error fetching data:", response.status_code, response.text)
        return []

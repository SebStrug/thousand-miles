from flask import Flask, render_template, request
import requests

import find_city

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    ip_addr = request.remote_addr
    resp = requests.get(f"https://geolocation-db.com/json/{ip_addr}")
    data = resp.json()
    your_city = data.get('city', 'London')
    try:
        lat_str, lng_str = data.get("latitude"), data.get("longitude")
        lat, lng = float(lat_str), float(lng_str)
    # handle no lat/long returned, default to London
    except ValueError:
        lat, lng = 51.5074, 0.1278
    lover_city = find_city.find_my_city(lat, lng)
    return render_template(
        "home.html", your_city=your_city, lover_city=lover_city
    )


if __name__ == "__main__":
    app.run()

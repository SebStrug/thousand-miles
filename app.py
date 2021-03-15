from flask import Flask, render_template, request
import requests

import find_city

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    ip_addr = request.remote_addr
    resp = requests.get(f"https://geolocation-db.com/json/{ip_addr}")
    data = resp.json()
    lat, long = data.get("latitude"), data.get("longitude")
    lover_city = find_city.find_my_city(lat, long)
    return render_template(
        "home.html", your_city=data.get("city", ""), lover_city=lover_city
    )


if __name__ == "__main__":
    app.run()

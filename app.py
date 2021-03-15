from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    ip_addr = request.remote_addr
    resp = requests.get(f'https://geolocation-db.com/json/{ip_addr}')
    data = resp.json()
    lat, long = data.get('latitude'), data.get('longitude')
    return render_template("home.html", city=data.get('city', ''))


if __name__ == "__main__":
    app.run()

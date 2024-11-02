from flask import Flask, render_template, request, url_for,redirect
from time import time
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/login", methods=["post", "get"])
def login():
    print(request.method)
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        return render_template("login.html", name=name, password=password)
    return render_template("login.html", name="undefined", password="undefined")


@app.route("/gender/<name>")
def genderize(name):
    print(name.title())
    data = requests.get(f"https://api.genderize.io?name={name.title()}")
    res1 = data.json()
    data = requests.get(f"https://api.agify.io?name={name.title()}")
    res = data.json()
    return render_template("index.html", gender=res1["gender"], age=res["age"])


if __name__ == "__main__":
    app.run(debug=True)

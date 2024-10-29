from flask import Flask, render_template, request
from dati import pievienot_skolenu
import sqlite3

conn = sqlite3.connect("dati.db")

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def skoleni():
    if request.method == "POST":
        vards = request.form["name"]
        uzvards = request.form["lastname"]
        pievienot_skolenu(vards, uzvards)
        dati = vards+" "+uzvards
        return render_template("skoleni.html", aizsutitais = dati)
    return render_template("skoleni.html")

@app.route("/skolotaji", methods=["POST", "GET"])
def skolotaji():
    return render_template("skolotaji.html")

@app.route("/atzimes", methods=["POST", "GET"])
def atzimes():
    return render_template("atzimes.html")

@app.route("/tabula", methods=["POST", "GET"])
def tabula():
    return render_template("tabula.html")


if __name__ == '__main__':
    app.run(port = 5000)
from flask import Flask, render_template, request
from dati import pievienot_skolenu, pievienot_skolotaju, pievienot_atzime, iegut_skolenus, iegut_skolotaju, iegut_atzime
import sqlite3

conn = sqlite3.connect("dati.db")

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def skoleni():
    skolenu_db = iegut_skolenus()
    print(skolenu_db)
    if request.method == "POST":
        vards = request.form["name"]
        uzvards = request.form["lastname"]
        if vards and uzvards:
          pievienot_skolenu(vards, uzvards)
        dati = vards+" "+uzvards
        return render_template("skoleni.html", aizsutitais = dati, skoleni = skolenu_db)
    return render_template("skoleni.html")

@app.route("/skolotaji", methods=["POST", "GET"])
def skolotaju():
    skolotaju_db = iegut_skolotaju()
    print(skolotaju_db)
    if request.method == "POST":
        skvards = request.form["skvards"]
        skuzvards = request.form["skuzvards"]
        if skvards and skuzvards:
            pievienot_skolotaju(skvards, skuzvards)
        dati = skvards+" "+skuzvards
        return render_template("skolotaji.html", aizsutitais = dati, skolotaju = skolotaju_db)
    return render_template("skolotaji.html")

@app.route("/atzimes", methods=["POST", "GET"])
def atzimes():
    atzime_db = iegut_atzime()
    print(atzime_db)
    if request.method == "POST":
        atname = request.form["atvards"]
        atsubject = request.form["atsubject"]
        grade = request.form["grade"]
        pievienot_atzime(atname, atsubject, grade)
        dati = atname+" "+atsubject+" "+grade
        return render_template("atzimes.html", aizsutitais = dati, atzime = atzime_db)
    return render_template("atzimes.html")

@app.route("/tabula", methods=["POST", "GET"])
def tabula():
    skolenu_db = iegut_skolenus()
    skolotaju_db = iegut_skolotaju()
    atzime_db = iegut_atzime()
    return render_template("tabula.html", atzime = atzime_db, skolotaju = skolotaju_db, skoleni = skolenu_db)



if __name__ == '__main__':
    app.run(port = 5000)
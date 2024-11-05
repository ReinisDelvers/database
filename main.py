from flask import Flask, render_template, request
from dati import pievienot_skolenu, pievienot_skolotaju, pievienot_atzime, iegut_skolenus, iegut_skolotaju, iegut_atzime, iegut_prieksmeti, pievienot_prieksmeti, iegut_prieksmeti_id, iegut_skoleni_id, iegut_skolotaji_id, iegut_prieksmetiunskolotaji, pievienot_prieksmetiunskolotaji
import sqlite3

conn = sqlite3.connect("dati.db")

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def skoleni():
    skolenu_db = iegut_skolenus()
    print(skolenu_db)
    if request.method == "POST":
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]
        if vards and uzvards:
          pievienot_skolenu(vards, uzvards)
        dati = vards+" "+uzvards
        return render_template("skoleni.html", aizsutitais = dati, skoleni = skolenu_db)
    return render_template("skoleni.html", aizsutitais = "", skoleni = skolenu_db)

@app.route("/skolotaji", methods=["POST", "GET"])
def skolotaju():
    skolotaju_db = iegut_skolotaju()
    print(skolotaju_db)
    if request.method == "POST":
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]
        if vards and uzvards:
            pievienot_skolotaju(vards, uzvards)
        dati = vards+" "+uzvards
        return render_template("skolotaji.html", aizsutitais = dati, skolotaju = skolotaju_db)
    return render_template("skolotaji.html", aizsutitais = "", skolotaju = skolotaju_db)

@app.route("/atzimes", methods=["POST", "GET"])
def atzime():
    atzime_db = iegut_atzime()
    prieksmeti_id_db = iegut_prieksmeti_id()
    skoleni_id_db = iegut_skoleni_id()

    print(atzime_db)
    if request.method == "POST":
        vards = request.form["vards"]
        subject = request.form["subject"]
        atzime = request.form["atzime"]
        if vards and subject and atzime:
            pievienot_atzime(vards, subject, atzime)
        dati = vards+" "+subject+" "+atzime
        return render_template("atzimes.html", aizsutitais = dati, atzime = atzime_db, skoleni = skoleni_id_db, prieksmeti = prieksmeti_id_db)
    return render_template("atzimes.html", aizsutitais="", atzime=atzime_db, skoleni=skoleni_id_db, prieksmeti=prieksmeti_id_db)

@app.route("/prieksmeti", methods=["POST", "GET"])
def prieksmeti():
    prieksmeti_db = iegut_prieksmeti()
    print(prieksmeti_db)
    if request.method == "POST":
        subject = request.form["subject"]

        if subject:
            pievienot_prieksmeti(subject)
        dati = subject
        return render_template("prieksmeti.html", aizsutitais = dati, prieksmeti = prieksmeti_db)
    return render_template("prieksmeti.html", aizsutitais = "", prieksmeti = prieksmeti_db)

@app.route("/prieksmetiunskolotaji", methods=["POST", "GET"])
def prieksmetiunskolotaji():
    prieksmetiunskolotaji_db = iegut_prieksmetiunskolotaji()
    prieksmeti_id_db = iegut_prieksmeti_id()
    skolotaji_id_db = iegut_skolotaji_id()

    print(prieksmetiunskolotaji_db)
    if request.method == "POST":
        vards = request.form["vards"]
        subject = request.form["subject"]
        if vards and subject:
            pievienot_prieksmetiunskolotaji(vards, subject)
        dati = vards+" "+subject
        return render_template("prieksmetiunskolotaji.html", aizsutitais = dati, prieksmetiunskolotaji = prieksmetiunskolotaji_db, skolotaji = skolotaji_id_db, prieksmeti = prieksmeti_id_db)
    return render_template("prieksmetiunskolotaji.html", aizsutitais="", prieksmetiunskolotaji = prieksmetiunskolotaji_db, skolotaji = skolotaji_id_db, prieksmeti=prieksmeti_id_db)

@app.route("/tabula", methods=["POST", "GET"])
def tabula():
    skolenu_db = iegut_skolenus()
    skolotaju_db = iegut_skolotaju()
    atzime_db = iegut_atzime()
    prieksmeti_db = iegut_prieksmeti()
    prieksmetiunskolotaji_db = iegut_prieksmetiunskolotaji()
    return render_template("tabula.html", atzime = atzime_db, skolotaju = skolotaju_db, skoleni = skolenu_db, prieksmeti = prieksmeti_db, prieksmetiunskolotaji = prieksmetiunskolotaji_db)

if __name__ == '__main__':
    app.run(port = 5000)
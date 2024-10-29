from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def skoleni():
    return render_template("skoleni.html")

@app.route("/skolotaji")
def skolotaji():
    return render_template("skolotaji.html")

@app.route("/atzimes")
def atzimes():
    return render_template("atzimes.html")

@app.route("/tabula")
def tabula():
    return render_template("tabula.html")


if __name__ == '__main__':
    app.run(port = 5000)
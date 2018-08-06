from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/CandyBreaker")
def CandyBreaker():
    return render_template("CandyBreaker.html");

@app.route("/NumberWizard")
def NumberWizard():
    return render_template("NumberWizard.html");

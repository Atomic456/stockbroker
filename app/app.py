from app import app
from flask import render_template


@app.route("/")
def home():
    return "Hello World! I'm using Flask."


@app.route("/createNewPortflolio")
def createPortfolio():
    return render_template("homepage/homepage.html")

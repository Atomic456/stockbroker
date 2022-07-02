from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return "Hello World! I'm using Flask."


@app.route("/createNewPortflolio")
def createPortfolio():
    return render_template('homePage.html')

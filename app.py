from flask import Flask
from flask import render_template
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World! I'm using Flask."


@app.route("/createPortflolio")
def createPortfolio():
    template = jinja_env.get_template('createPortfolio/createPortfolio.html')
    return render_template(template)

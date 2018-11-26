from flask import Flask
from flask import render_template

from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/apps")
def apps():
    return render_template('apps.html')

@app.route("/publications")
def publications():
    return render_template('publications.html')

@app.route("/about")
def about():
    return render_template('about.html')


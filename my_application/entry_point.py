from flask import Flask
from flask import render_template

app_name = Flask(__name__)

@app_name.route("/")
def hello_world():
    return render_template("templates/index.html")

"""
Commande pour mettre a jour python et installer flask
pip --upgrade
pip install flask
"""

from flask import flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hello world from flask"
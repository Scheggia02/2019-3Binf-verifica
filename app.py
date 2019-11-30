from salernitano import catalog
from flask import Flask
import json

app = Flask("Marconi")

@app.route("/")
def data_book():
    return json.dumps([book for book in catalog])


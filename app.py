from flask import Flask, request, jsonify, json
from flask_marshmallow import Marshmallow
from app_core import get_northcountires_names

app = Flask(__name__)
ma = Marshmallow(app)

@app.route('/index')
@app.route('/')
def index():
    ips = request.args.getlist('ip')

    return jsonify({"North Countries": get_northcountires_names(ips)})
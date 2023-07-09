from flask import Flask, jsonify
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")
sys.path.append(parent_dir)

from data.style import style_sheet

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(style_sheet)

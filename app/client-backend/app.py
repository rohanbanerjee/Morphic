from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from flask.json import jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)

datasetHeaders = [
    ['Age', 'Nationality', 'Children']
]
datasetValues = [
    ['45', 'IN', '1'],
    ['22', 'PAK', '0'],
    ['37', 'IN', '1']
]

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/analytics', methods=['GET', 'POST'])
def analytics():
    return render_template('analytics.html')

@app.route('/get/headers/<query>', methods=['GET', 'POST'])
def getHeaders(query):
    return jsonify({'headers': datasetHeaders})

@app.route('/get/values/<query>', methods=['GET', 'POST'])
def getValues(query):
    return jsonify({'values': datasetValues})

if __name__ == "__main__":
    app.run() # host='0.0.0.0'
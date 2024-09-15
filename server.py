from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functions import create
import os.path
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/dbname' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Spreadsheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.Date, nullable=False)

class SpreadsheetData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spreadsheet_id = db.Column(db.Integer, db.ForeignKey('spreadsheet.id'), nullable=False)
    data_date = db.Column(db.Date, nullable=False)
    data_index = db.Column(db.String(100), nullable=False)
    x = db.Column(db.String(100), nullable=False)
    y = db.Column(db.String(100), nullable=False)
    data_value = db.Column(db.Text, nullable=True)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/create_spreadsheet', methods=['POST'])
def create_spreadsheet():
    data = request.json
    id=create(data['name'])
    new_spreadsheet = Spreadsheet(
        name=data['name'],
        owner=data['owner'],
        creation_date=datetime.strptime(data['creation_date'], '%Y-%m-%d')
    )
    response = {
        "message": "Spreadsheet created successfully!",
        "spreadsheet": {
            "name": new_spreadsheet.name,
            "owner": new_spreadsheet.owner,
            "creation_date": new_spreadsheet.creation_date.strftime('%Y-%m-%d')
        }
    }
    
    response_str = json.dumps(response)
    return response_str, 201

@app.route('/create_sheet', methods=['POST'])
def create_sheet():
    data = request.json
    return jsonify(data)

@app.route('/reading', methods=['POST'])
def reading():
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
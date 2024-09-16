from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functions import create,updationg_cells,to_a1_notation
import os.path
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/spread' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Spreadsheet(db.Model):
    spreadsheet_id = db.Column(db.String(100), primary_key=True)
    spreadsheet_name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.Date, nullable=False)

class SpreadsheetData(db.Model):
    spreadsheet_id = db.Column(db.String(100), db.ForeignKey('spreadsheet.spreadsheet_id'), primary_key=True, nullable=False)
    data_date = db.Column(db.Date, nullable=False)
    data_index = db.Column(db.String(100), primary_key=True, nullable=False)
    x = db.Column(db.String(100), primary_key=True, nullable=False)
    y = db.Column(db.String(100), primary_key=True, nullable=False)
    data_value = db.Column(db.Text, nullable=True)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/create_spreadsheet', methods=['POST'])
def create_spreadsheet():
    data = request.json
    id=create(data['spreadsheet_name'])
    new_spreadsheet = Spreadsheet(
        spreadsheet_id=id,
        spreadsheet_name=data['spreadsheet_name'],
        owner=data['owner'],
        creation_date=datetime.strptime(data['creation_date'], '%Y-%m-%d')
    )
    db.session.add(new_spreadsheet)
    db.session.commit()
    inserted_spreadsheet = Spreadsheet.query.filter_by(spreadsheet_id=id).first()
    if inserted_spreadsheet:
        print(f"Inserted Spreadsheet: {inserted_spreadsheet}")
    else:
        print("Spreadsheet not found in the database after insertion.")
    
    response = {
        "message": "Spreadsheet created successfully!",
        "spreadsheet": {
            "spreadsheet_id":id,
            "spreadsheet_name": new_spreadsheet.spreadsheet_name,
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
    id=data['spreadsheet_id']
    inserted_spreadsheet = SpreadsheetData.query.filter_by(spreadsheet_id=id).all()
    if inserted_spreadsheet:
            for row in inserted_spreadsheet:
                print(row.spreadsheet_id,row.data_value,row.x,row.y)
    else:
            print("Spreadsheet no data found.")
    return jsonify(data)

@app.route('/lol', methods=['POST'])
def printing():
    data = request.json
    print(data)
    return jsonify({"message": "Data received"}), 200



@app.route('/delete', methods=['POST'])
def delete():
    data = request.json
    print("deleting")

    id=data['spreadsheet_id']
    x=data['x']
    y=data['y']
    index=data['data_index']
    print(x)
    print(y)
    print(id)
    print(index)
    if(type(x)!=str):
        x=to_a1_notation([x,y])
    cell=SpreadsheetData.query.filter_by(spreadsheet_id=id,x=x,y=y,data_index=index).first()
    if cell:
        db.session.delete(cell) 
        db.session.commit() 
        return jsonify({"message": "Data deleted"}), 200
    else:
       return jsonify({"message": "Data not there in database"}), 200

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    print("adding or updating")
    id=data['spreadsheet_id']
    x=data['x']
    y=data['y']
    index=data['data_index']
    value=data['data_value']
    print(x)
    print(y)
    print(id) 
    print(index)
    print(data)
    if(type(x)!=str):
        x=to_a1_notation([x,y])
    cell=SpreadsheetData.query.filter_by(spreadsheet_id=id,x=x,y=y,data_index=index).first()
    if cell:
        cell.data_value=value
        db.session.commit()
    else:
        final=SpreadsheetData( spreadsheet_id=id,
        data_index=index,
        data_date=datetime.now(), 
        data_value=value,
        x=x,
        y=y        )
        db.session.add(final)
        db.session.commit()
        print("inserting to database")
    updationg_cells(x,y,value,id,index)
    return jsonify({"message": "Data received"}), 200

@app.route('/deletesheet', methods=['POST'])
def deleting_sheet():
    data = request.json
    sheets=SpreadsheetData.query.filter_by(spreadsheet_id=id,x=x,y=y,data_index=index).first()
    if cell:
        db.session.delete(sheets) 
        db.session.commit() 
        return jsonify({"message": "Data deleted"}), 200
    return jsonify({"message": "the spread was not there"}), 200

if __name__ == '__main__':
    app.run(debug=True)
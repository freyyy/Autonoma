
#!flask/bin/python
from flask import Flask, jsonify
import json
import numpy as np
from model import Model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = Model()

@app.route('/employees', methods=['GET'])
def employees():
    current_employees = read_users()
    for current_employee in current_employees:
        add_churn(current_employee)
    return jsonify(current_employees)

@app.route('/employees/<id>', methods=['GET'])
def employee(id):
    current_employees = read_users()
    current_employee = next(emp for emp in current_employees if emp['empId'] == int(id))
    add_churn(current_employee)
    return jsonify(current_employee)

@app.route('/features', methods=['GET'])
def features():
    feature_importances = model.feature_importances()
    features = {}
    features['last_evaluation'] = feature_importances[0] * 100
    features['number_project'] = feature_importances[1] * 100
    features['average_monthly_hours'] = feature_importances[2] * 100
    features['time_spend_company'] = feature_importances[3] * 100
    return jsonify(features)

def read_users():
    with open('current_employees.json') as f:
        current_employees = json.load(f)
        return current_employees

def add_churn(current_employee):
    current_employee['churn'] = model.predict(np.array([[
        current_employee['last_evaluation'],
        current_employee['number_project'],
        current_employee['average_montly_hours'],
        current_employee['time_spend_company'],
        current_employee['Work_accident'],
        current_employee['promotion_last_5years'],
        current_employee['Departments'],
        current_employee['salary'],
    ]])).tolist()[0]
    if current_employee['churn'] == 1:
        current_employee['estimated_years_in_company'] = model.predict_left(np.array([[
            current_employee['last_evaluation'],
            current_employee['number_project'],
            current_employee['average_montly_hours'],
            current_employee['Work_accident'],
            current_employee['promotion_last_5years'],
            current_employee['Departments'],
            current_employee['salary'],
        ]])).tolist()[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

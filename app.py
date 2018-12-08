
#!flask/bin/python
from flask import Flask, jsonify
import json
import numpy as np
from model import Model

app = Flask(__name__)
model = Model()

@app.route('/users', methods=['GET'])
def users():
    current_employees = read_users()
    for current_employee in current_employees:
        add_churn(current_employee)
    return jsonify(current_employees)

@app.route('/users/<id>', methods=['GET'])
def user(id):
    current_employees = read_users()
    current_employee = next(emp for emp in current_employees if emp['empId'] == int(id))
    add_churn(current_employee)
    return jsonify(current_employee)

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

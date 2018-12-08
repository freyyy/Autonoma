
#!flask/bin/python
from flask import Flask, jsonify
import json
import numpy as np
from model import Model

app = Flask(__name__)
model = Model()

with open('current_employees.json') as f:
    current_employees = json.load(f)

@app.route('/', methods=['GET'])
def get_tasks():
    for current_employee in current_employees:
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
    return jsonify(current_employees)

@app.route('/predict', methods=['GET'])
def get_prediction():
    prediction = model.predict(np.array([[0.9, 20, 190, 5, 0, 0, "IT", "high"]]))

    return jsonify(prediction.tolist())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

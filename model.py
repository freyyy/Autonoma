import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

class Model:

    def __init__(self):
        data = pd.read_csv('employee_data.csv')
        data_left = pd.read_csv('employee_data.csv')
        print(data.head())

        self.department_label_encoder = preprocessing.LabelEncoder()
        self.salary_label_encoder = preprocessing.LabelEncoder()

        data['department'] = self.department_label_encoder.fit_transform(data['department'])
        data['salary'] = self.salary_label_encoder.fit_transform(data['salary'])

        X = data[['last_evaluation', 'number_project',
               'average_montly_hours', 'time_spend_company', 'work_accident',
               'promotion_last_5years', 'department', 'salary']]
        y = data['left']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        self.rf = RandomForestClassifier()
        self.rf.fit(X_train, y_train)

        rf_y_pred = self.rf.predict(X_test)

        print("Accuracy:", metrics.accuracy_score(y_test, rf_y_pred))
        print("Precision:", metrics.precision_score(y_test, rf_y_pred))
        print("Recall:", metrics.recall_score(y_test, rf_y_pred))
        print(self.rf.feature_importances_)

        data_left = data.loc[data['left'] == 1]

        X_left = data_left[['last_evaluation', 'number_project',
               'average_montly_hours', 'work_accident',
               'promotion_last_5years', 'department', 'salary']]
        y_left = data_left['time_spend_company']

        X_left_train, X_left_test, y_left_train, y_left_test = train_test_split(X_left, y_left, test_size=0.3, random_state=42)
        self.rf_left = RandomForestClassifier()
        self.rf_left.fit(X_left_train, y_left_train)

        rf_y_left_pred = self.rf_left.predict(X_left_test)

        print("Accuracy:", metrics.accuracy_score(y_left_test, rf_y_left_pred))
        print("Precision:", metrics.precision_score(y_left_test, rf_y_left_pred, average='micro'))
        print("Recall:", metrics.recall_score(y_left_test, rf_y_left_pred, average='micro'))
        print(self.rf_left.feature_importances_)


    def predict(self, employee_data):
        print(employee_data)
        employee_data[:, 6] = self.department_label_encoder.transform(employee_data[:, 6])
        employee_data[:, 7] = self.salary_label_encoder.transform(employee_data[:, 7])
        print(employee_data)
        return self.rf.predict(employee_data)

    def predict_left(self, employee_data):
        print(employee_data)
        employee_data[:, 5] = self.department_label_encoder.transform(employee_data[:, 5])
        employee_data[:, 6] = self.salary_label_encoder.transform(employee_data[:, 6])
        print(employee_data)
        return self.rf_left.predict(employee_data)

if __name__ == '__main__':
    model = Model()
    prediction = model.predict(np.array([[0.9, 20, 190, 5, 0, 0, "IT", "high"]]))
    prediction_left = model.predict_left(np.array([[0.7, 3, 220, 0, 0, "IT", "medium"]]))
    print("Predicted: ", prediction)
    print("Predicted left: ", prediction_left)

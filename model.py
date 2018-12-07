import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

class Model:

    def __init__(self):
        data = pd.read_csv('employee_data.csv')
        print(data.head())


        self.department_label_encoder = preprocessing.LabelEncoder()
        self.salary_label_encoder = preprocessing.LabelEncoder()

        data['department'] = self.department_label_encoder.fit_transform(data['department'])
        data['salary'] = self.salary_label_encoder.fit_transform(data['salary'])

        X = data[['satisfaction_level', 'last_evaluation', 'number_project',
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

    def predict(self, employee_data):
        print(employee_data)
        employee_data[:, 7] = self.department_label_encoder.transform(employee_data[:, 7])
        employee_data[:, 8] = self.salary_label_encoder.transform(employee_data[:, 8])
        print(employee_data)
        return self.rf.predict(employee_data)

if __name__ == '__main__':
    model = Model()
    prediction = model.predict(np.array([[0.50, 0.7, 2, 157, 3, 0, 0, "sales", "low"]]))
    print("Predicted: ", prediction)

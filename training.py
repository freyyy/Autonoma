import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from joblib import dump, load
import numpy

# load data
data = pd.read_csv('employee_data.csv')

# create label encoder
le = preprocessing.LabelEncoder()

# convert string labels into numbers.
data['salary']=le.fit_transform(data['salary'])
data['department']=le.fit_transform(data['department'])

print(data.head())

# split dataset into input columns and output column
X=data[['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'work_accident',
       'promotion_last_5years', 'department', 'salary']]
y=data['left']

# split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# create gradient boosting classifier
gb = GradientBoostingClassifier()

# train model using the training set
gb.fit(X_train, y_train)

# save model
dump(gb, 'gb.joblib')

# load model
gb = load('gb.joblib')

# preditct the response using the test set
y_pred = gb.predict(X_test)

# evaluate model performance
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))

y_pred_proba = gb.predict_proba(X_test)

print(y_pred_proba)

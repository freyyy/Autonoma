import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from joblib import dump, load

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
rf = RandomForestClassifier()

# train model using the training set
gb.fit(X_train, y_train)
rf.fit(X_train, y_train)

# save model
dump(gb, 'gb.joblib')
dump(rf, 'rf.joblib')

# load model
gb = load('gb.joblib')
rf = load('rf.joblib')

# preditct the response using the test set
gb_y_pred = gb.predict(X_test)
rf_y_pred = rf.predict(X_test)

# evaluate gradient boosting classifier performance
print("Gradient Boosting Classifier")
print("Accuracy:", metrics.accuracy_score(y_test, gb_y_pred))
print("Precision:", metrics.precision_score(y_test, gb_y_pred))
print("Recall:", metrics.recall_score(y_test, gb_y_pred))
print(gb.feature_importances_)
gb_y_pred_proba = gb.predict_proba(X_test)
print(gb_y_pred_proba)

# evaluate gradient boosting classifier performance
print("Random Forest Classifier")
print("Accuracy:", metrics.accuracy_score(y_test, rf_y_pred))
print("Precision:", metrics.precision_score(y_test, rf_y_pred))
print("Recall:", metrics.recall_score(y_test, rf_y_pred))
print(rf.feature_importances_)

rf_y_pred_proba = rf.predict_proba(X_test)
print(rf_y_pred_proba)

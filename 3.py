# Customer churn: Logistic Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
data = pd.read_csv('Churn_Modelling.csv')
data = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)
data = pd.get_dummies(data, columns=['Geography', 'Gender'], drop_first=True)
X = data.drop('Exited', axis=1)
y = data['Exited']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print('\nBasic Model Accuracy:', accuracy_score(y_test, y_pred))
print('Basic Model Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
improved_model = LogisticRegression(random_state=42, class_weight='balanced')
improved_model.fit(X_train, y_train)
y_pred_improved = improved_model.predict(X_test)
print('\nBalanced Model Accuracy:', accuracy_score(y_test, y_pred_improved))
print('Balanced Model Confusion Matrix:\n', confusion_matrix(y_test, y_pred_improved))

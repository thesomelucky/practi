# Uber fare: Linear Regression and Random Forest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    a = np.sin((lat2 - lat1) / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2
    return 6371 * 2 * np.arcsin(np.sqrt(np.clip(a, 0, 1)))

def remove_outliers_iqr(data, column):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    return data[data[column].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)]
df = pd.read_csv('uber.csv')
df.drop(columns=['Unnamed: 0'], errors='ignore', inplace=True)
df.dropna(inplace=True)
df = df[(df['fare_amount'] > 0) & (df['passenger_count'] > 0)].copy()
df = df[df['pickup_latitude'].between(-90, 90) & df['dropoff_latitude'].between(-90, 90) & df['pickup_longitude'].between(-180, 180) & df['dropoff_longitude'].between(-180, 180)].copy()
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce', utc=True)
df.dropna(subset=['pickup_datetime'], inplace=True)
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
df['distance_km'] = haversine_distance(df['pickup_latitude'], df['pickup_longitude'], df['dropoff_latitude'], df['dropoff_longitude'])
for column in ['fare_amount', 'passenger_count', 'distance_km']:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title('Outliers in ' + column)
    plt.tight_layout()
    plt.show()
df = remove_outliers_iqr(df, 'fare_amount')
df = remove_outliers_iqr(df, 'distance_km')
features = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'hour', 'day', 'month', 'year', 'day_of_week', 'distance_km']
correlation_matrix = df[['fare_amount'] + features].corr()
print('Correlation Matrix:\n', correlation_matrix)
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.tight_layout()
plt.show()
X_train, X_test, y_train, y_test = train_test_split(df[features], df['fare_amount'], test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
linear_model = LinearRegression()
linear_model.fit(X_train_scaled, y_train)
linear_predictions = linear_model.predict(X_test_scaled)
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
random_forest_model.fit(X_train, y_train)
rf_predictions = random_forest_model.predict(X_test)
rows = []
for name, predictions in [('Linear Regression', linear_predictions), ('Random Forest Regression', rf_predictions)]:
    mse = mean_squared_error(y_test, predictions)
    rows.append({'Model': name, 'R2 Score': r2_score(y_test, predictions), 'MSE': mse, 'RMSE': np.sqrt(mse), 'MAE': mean_absolute_error(y_test, predictions)})
print('\nMODEL COMPARISON\n', pd.DataFrame(rows).to_string(index=False))

# Sales: K-Means

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
data = pd.read_csv('sales_data_sample.csv', encoding='latin1')
X = data[['QUANTITYORDERED', 'PRICEEACH', 'SALES']].dropna()
if len(X) < 10:
    raise ValueError('At least 10 complete rows are needed for the elbow method (k=1 to 10).')
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
plt.figure()
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.tight_layout()
plt.show()
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)
result = X.copy()
result['Cluster'] = clusters
plt.figure()
plt.scatter(result['QUANTITYORDERED'], result['SALES'], c=result['Cluster'], cmap='viridis')
plt.xlabel('Quantity Ordered')
plt.ylabel('Sales')
plt.title('K-Means Clustering')
plt.tight_layout()
plt.show()

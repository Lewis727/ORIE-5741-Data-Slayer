import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
import os

# Prepare the data
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '/Data/'
data = pd.read_excel(dir + 'Region_NW.xlsx', index_col=0)
data.index = pd.to_datetime(data.index)
y = data['D'].iloc[1:]
X = data[['D', 'NG']].iloc[:-1]

# Train the model
clf = OneClassSVM(gamma='auto', nu=0.05)
clf.fit(X)

# Test the model
y_pred = clf.predict(X)

plt.figure(figsize=(15, 7))
fig, ax = plt.subplots()
ax.scatter(data.index, data['D'], label='Time Series Data')
anomalies = data[y_pred == -1]
ax.scatter(anomalies.index, anomalies['D'], color='red', label='Anomalies')

plt.legend()
plt.show()
plt.savefig('alltime_ocsvm.jpg')
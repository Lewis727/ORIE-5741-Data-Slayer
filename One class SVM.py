import pandas as pd
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
import os

# Prepare the data
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '/Data/'
data = pd.read_csv(dir + 'data.csv', index_col=0)
data.index = pd.to_datetime(data.index)

# Train the model
clf = OneClassSVM(kernel='sigmoid', gamma='auto', nu=0.0005)
clf.fit(data)

# Test the model
y_pred = clf.predict(data)

plt.figure(figsize=(15, 7))
fig, ax = plt.subplots()
ax.plot(data.index, data['D'], alpha=0.6, label='Time Series Data')
anomalies = data[y_pred == -1]
ax.scatter(anomalies.index, anomalies['D'], color='red', label='Anomalies')
plt.legend()
plt.savefig('ocs.jpg')
print(len(anomalies)/len(data))
res = pd.DataFrame(y_pred)
res.index = data.index
res.to_csv('one class svm.csv')
import matplotlib.pyplot as plt
import pandas as pd
import os

# Prepare the data
labels = pd.read_csv('labels.csv')
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '/Data/'
data = pd.read_csv(dir + 'data.csv', index_col=0)
data.index = pd.to_datetime(data.index)
labels.index = data.index
plt.figure(figsize=(15, 7))
fig, ax = plt.subplots()
plt.plot(data.index, data['D'], alpha=0.6, label='Time Series Data')
anomalies = data[labels['mode'] == -1]
ax.scatter(anomalies.index, anomalies['D'], color='red', label='Anomalies')
plt.legend()
plt.title('Final anomalies')
plt.savefig('final.jpg')

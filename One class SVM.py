import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM
import os

# Prepare the data
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '\Data\\'
data = pd.read_csv(dir + 'data.csv', index_col=0)
data.index = pd.to_datetime(data.index)
y = data['D']
X = data.columns.drop('D')
print(X)
X = data[X]

# Train the model
clf = OneClassSVM(gamma='auto', nu=0.05)
clf.fit(X)

# Test the model
y_pred = clf.predict(X)
print(y_pred) # Outputs the predicted labels for each data point


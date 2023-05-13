import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '/Data/'
data = pd.read_csv(dir + 'data.csv')
labels = pd.read_csv('labels.csv', index_col=0)
am = data[data['delta_D_0'] == 1].index
al = ['random_forest', 'kmeans', 'mode']
titles = ['random forest', 'kmeans', 'final label']
fig, axs = plt.subplots(1, 3, sharey=True, figsize=(12,4))

for i, m in enumerate(al):
    ax = axs[i]
    t = np.sum(labels[m].iloc[am] == -1)
    if t == 0:
        n = np.random.randint(1, 10)
        p = sorted(np.random.choice(am, n, replace=False))
    else:
        p = am
    P = labels[labels[m] == -1].index
    X = data['UTC time'].iloc[P]
    y = data['D'].iloc[P]
    ax.scatter(X, y, c='b', label='Normal anomaly')
    X = data['UTC time'].iloc[p]
    y = data['D'].iloc[p]
    ax.scatter(X, y, c='r', label='Apparent anomaly')
    ax.set_title(titles[i])
    ax.set_xticks([])


fig.text(0.5, 0.04, 'Time', ha='center', va='center')
fig.text(0.06, 0.5, 'Demand', ha='center', va='center', rotation='vertical')
plt.savefig('two same.jpg')



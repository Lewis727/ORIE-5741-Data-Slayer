import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '/Data/'
data = pd.read_csv(dir + 'data.csv')
labels = pd.read_csv('labels.csv', index_col=0)
print(labels.eq(-1).sum())
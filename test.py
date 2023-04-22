import pandas as pd
import os

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '\Data\\'
data = pd.read_excel(dir+'region_NW.xlsx')
print(data.shape)
data = pd.read_csv(dir + 'data.csv', index_col=0)
print(data.shape)

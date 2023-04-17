import pandas as pd

data = pd.read_excel('Region_NW.xlsx', index_col=1)
data.index = pd.to_datetime(data.index)
data = data.dropna(axis='columns', how='all')
data = data.dropna(axis=0, subset=['D'])
data = data.drop(columns=['Local time', 'Local date', 'Hour', 'Time zone', 'DF', 'Region'])

import pandas as pd
import os

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '\Data\\'
data = pd.read_excel(dir + 'Region_NW.xlsx', index_col=1)
data.index = pd.to_datetime(data.index)
data = data.drop(columns=['Local time', 'Local date', 'Hour', 'Time zone', 'DF', 'Region'])

regions = ['AVA', 'AVRN', 'BPAT', 'CHPD', 'DOPD', 'GCPD', 'GRID', 'GWA', 'IPCO', 'NEVP', 'NWMT', 'PACE', 'PACW', 'PGE', 'PSCO', 'PSEI', 'SCL', 'TPWR', 'WACM', 'WAUW', 'WWA']
for r in regions:
    region = pd.read_excel(dir + r + '.xlsx', index_col=1)
    region.index = pd.to_datetime(region.index)
    temp = region['D']
    data = data.join(temp, rsuffix='_'+r)
data = data.dropna(axis='columns', how='all')
data = data.dropna()
data.to_csv(dir+'data.csv')
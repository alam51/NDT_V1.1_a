import pandas as pd

df = pd.DataFrame()

dt = pd.to_datetime('2021-1-5')
df.loc[dt, '2'] = 5
a = 5
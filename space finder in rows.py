import pandas as pd

df = pd.read_csv(r'C:\Users\USER\Downloads\gmd.csv')
a = 5

for i, name in enumerate(df.name):
    df.loc[i, 'name'] = name.replace(' ', '*')

df.to_csv('gmd_space.csv')




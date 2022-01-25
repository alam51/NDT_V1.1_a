import pandas as pd
import numpy as np

file_path = r'G:\Other computers\My Computer\Data [F]\Gen\Irrigation\2021\peaks\total.csv'
df = pd.read_csv(file_path, parse_dates=[0],
                 infer_datetime_format=True, index_col=[0, 1], dayfirst=True)
a = 4
# print(df)
# df_dhaka = df
# df1
# for i in df_dhaka.index:
#     if i[1] not in [1,2,3,4]:
#         l = [pd.NA for j in df_dhaka.columns]
#         df_dhaka.loc[i, :] = l
#
# df_dhaka.dropna(inplace=True)
df_dhaka = pd.DataFrame()

for i in df.index:
    if i[1] in [1, 2, 3, 4]:
        val = df.loc[i, 'value']
        # df_dhaka.loc[i[0], 'value'] += val
        try:
            df_dhaka.loc[i[0], 'value'] += val
        except KeyError:
            df_dhaka.loc[i[0], 'value'] = val
        # df_dhaka.loc[i, 'value'] += df.loc[i, 'value']

c = 5

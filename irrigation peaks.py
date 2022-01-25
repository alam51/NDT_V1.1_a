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

"""unifying zones 1-4 to a single zone Dhaka by summing up"""
for i in df.index:
    if i[1] in [1, 2, 3, 4]:  # i -> (date_time, id)
        val = df.loc[i, 'value']
        # df_dhaka.loc[i[0], 'value'] += val
        try:
            df_dhaka.loc[i[0], 'value'] += val
        except KeyError:  # আগে থেকে না থাকলে এই ব্লকে ঢুকবে
            df_dhaka.loc[i[0], 'value'] = val

        df_dhaka.loc[i[0], 'name'] = 'Dhaka'
        # df_dhaka.loc[i, 'value'] += df.loc[i, 'value']

zone_df_list = [pd.DataFrame()]  # Assigning a blank zone (zone=0 for Dhaka)
# for i in [0] + df.loc[:, 'id'].unique():  # 0th zone is Dhaka (sum of zones 1-4)
# for i in range(0, 12+1):  # 0th zone is Dhaka (sum of zones 1-4)
#     zone_df_list.append(pd.DataFrame())
"""Assigning zones (1-12) to df_list"""
for i in range(1, 12 + 1):
    df2 = df.xs(i, level=1)  # index[1]
    # df3 = df2.resample('1W').max()
    zone_df_list.append(df2)
    # pass

zone_df_list[0] = df_dhaka

resampled_zone_df_list = []
for zone_df in zone_df_list:
    df3 = zone_df.resample('1W').max()
    resampled_zone_df_list.append(df3)

reshaped_zone_df_list = []
for df in resampled_zone_df_list:
    new_df = pd.DataFrame()
    for i in df.index:
        if i.month in [2, 3, 4]:
            new_df.loc[i.day, i.month] = df.loc[i, 'value']
c = 5

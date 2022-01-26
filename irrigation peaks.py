import pandas as pd
import numpy as np

file_path = r'G:\Other computers\My Computer\Data [F]\Gen\Irrigation\2021\peaks\total.csv'
df = pd.read_csv(file_path, parse_dates=[0],
                 infer_datetime_format=True, index_col=[0, 1], dayfirst=True)
year = df.index[0][0].year
a = 4

total_df = pd.DataFrame()
for i in df.index:
    if i[0] not in total_df.index:
        total_df.loc[i[0], 'name'] = 'system total'
        new_df = df.xs(i[0])
        total_df.loc[i[0], 'value'] = new_df.loc[:, 'value'].sum()

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
zone_df_list.append(total_df)

resampled_zone_df_list = []
for zone_df in zone_df_list:
    df3 = zone_df.resample('1W').max()
    start_str = str(year) + '-2'
    end_str = str(year) + '-4'
    resampled_zone_df_list.append(df3.loc[start_str:end_str])

reshaped_zone_df_list = []

with pd.ExcelWriter("op.xlsx") as writer:
    for df in resampled_zone_df_list:
        new_df = pd.DataFrame()
        month_count_dict = {2: 1, 3: 1, 4: 1, 5: 1}
        for i in df.index:
            if i.month in [2, 3, 4]:
                new_df.loc[month_count_dict[i.month], i.strftime("%B-%y")] = df.loc[i, 'value']
                month_count_dict[i.month] += 1
        # reshaped_zone_df_list.append(new_df)
        new_df.index.name = 'Week'
        sheet_name = df.loc[:, 'name'][0]
        new_df.to_excel(writer, sheet_name=sheet_name)

c = 5

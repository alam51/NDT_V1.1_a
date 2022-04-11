import datetime
import traceback

import numpy as np
import pandas as pd

file_path = r'G:\My Drive\presentation\ss load feeders.xlsx'
df = pd.read_excel(file_path, index_col=[0])
# df = pd.read_csv(file_path, index_col=[0], dayfirst=True)
a = 4
value_col = 'MW'  # may be MW, kV etc
ss_col = 'ss'
zone_col = 'zone'


def daily_peak(df: pd.DataFrame) -> pd.DataFrame:
    _index = pd.date_range(start=df.index[0], end=df.index[-1], freq='1D')
    _cols = ['peak', 'peak_time']
    peak_df = pd.DataFrame(index=_index, columns=_cols)

    for day in _index:
        try:
            day_str = str(day)[:10]
            # current_day_df = df.loc[day_str]  # takes whole day
            current_day_df = df.loc[day_str].between_time('18:00', '22:00')  # takes peak hour only
            current_day_system_load_df = current_day_df.groupby(current_day_df.index).sum()
            system_max = current_day_system_load_df[value_col].max()
            system_max_df = current_day_system_load_df[current_day_system_load_df[value_col] == system_max]

            peak_df.loc[day, 'peak'] = system_max_df[value_col][0]
            peak_df.loc[day, 'peak_time'] = system_max_df.index[0]
        except:
            print(traceback.format_exc())
            # print(f'error on ')

    return peak_df


def ss_load_at_system_peak(df: pd.DataFrame) -> pd.DataFrame:
    # for i in df.index:
    #     if df.loc[i, value_col] < 0:
    #         df.loc[i, value_col] *= -1

    _daily_system_peak_df = daily_peak(df)
    # _index = pd.date_range(start=df.index[0], end=df.index[-1], freq='1D')
    _index = _daily_system_peak_df['peak_time'].tolist()
    _index = pd.Index(_index)
    _cols = df[ss_col].unique()
    ss_load_at_system_peak_df = pd.DataFrame(index=_index, columns=_cols)
    for i in ss_load_at_system_peak_df.index:
        # peak_time = _daily_system_peak_df.loc[i, 'peak_time']
        for j in ss_load_at_system_peak_df.columns:
            # daily_ss_peak_df = df.loc[peak_time, :]
            try:
                df3 = df.loc[i, :]
                val_df = df3[df3[ss_col] == j]  # Multiple entry of single value
                val = val_df[value_col].max()  # Take max value
                ss_load_at_system_peak_df.loc[i, j] = val
            except:
                print(f'df3')
                print(f'{df.loc[i, :]}')
                print(traceback.format_exc())

    ss_load_at_system_peak_df = ss_load_at_system_peak_df.T
    a = 5
    for col in ss_load_at_system_peak_df.columns:
        sum_val = ss_load_at_system_peak_df[col].sum()
        ss_load_at_system_peak_df.loc['sum', col] = sum_val

    return ss_load_at_system_peak_df  # SE sir format


def ss_load_at_system_peak_ratio(df: pd.DataFrame) -> pd.DataFrame:
    ss_load_at_system_peak_ratio_df = pd.DataFrame()
    for col in df.columns:
        denominator = df.loc['sum', col]
        for i in df.index:  # except last row ('sum)
            if denominator:
                ss_load_at_system_peak_ratio_df.loc[i, col] = df.loc[i, col] / denominator
            else:
                print(f'Failed due to 0 in denominator. The top five row of df:')
                print(ss_load_at_system_peak_ratio_df.head(5))

    return ss_load_at_system_peak_ratio_df


# daily_system_peak_df = daily_peak(df)
# ss_load_at_system_peak_df = ss_load_at_system_peak(df)
# ss_load_at_system_peak_ratio_df = ss_load_at_system_peak_ratio(ss_load_at_system_peak_df)
# a = 4

with pd.ExcelWriter('ss_load_value.xlsx') as writer:
    zones = df[zone_col].unique()

    for zone in zones:
        zone_df = df[df[zone_col] == zone]
        zonewise_ss_load_at_zone_peak_df = ss_load_at_system_peak(zone_df)
        # zonewise_ss_load_at_system_peak_ratio_df = ss_load_at_system_peak_ratio(zonewise_ss_load_at_system_peak_df)
        zonewise_ss_load_at_zone_peak_df.to_excel(writer, sheet_name=f'zone {zone}')

with pd.ExcelWriter('ss_load_rationing.xlsx') as writer:
    zones = df[zone_col].unique()

    for zone in zones:
        zone_df = df[df[zone_col] == zone]
        zonewise_ss_load_at_zone_peak_df = ss_load_at_system_peak(zone_df)
        zonewise_ss_load_at_zone_peak_ratio_df = ss_load_at_system_peak_ratio(zonewise_ss_load_at_system_peak_df)
        zonewise_ss_load_at_zone_peak_ratio_df.to_excel(writer, sheet_name=f'zone {zone}')

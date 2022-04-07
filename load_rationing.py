import datetime

import pandas as pd

file_path = r'G:\My Drive\presentation\Load Rationing1.xlsx'
df = pd.read_excel(file_path, index_col=[0])
a = 4
value_col = 'value'  # may be MW, kV etc
ss_col = 'SS'

def daily_peak(df: pd.DataFrame) -> pd.DataFrame:
    _index = pd.date_range(start=df.index[0], end=df.index[-1], freq='1D')
    _cols = ['peak', 'peak_time']
    peak_df = pd.DataFrame(index=_index, columns=_cols)

    for day in _index:
        day_str = str(day)[:10]
        current_day_df = df.loc[day_str]
        current_day_system_load_df = current_day_df.groupby(current_day_df.index).sum()
        system_max = current_day_system_load_df[value_col].max()
        system_max_df = current_day_system_load_df[current_day_system_load_df[value_col] == system_max]

        peak_df.loc[day, 'peak'] = system_max_df[value_col][0]
        peak_df.loc[day, 'peak_time'] = system_max_df.index[0]

    return peak_df


def ss_load_at_system_peak(df: pd.DataFrame) -> pd.DataFrame:
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
            df3 = df.loc[i, :]
            val_df = df3[df3[ss_col] == j]  # Multiple entry of single value
            val = val_df[value_col].max()  # Take max value
            ss_load_at_system_peak_df.loc[i, j] = val

    return ss_load_at_system_peak_df


daily_system_peak_df = daily_peak(df)
df2 = ss_load_at_system_peak(df)
a = 4
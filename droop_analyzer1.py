import re

import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
from mpl_toolkits import mplot3d
from data_processor import DfProcessor

# file_path = 'F:/Bhola_Notun_Biddyut/2021.11.09.csv'
# file_path = 'G:/Other computers/My Computer/FGMO/Summit_Bibiyana/Summit Bib 2021.11.16.csv'
file_path = r'G:\Other computers\My Computer\Data [F]\FGMO\2022.02.27.csv'
df_obj = DfProcessor(file_path, source='s')
df = df_obj.df
del df_obj
a = 5


def hourly_rank(df: pd.DataFrame, time_start=None, time_end=None, freq='1H'):
    """
    df with 2 cols
    1. FREQ
    2. MW

    """
    df1 = df.loc[time_start:time_end]
    time_start = df.index[0]
    time_end = df.index[-1]
    time_range = pd.date_range(start=time_start, end=time_end, freq=freq)
    rank_df = pd.DataFrame(index=time_range[:-2], columns=df1.columns[1:])
    for i, time in enumerate(time_range[:-2]):
        t1 = str(time_range[i])
        t2 = str(time_range[i + 1])
        df2 = df1.loc[t1:t2]
        corr_df = df2.corr()
        df_to_concat = corr_df.iloc[0, 1:]
        freq_index = None
        for row in corr_df.index:
            if 'FREQ.HZ' in row.upper():
                freq_index = row
                break
        if freq_index is None:
            print('No frequency column found in code line 41')

        for col in corr_df.columns:
            if 'FREQ.HZ' not in col.upper():
                rank_df.loc[time, col] = corr_df.loc[freq_index, col]

    rank_df1 = rank_df.apply(pd.to_numeric)
    new_col_names = []
    for j, col in enumerate(rank_df1.columns):
        c = re.search(r'.STTN', col)
        d = re.search('CALC_', col)
        new_col_name1 = col[:c.span()[0]] if c else ''
        new_col_name2 = col[d.span()[1] + 0] if d else ''  # last span is already original pos + 1
        new_col_names.append(new_col_name1 + new_col_name2)
        # rank_df1.columns[j] = new_col_name1 + new_col_name2
    rank_df1.columns = new_col_names
    return rank_df1


rank_df = hourly_rank(df)
rank_df.to_html('op.html')
rank_df.to_excel('op.xlsx')
a = 3
# class DroopAnalyzer:
#     pass
#
#
#
# a = DroopAnalyzer(df)
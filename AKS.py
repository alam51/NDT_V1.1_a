import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
from mpl_toolkits import mplot3d
from data_processor import DfProcessor
import openpyxl as xl

# file_path = 'F:/Bhola_Notun_Biddyut/2021.11.09.csv'
file_path = r'G:\Other computers\My Computer\Data [F]\FGMO\AKS\Dec 2021.csv'
df = DfProcessor(file_path)
df1 = df.df.loc['2021-12-20']
# df.df.plot(secondary_y=[df.df.columns[1]])
# df.df.loc[:, 'time'] = df.df.index.to_list()
a = df1.corr()
a.to_excel('AKS.xlsx')

f_time = df.df.index[0]
l_time = df.df.index[-1]

corr_value_df = pd.DataFrame()
time = f_time
while time < l_time-pd.Timedelta(hours=1):
    time_range_start = str(time)
    time_range_end = str(time+pd.Timedelta(hours=1))
    corr_df = df.df.loc[time_range_start:time_range_end].corr()
    corr_value_df.loc[time, 0] = corr_df.iloc[0,3]
    time += pd.Timedelta(hours=1)

corr_value_df1 = corr_value_df.dropna(axis=0)
corr_value_df_max = corr_value_df1[corr_value_df1[0] == corr_value_df1[0].max()]
corr_value_df_min = corr_value_df1[corr_value_df1[0] == corr_value_df1[0].min()]
v = 4
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
from mpl_toolkits import mplot3d
from data_processor import DfProcessor

# file_path = 'F:/Bhola_Notun_Biddyut/2021.11.09.csv'
# file_path = r'G:\Other computers\My Computer\Data [F]\FGMO\AKS\Dec 2021.csv'
file_path = r'Dec 2021.csv'
# file_path = r'Dec 2021.xlsx'
df = DfProcessor(file_path)
df1 = df.df.iloc[:, [0, 3]]
df1 = df1.loc['2021-12-20':, :]
df1.plot(secondary_y=[df1.columns[1]])
# df.df.loc[:, 'time'] = df.df.index.to_list()
# a = df.df.corr()
# a.to_excel()

f_time = df1.index[0]
l_time = df1.index[-1]

corr_value_df = pd.DataFrame()
time = f_time
while time < l_time - pd.Timedelta(hours=1):
    time_range_start = str(time)
    time_range_end = str(time + pd.Timedelta(hours=1))
    corr_df = df1.loc[time_range_start:time_range_end].corr()
    corr_value_df.loc[time, 0] = corr_df.iloc[0, 1]
    time += pd.Timedelta(hours=1)

corr_value_df1 = corr_value_df.dropna(axis=0)
corr_value_df_max = corr_value_df1[corr_value_df1[0] == corr_value_df1[0].max()]
corr_value_df_min = corr_value_df1[corr_value_df1[0] == corr_value_df1[0].min()]
v = 4
with pd.ExcelWriter('AKS.xlsx') as writer:
    corr_value_df1.columns = ['Hourly Corr Value']
    corr_value_df1.to_excel(writer, sheet_name='overall')
    corr_value_df_max.to_excel(writer, sheet_name='max')
    corr_value_df_min.to_excel(writer, sheet_name='min')

plt.grid(True)
plt.show()

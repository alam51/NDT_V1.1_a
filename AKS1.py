import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
# from scipy import stats
# from mpl_toolkits import mplot3d
from data_processor import DfProcessor

# file_path = 'F:/Bhola_Notun_Biddyut/2021.11.09.csv'
# file_path = r'G:\Other computers\My Computer\Data [F]\FGMO\AKS\Dec 2021.csv'
file_path = r'Dec 2021.csv'
# file_path = r'Dec 2021.xlsx'
df = DfProcessor(file_path)
df1 = df.df.iloc[:, [0, 3]]
df1 = df1.loc['2021-12-20':, :]

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

corr_value_df1 = corr_value_df.dropna(axis=0, how='any')
corr_value_df_max = corr_value_df1[corr_value_df1[0] == corr_value_df1[0].max()]
corr_value_df_min = corr_value_df1[corr_value_df1[0] == corr_value_df1[0].min()]
v = 4
with pd.ExcelWriter('AKS.xlsx') as writer:
    corr_value_df1.columns = ['Hourly Corr Value']
    corr_value_df1.to_excel(writer, sheet_name='overall')
    corr_value_df_max.to_excel(writer, sheet_name='max')
    corr_value_df_min.to_excel(writer, sheet_name='min')

# df1.plot(secondary_y=[df1.columns[0]])
# df1.plot(xlabel='Time', ylabel='MW/kV', ylim=[220, 255], secondary_y=[df1.columns[0]])
# # plt.xlabel('Time', fontsize=15)
# # plt.ylabel('MW / kV', fontsize=15)
# # plt.grid(axis='both', which='major')
# plt.grid(True)
# # plt.subplots_adjust(bottom=.25, left=.25)
# # plt.legend(fontsize=16)
# plt.show()
fig, ax1 = plt.subplots()

color = 'tab:green'
ax1.set_xlabel('Time', fontsize=15)
ax1.set_ylabel('BSRM 230kV Bus Voltage [kV]', color=color, fontsize=15)
ax1.plot(df1.index, df1.iloc[:, 1], color=color)
ax1.tick_params(axis='y', labelcolor=color)
# ax1.set_ylim(225, 2)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y %H-%M'))

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'darkred'
ax2.set_ylabel('AKS Total Load [MW]', color=color, fontsize=15)  # we already handled the x-label with ax1
ax2.plot(df1.index, df1.iloc[:, 0], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.grid(True)
plt.show()

from matplotlib import pyplot as plt
from scipy import stats

from data_processor import DfProcessor

# file_path = 'F:/Bhola_Notun_Biddyut/2021.11.09.csv'
file_path = 'F:/Summit Bib 2021.11.16.csv'
df = DfProcessor(file_path)
# df.df.plot(secondary_y=[df.df.columns[1]])
x_data = df.df.loc[:].iloc[:, 1].to_list()
# x_data = df.df.loc['2021-11-09 01:00':'2021-11-09 19:00'].iloc[:, 1].to_list()
y_data = df.df.loc[:].iloc[:, 0].to_list()
# y_data = df.df.loc['2021-11-09 01:00':'2021-11-09 19:00'].iloc[:, 0].to_list()
# df.df.plot.scatter(x=df.df.columns[1], y=df.df.columns[0])
slope, intercept, r, p, std_err = stats.linregress(x_data, y_data)
droop = (intercept-50.0)/50.0


def myfunc(x):
    return slope * x + intercept


# df.df.loc['2021-11-08 18'].plot.scatter(x=df.df.columns[1], y=df.df.columns[0])
mymodel = list(map(myfunc, x_data))
plt.scatter(x_data, y_data)
plt.xlabel('Active Power [MW]', fontsize=15)
plt.ylabel('Frequency [Hz]', fontsize=15)
plt.plot(x_data, mymodel, color='r', label=f'slope={slope:.4f}Hz/MW\n'
                                           f'gain={1/slope:.2f}MW/Hz\n'
                                           f'intercept={intercept:.2f}Hz\n'
                                           f'droop={droop*100:.2f}%\n'
                                           f'error={std_err*100:.4f}%'
         )
plt.grid(True)
plt.legend(fontsize=16)
plt.show()
b = 4

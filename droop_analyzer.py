from matplotlib import pyplot as plt
from scipy import stats

from data_processor import DfProcessor

file_path = 'F:/Bhola_Notun_Biddyut/2021.11.09.csv'
df = DfProcessor(file_path)
# df.df.plot(secondary_y=[df.df.columns[1]])
x_data = df.df.iloc[:, 1].to_list()
y_data = df.df.iloc[:, 0].to_list()
# df.df.plot.scatter(x=df.df.columns[1], y=df.df.columns[0])
slope, intercept, r, p, std_err = stats.linregress(x_data, y_data)


def myfunc(x):
    return slope * x + intercept


# df.df.loc['2021-11-08 18'].plot.scatter(x=df.df.columns[1], y=df.df.columns[0])
mymodel = list(map(myfunc, x_data))
plt.scatter(x_data, y_data)
plt.plot(x_data, mymodel, color='r', label=f'slope={slope},\nintercept={intercept}')
plt.legend()  # must be added to show custom label
# plt.show()  # no more needed as plt.legend() added
b = 4

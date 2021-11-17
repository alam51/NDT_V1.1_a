import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


class DfProcessor:
    """
    raw_df = pandas df with column=None and index=None
    source =
        1. 'S' for SCADA (after last update)
        2. 'Sp' for SCADA (before last update)
        3. to be updated....
    """

    def __init__(self, csv_file_path: str, source='S'):
        raw_df = pd.read_csv(csv_file_path, skiprows=[1], parse_dates=[0],
                             infer_datetime_format=True, index_col=[0], dayfirst=False)
        self.df = raw_df.dropna(axis=1, thresh=1)
        for j in self.df.columns:
            self.df[str(j)].replace(to_replace=0, method='bfill', inplace=True)


# file_path = 'F:/Summit Bib 2021.11.16.csv'
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
plt.legend()
plt.show()
b = 4

from matplotlib import pyplot as plt
from scipy import stats
from mpl_toolkits import mplot3d
from data_processor import DfProcessor
import openpyxl as xl

# file_path = 'F:/Bhola_Notun_Biddyut/2021.11.09.csv'
file_path = r'G:\Other computers\My Computer\Data [F]\FGMO\AKS\Dec 2021.csv'
df = DfProcessor(file_path)
# df.df.plot(secondary_y=[df.df.columns[1]])
# df.df.loc[:, 'time'] = df.df.index.to_list()
a = df.df.corr()
a.to_excel('AKS.xlsx')

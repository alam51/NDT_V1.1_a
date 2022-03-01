import datetime
import os
import dateutil.parser as date_parser
import pandas as pd
import traceback

file_path = r'G:\My Drive\Monthly_Report\2021\March\March2021'
files = os.listdir(file_path)
a = 4
t1 = datetime.datetime.now()

df1 = pd.DataFrame()
for file in files:
    try:
        # dt = pd.to_datetime(file,dayfirst=True, yearfirst=False, exact=False, infer_datetime_format=True)
        date = date_parser.parse(file, fuzzy=True, dayfirst=True)
        df = pd.read_excel(os.path.join(file_path,file), sheet_name='P1', usecols='B:E', skiprows=15, nrows=10,
                           index_col=None, header=None)
        br = True
        for i, _ in enumerate(df.index):
            if not br:
                break
            for j, _ in enumerate(df.columns):
                val = df.iloc[i,j]
                if type(val) == str:
                    if 'MMCFD' in val.upper():
                        df1.loc[date-pd.to_timedelta('1 day'), 'MMCFD'] = df.iloc[i,j-1]
                        br = False
                        break
        c = 5
    except Exception:
        traceback.print_exc()

df1.to_excel('MMCFD.xlsx')
print(f'time elapsed {datetime.datetime.now() - t1}')

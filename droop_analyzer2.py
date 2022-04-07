import os
import time

import pandas as pd
import xlsxwriter

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']

worksheet.set_column('D:D', 30)

# Add the VBA project binary.
workbook.add_vba_project('./vbaProject.bin')

# Show text for the end user.
worksheet.write('D3', 'Press the button to say hello.')

# Add a button tied to a macro in the VBA project.
worksheet.insert_button('D5', {'macro': 'say_hello',
                               'caption': 'Press Me',
                               'width': 80,
                               'height': 30})

# Close the Pandas Excel writer and output the Excel file.
writer.save()

# Pandas doesn't allow a '.xslm' extension but Excel requires
# it for files containing macros so we rename the file.
time.sleep(1)
os.rename('pandas_simple.xlsx', 'pandas_simple.xlsm')

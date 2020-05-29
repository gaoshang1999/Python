from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
import os

path = "C:/Work/TS001/test/"
xls_file = "merged.xlsx"

workbook = Workbook()
sheet = workbook.active
workbook.remove(sheet)
for dirpath, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith('.csv'):
            csv_file = os.path.join(dirpath, filename)
            print(csv_file)

            base = os.path.basename(csv_file)
            print(base)
            new_sheet = workbook.create_sheet(base, 0)

            df = pd.read_csv(csv_file)

            for row in dataframe_to_rows(df, index=False, header=True):
                # print(row)
                new_sheet.append(row)

workbook.save(filename=xls_file)

import pandas as pd

path = 'readExcel.xlsx'
dataFrame = pd.read_excel(path)
print("Data from Excel File:")
print(dataFrame)

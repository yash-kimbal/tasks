import pandas as pd

path = 'readCSV.csv'
dataFrame = pd.read_csv(path)
print("Data from Excel File:")
print(dataFrame)

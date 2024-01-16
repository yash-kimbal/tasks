import pandas as pd
new_dataframe=pd.read_csv('./readCSV.csv')
new_xl=pd.ExcelWriter('./newxl.xlsx')
new_dataframe.to_excel(new_xl,index=False)
new_xl._save()
import pandas as pd
data ={'Name':['Yash','Manish','Shambhavi'],
    'Age':[22,23,20],
    'City':['Fariabad','Delhi','Delhi']}

dataFrame=pd.DataFrame(data)

ouptut_excel_p = 'writeExcel.xlsx'
dataFrame.to_excel(ouptut_excel_p,index=False)

print(f"Data written to {ouptut_excel_p}")
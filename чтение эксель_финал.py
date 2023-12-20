import pandas as pd

file = "C:\\files\\result.xls"
xl = pd.read_excel(file)
for i in range(len(xl['Участник'])):
    print(xl['Участник'][i])
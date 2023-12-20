#экспорт из excel
import xlwings as xw
import pandas as pd

wb=xw.Book("c://files/zb.xlsx")
data_excel = wb.sheets['3']
data_pd = data_excel.range('A1:C6').options(pd.DataFrame, header = 1, index = False).value
print(data_pd)


 
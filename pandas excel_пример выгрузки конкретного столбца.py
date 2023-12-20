# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:28:49 2023

@author: S.Stycenkov
"""

import pandas as pd
import time



df = pd.read_excel('C:/files/marketdata/m2.xlsx', usecols=[1])

#вырезает конкретные строки
df2 = pd.read_excel('C:/files/marketdata/m2.xlsx', skiprows=[1,2])

print(df)
print(df2)

'''
Параметры:
dtype – Dict with column name an type.
nrows – How many rows to parse.
na_values – Additional strings to recognize as NA/NaN. 
keep_default_na – Whether or not to include the default NaN values when parsing the data. 
na_filter – Filters missing values.
parse_dates – Specify the column index you wanted to parse as dates
thousands – Thousands separator for parsing string columns to numeric.
skipfooter – Specify how to rows you wanted to skip from the footer.
mangle_dupe_cols – Duplicate columns will be specified as ‘X’, ‘X.1’, …’X.N’,     
'''    

# print(*[column for column in df])
# for i in range(len(df['A'])):
#     print(df['B'][i], end="\t")
# print()
# for i in range(len(df['A'])):
#     print(df['C'][i], end="\t")

# start_script=time.time()
# p = []
# for i in range(len(df['A'])):
#     p.append(15 - i)
# df['A'] = p

# finish_script=time.time()

# print(p)
# print('time=', finish_script - start_script)

# start_script2=time.time()
# for i in range(len(df['A'])):
#     df['B'][i] = 15 - i
# finish_script2=time.time()

# print('time2=', finish_script2 - start_script2)

# if finish_script - start_script > 0:
#     print('time2 / time1', (finish_script2 - start_script2)/(finish_script - start_script))

# print(df)

# df.iloc[0,2]=3.1415926

# print(df.iloc[1])S
# print(len(df.iloc[1]))



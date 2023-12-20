# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:59:26 2023

@author: S.Stycenkov
"""

import pandas as pd

# russianwords = pd.read_csv('C:\\files\marketdata\russianwords2.txt', sep=" ", header=None)

df = pd.read_excel('C:/files/marketdata/russiantext.xlsx', header=None)

df.columns=['A']

# print(df['A'][0:15])

# print(df['A'].str.contains('океан').any())

#проверка:
     
m = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
n=[]

ind=0
wordind=0
for i in m:
    for j in m:
        s = "ма" + i + j + "а"
        ind += 1
        if df['A'].str.contains(str(s)).any():    
            n.append(s)
            print(len(n), ": ", s, sep="")
            wordind += 1
            if wordind % 5 == 0:
                print()
            
print()            
print(*n)

if wordind == 0:
    print('слов не найдено')
else:
    print(f"за {ind} итераций")
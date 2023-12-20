# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:59:26 2023

@author: S.Stycenkov
"""

import pandas as pd

# russianwords = pd.read_csv('C:\\files\marketdata\russianwords2.txt', sep=" ", header=None)

dict = 1

if dict ==1 :
    txtdict = ""
    txtnamedic = "Словарь I : "
else:
    txtdict = "2"
    txtnamedic = "Словарь II : "

df = pd.read_excel("C:/files/marketdata/russiantext" + txtdict + ".xlsx", header=None)

df.columns=['A']

# print(df['A'][0:15])

# print(df['A'].str.contains('океан').any())

#проверка:
print('-' * 25)
print('5 букв: подбор вариантов')
print()
     
m = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
# m = 'цугшщзхъфыплжэячсмитьбю'
n=[]

ind=0
wordind=0
for i in m:
    for j in m:
        for k in m:
            s =  i + j  + k + "ба"
            ind += 1
            if df['A'].str.contains(str(s)).any():    
                n.append(s)
                print(len(n), ": ", s, sep="")
                wordind += 1
print()
print('-' * 25)
print()
print(*n, sep = " | ")
print()
print('-' * 25)
print()
if wordind == 0:
    print(txtnamedic + ' слов не найдено')
else:
    print(txtnamedic + str(wordind), end = '')
    print(f" слов за {ind} итераций")
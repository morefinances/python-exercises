# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:59:26 2023

@author: S.Stycenkov
"""

import pandas as pd
import colorama
from colorama import Fore, Style, Back
from datetime import datetime

# russianwords = pd.read_csv('C:\\files\marketdata\russianwords2.txt', sep=" ", header=None)

time1 = datetime.now()

dict = 2

if dict == 1 :
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
print('5 букв: подбор вариантов.')
print(txtnamedic[:10])
print()
     
m = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
# m = 'йцукенгшщзхъфывапролджэячсмитьбю' #все буквы
# m = 'йцугщзъфвлджэячитб' #выборка
n=[]

ind=0
wordind=0
for i in m:
    for j in m:
        for k in m:
            s = i + "а" + j + "о" + k 
            ind += 1
            if df['A'].str.contains(str(s)).any():    
                n.append(s)
                print('{:3d}'.format(len(n)), ": ", s, sep="")
                wordind += 1
print()
colorama.init()
print(Fore.BLUE, end = "") # Style.BRIGHT
print('--' * 25)
print(Style.RESET_ALL, end="")
print(Fore.BLUE, end = "")
print(*n, sep = " | ")
print('--' * 25)
print(Style.RESET_ALL, end="")
print()

if wordind == 0:
    print(txtnamedic + ' слов не найдено')
else:
    print(txtnamedic + str(wordind), end = '')
    print(f" слов за {ind} итераций")

time2 = datetime.now()
print('Найдено за ' + str(time2-time1).split('.')[0])


# # прицеливаемся по буквам
# print('--' * 25)
# for i in n:
#     if i[3]=="и":
#         print(i)

# # удаление задвоение букв
# print()
# print('--' * 25)
# ind = 1
# for i in n:
#     if i.count('о')==1:
#         print("{:3d}".format(ind), '> ', i, sep ='')
#         ind += 1
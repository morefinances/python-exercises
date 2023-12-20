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

word_for_work = "*а**о"

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

word_symbol = []
location_symbol = []

word_symbol.append('е')
location_symbol.append(2)

word_symbol.append('о')
location_symbol.append(5)

n=[]
wordind=0
if len(word_symbol) == 2:
    for i in df['A']:
        if i[location_symbol[0]-1] == word_symbol[0] and \
            i[location_symbol[1]-1] == word_symbol[1] and \
                i not in n:
                # print(i)
                n.append(i)
                print('{:3d}'.format(len(n)), ": ", i, sep="")
                wordind += 1


dopsymbols = 'т'

m = []

if len(dopsymbols) == 1:
    for u in range(len(n)):
        if dopsymbols[0] in n[u]: 
            m.append(n[u])


if len(dopsymbols) == 2:
    for u in range(len(n)):
        if dopsymbols[0] in n[u] and dopsymbols[1] in n[u]: 
            m.append(n[u])
            # print(u, n[u])
            


print()
colorama.init()
print(Fore.BLUE, end = "") # Style.BRIGHT
print('--' * min(4 *(len(m)),39))
print(Style.RESET_ALL, end="")
print(Fore.BLUE, end = "")
print(*m, sep = " | ")
print('--' * min(4 *(len(m)),39))
print(Style.RESET_ALL, end="")
print()

if wordind == 0:
    print(txtnamedic + ' слов не найдено')
else:
    print(txtnamedic + str(wordind) + " слов")
    # print(f" слов")

print(f'Под дополнительные условия подпадают : {len(m)} слов(а)')

time2 = datetime.now()
print('Найдено за ' + str(time2-time1).split('.')[0])


# # # прицеливаемся по буквам
# # print('--' * 25)
# # for i in n:
# #     if i[3]=="и":
# #         print(i)

# # # удаление задвоение букв
# # print()
# # print('--' * 25)
# # ind = 1
# # for i in n:
# #     if i.count('о')==1:
# #         print("{:3d}".format(ind), '> ', i, sep ='')
# #         ind += 1
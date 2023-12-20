# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:59:26 2023

@author: S.Stycenkov
"""

import pandas as pd
import colorama
from colorama import Fore, Style, Back
from datetime import datetime


word_for_work = "**е**"

dopsymbols = ''



time1 = datetime.now()

def work_symbol(myword):
    global word_symbol
    word_symbol = []
    
    global location_symbol
    location_symbol = []
    
    for i in range(len(myword)):
        if myword[i] != "*":
            word_symbol.append(myword[i])
            location_symbol.append(i)

work_symbol(word_for_work)

dict = 2

if dict == 1 :
    txtdict = ""
    txtnamedic = "Словарь I : "
else:
    txtdict = "2"
    txtnamedic = "Словарь II : "

df = pd.read_excel("C:/files/marketdata/russiantext" + txtdict + ".xlsx", header=None)

df.columns=['A']



#проверка:
print('-' * 25)
print('5 букв: подбор вариантов.')
print(txtnamedic[:10])
print()



n=[]
wordind=0

if len(word_symbol) == 1:
    for i in df['A']:
        if i[location_symbol[0]] == word_symbol[0] and \
            i not in n:
                # print(i)
                n.append(i)
                print('{:3d}'.format(len(n)), ": ", i, sep="")
                wordind += 1


if len(word_symbol) == 2:
    for i in df['A']:
        if i[location_symbol[0]] == word_symbol[0] and \
            i[location_symbol[1]] == word_symbol[1] and \
                i not in n:
                # print(i)
                n.append(i)
                print('{:3d}'.format(len(n)), ": ", i, sep="")
                wordind += 1






if len(dopsymbols) == 0:
    m = n
else:
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

if len(dopsymbols) >= 0:
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
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:31:58 2023

@author: S.Stycenkov
"""

import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/titanic.csv"

titanic = pd.read_csv(url)

print(titanic[titanic['Age']>35])

# t=titanic[titanic.Name.str.contains('Rebecca')].head(10)

global_str = ""

for i in range(len(titanic['PassengerId'])):
    global_str += titanic.Name[i] + ' '



not_word = ['.', ',', 'Mr', 'Mrs', 'Miss', '(', ')', '"']

for u in not_word:
    global_str=global_str.replace(u, '')
    
    
print(global_str)

name_words = global_str.split()

listname_word = list(set(name_words))
listname_word.sort()
# print(*listname_word)

mn = [0 for i in range(len(listname_word))]

mnn = {'Names': listname_word, 'Q': mn}

mdata=pd.DataFrame(mnn)

for i in range(len(listname_word)):
    mdata['Q'][i] = name_words.count(mdata['Names'][i])
    print(mdata['Names'][i])
    
print(mdata[mdata['Q']>5])

t = titanic[titanic.Name.str.contains('Anna')]

t.to_excel('./t1.xlsx')
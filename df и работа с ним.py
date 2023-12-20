# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:44:23 2023

@author: S.Stycenkov
"""

import pandas as pd
from random import randint

c=range(5)
print(c[2])

aa = [i for i in range(10)]

d = {'a': aa,
     'b': [ randint(0,10) for i in aa],
     'c': [ randint(0,10) / 10 for i in aa]}

df = pd.DataFrame(d)

print(df)
print()
print(df[(df['b']>=5) & (df['c']>=0.5)])
print('= ' * 7)

print('query:')
print(df.query('b>=5 and c>=0.5'))
print('= ' * 7)

print(df[(df.a >=9) | (df.b >= 0.9)])

print()

print(df['b'].tolist())    #столбец в список
print(df.columns.tolist()) #значение столбцов

aa=df.copy(deep=True)

print('= ' * 7)
#изменение df
df.query('a>=5 and c>=0.8', inplace=True)

print('= ' * 7)
print(df)


print('= ' * 7)
print(aa)
print('= ' * 7)
print(aa.sample(frac=0.5))

#пройти по всем значениям по строчно
for idx, row in aa.iterrows():
    print(idx, '\n', row)
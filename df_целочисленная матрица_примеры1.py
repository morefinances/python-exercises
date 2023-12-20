# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:28:42 2023

@author: S.Stycenkov
"""

import pandas as pd
import numpy as np
import copy as cp

N = 10
m = 21

a = [0] * N
for i in range(N):
    a[i] = [np.random.randint(9) for i in range(N)]

df = pd.DataFrame(a, columns = list('abcdefgijk'))

for i in range(len(a)):
    for u in range(len(a[i])):
        print(a[i][u],'\t', end="")
    print()
print('==' * m)

print(df)
print('- ' * m)

print(df.query('(a >= b) & (b >= c)'))
print('- ' * m)

print(df.query('((a - b) >= 10) & ((b + c) >=15)'))
print('- ' * m)

print(df.query('c == [1, 2, 3]')) #вывод только с = 1 or = 2 or =3
print('- ' * m)

print(df.query('c != [1, 2, 3]')) #вывод только с = 1 or = 2 or =3
print('- ' * m)

# print(df.query('(a > b) & (b > c)'))

a = df.index.tolist()
b = df.columns.tolist()
for i in range(len(a)):
    print(a[i],'\t', end="")
print()
for i in range(len(a)):
    print(b[i],'\t', end="")

print('\n'*2)

df2 = cp.deepcopy(df)
print(df2)
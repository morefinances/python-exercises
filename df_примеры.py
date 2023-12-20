# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:04:18 2023

@author: S.Stycenkov
"""

import pandas as pd
import random as rnd


mypoint = [ (i + 1) for i in range(10) ]
chanceA = [ rnd.randint(i, 99) for i in range(10) ]
chanceB = [ rnd.randint(i, 99) for i in range(10) ]

df = pd.DataFrame({'A':mypoint,
                   'B':chanceA,
                   'C':chanceB
                   }, index = list('abcdefghij'))

print(df[['A','C']])
print('')
print(df.loc[['b','c','d']])
print('')
print(df[df['C']>=50])
print('')
print(df.query('A==5'))


# print(df.style.background_gradient(subset=["A", "50%"], cmap="Reds"))


print(df)
print()
print(df.max(axis=1))

print()
print(df.nlargest(5, 'B')) #nsmallest - наименьшие значения

print(df.B.idxmax())



# print(df.shape[0])

# for i in range(df.shape[0]):
#     print(df.iloc[i], '\n')

# print(df.describe())
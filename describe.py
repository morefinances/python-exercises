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

print(df.loc[['b','c','d']])

# print(df.describe())
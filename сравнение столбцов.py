# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:55:26 2023

@author: S.Stycenkov
"""

import pandas as pd
import numpy as np

n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
# df = pd.DataFrame(np.random.randint(n, size=(n, 2)), columns=list('bc'))
# целочисленный датафрейм

print(df)

print(df[(df['a'] < df['b']) & (df['b'] < df['c'])])

print(df.query('(a < b) & (b < c)'))

print(df.query('index > b < c'))
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:44:23 2023

@author: S.Stycenkov
"""

import pandas as pd

c=range(5)
print(c[2])

aa = [i for i in range(10)]

d = {'a': aa,
     'b': [ int(i ** 2)  for i in aa],
     'c': [ int( 10 * i ** 0.5 ) / 10 for i in aa]}

df = pd.DataFrame(d)

print(df)
print()
print(df[(df['b']>=10) & (df['c']>=2.6)])


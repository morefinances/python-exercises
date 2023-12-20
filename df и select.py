# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:33:18 2023

@author: S.Stycenkov
"""


import pandas as pd
from random import randint
import numpy as np

aa = [i for i in range(20)]

d = {'a': aa,
     'b': [ randint(1,9) for i in aa],
     'c': [ randint(1,9) / 10 for i in aa]}

df = pd.DataFrame(d)

print(df)

conditions = [
    (df.b == 1),
    (df.b > 1) & (df.b < 9),
    (df.b == 9)
]

values = ['u', 'un', 'ten' ]
  
df['d'] = np.select(conditions, values)

print(df)
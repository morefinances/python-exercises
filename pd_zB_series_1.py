# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:59:01 2023

@author: S.Stycenkov
"""

import pandas as pd
import numpy as np

# s1 = pd.Series(np.random.randn(6), index=list('abcdef'))


s = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])
print(s)

print(s.loc[3:5])

print(s.sort_index())

print(s.sort_index().loc[1:6])

print(s.iloc[:3])

s2 = s.sample()
print(s2)
s3 = s.sample(n=3)
print(s3)
s4 = s.sample(frac=0.8)
print(s4)

example_weights = [0, 0.2, 0.2, 0.2, 1]

# автоматическое перенормирование весов

print(s.sample(n=3, weights=example_weights))

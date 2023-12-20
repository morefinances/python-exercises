# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:59:01 2023

@author: S.Stycenkov
"""


import pandas as pd
import numpy as np

 

N = 100


# print(index)
s1 = pd.Series(np.random.randn(N), index=[i for i in range(N)])
print(s1[(s1>0.2) | (s1<-0.2)])
print(len(s1[(s1>0.2) | (s1<-0.2)]))
print(s1[~(s1<0)])
print(len(s1[~(s1<0)]))


print(s1.where(s1>0))
print(s1.where(s1>0, 10)) #, inplace=True меняет в т.ч. сам датафрейм
print(s1.where(s1>0, -s1))
# print(s1.isin([2, 4, 6]))

s2 = s1.copy()
s2[s2 < 0] = 0
print(s2)
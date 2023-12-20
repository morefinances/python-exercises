# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:28:42 2023

@author: S.Stycenkov
"""

import pandas as pd
import numpy as np

N = 5

a = [0]*N
for i in range(N):
    a[i] = [np.random.randint(9) for i in range(N)]


for i in range(len(a)):
    print(a[i])
# df = pd.DataFrame([[i for i in range(10)]])
# print(df)
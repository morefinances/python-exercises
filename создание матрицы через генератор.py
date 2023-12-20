# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:48:32 2023

@author: S.Stycenkov
"""
import numpy as np
import pprint

N = 10
A = [[np.random.randint(9) for i in range(N)] for i in range(N) ]

# for i in range(len(A)):
    # print(A[i])
    
pprint.pprint(A)

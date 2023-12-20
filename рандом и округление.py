# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:52:54 2023

@author: S.Stycenkov
"""

import random
import math


for i in range(20):
    ri = 100*random.random()
    print(i, "\t", ri)
    print("\t", ri - math.floor(ri))
    print("\t", ri - int(ri))
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:41:35 2023

@author: S.Stycenkov
"""

import random 
values = [10, 20, 30]
data = random.choices(values, weights=[0.9, 0.05, 0.05], k=100)
print(data)
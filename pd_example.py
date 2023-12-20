# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:48:16 2023

@author: S.Stycenkov
"""

import pandas as pd

abc_ex = pd.Series([10,5,8,12],
                   index = ['a','b','x','x'],
                   name = 'example')
print(abc_ex['x'])
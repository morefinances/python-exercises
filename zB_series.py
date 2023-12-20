# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:13:08 2023

@author: S.Stycenkov
"""

import pandas as pd
example = pd.Series([10, 121, None, 115, 1025],
                    name = 'zB_data',
                    index=['A', 'B', 'C', 'E', 'F'])
print(example)
print('-'*25)
print(example.count())
print(example.mean())
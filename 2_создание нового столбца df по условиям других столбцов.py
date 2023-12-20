# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:47:36 2023

@author: S.Stycenkov
"""

# Если у вас есть несколько условий, вы можете использовать numpy.select()  для достижения этого. Скажем, в соответствии с тремя условиями есть три варианта выбора цвета, с четвертым цветом в качестве запасного варианта вы можете сделать следующее.

import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': list('ABBC'), 'col2': list('ZZXY')})

conditions = [
     (df['col2'] == 'Z') & (df['col1'] == 'A'),
     (df['col2'] == 'Z') & (df['col1'] == 'B'),
     (df['col1'] == 'B')
]
 

choices = ['yellow', 'blue', 'purple']

df['color'] = np.select(conditions, choices, default='black')

print(df)

# Out[216]: 
#   col1 col2   color
# 0    A    Z  yellow
# 1    B    Z    blue
# 2    B    X  purple
# 3    C    Y   black
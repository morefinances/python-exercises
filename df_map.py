# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:04:18 2023

@author: S.Stycenkov
"""

import pandas as pd
import random as rnd
import numpy as np


mypoint = [ (i + 1) for i in range(10) ]
chanceA = [ rnd.randint(i, 99) for i in range(10) ]
chanceB = [ rnd.randint(i, 99) for i in range(10) ]

df = pd.DataFrame({'A':mypoint,
                   'B':chanceA,
                   'C':chanceB
                   }, index = list('abcdefghij'))


#-------------------------------------------------------

df['d2'] = df['C'].apply(lambda x: 0 if x% 2 == 0 else 1)

yes_no_diction = {0: 'yes', 1: 'no'}

df['yes/no'] = df['d2'].map(yes_no_diction)


print(df)

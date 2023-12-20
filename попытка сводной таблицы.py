# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:48:33 2023

@author: S.Stycenkov
"""

import numpy as np
import pandas as pd

# df = pd.read_csv('C:/Users/S.Stycenkov/Documents/alfac/marketdata/tz.csv', encoding = "utf-8-sig", delimiter=';')


df = pd.read_excel('C:/Users/S.Stycenkov/Documents/alfac/marketdata/tz.xlsx')

print(df.groupby('Возраст').mean())
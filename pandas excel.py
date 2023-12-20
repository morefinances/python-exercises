# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:28:49 2023

@author: S.Stycenkov
"""

import pandas as pd


df = pd.read_excel('C:\\files\marketdata\m2.xlsx')
print(df)

print(*[column for column in df])
for i in range(len(df['A'])):
    print(df['B'][i], end="\t")
print()
for i in range(len(df['A'])):
    print(df['C'][i], end="\t")
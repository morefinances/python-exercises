# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:05:02 2023

@author: S.Stycenkov
"""

import pandas as pd

t=pd.DataFrame([i for i in range(1, 11)])
print(t)

t.to_excel('./teams.xlsx')
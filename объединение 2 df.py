# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:13:59 2023

@author: S.Stycenkov
"""

import pandas as pd

i = pd.DataFrame([101,109,108],[1,2,3])
i.columns=['mean']

y = pd.DataFrame([11,18,16,18],[1,2,3,4])
y.columns=['mean2']

z=[i, y]

df2=pd.concat(z, axis=1)  #иногда: ignore_index=True
                          #полное описание:
                          #https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
                          #https://rukovodstvo.net/posts/id_606/ - русскоязычная версия
                          
                          
df3=i.join(y, on=None, how='right', lsuffix='', rsuffix='', sort=False)                          

df4 = i.append(y, ignore_index=True)

df5 = pd.concat([i, y], axis=1)

print("\n", df3, "\n\n", df4, "\n\n", df5)
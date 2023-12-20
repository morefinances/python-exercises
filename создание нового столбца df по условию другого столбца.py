# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:47:36 2023

@author: S.Stycenkov
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': list('ABBC'), 'col2': list('ZZXY')})

df['color'] = np.where(df['col2'] == 'Z', 'green', 'red')

print(df)
 
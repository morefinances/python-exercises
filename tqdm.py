# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:19:40 2023

@author: S.Stycenkov
"""

import time
import tqdm

# mylist = [i for i in range(20)]

for i in tqdm.tqdm(range(10)):
    print(i)
    # time.sleep(1)

# for i in range(100):
#     print(i, end=" ")
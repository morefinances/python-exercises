# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 13:24:19 2023

@author: S.Stycenkov
"""

import random

x = [random.randint(0, 100)/10 for i in range(100)]
print(x)
print()

ind = 1
for elem in x:
    if elem-int(elem) == 0:
        print(ind, "\t", elem)
        ind += 1

u = enumerate(x, start=1)



for it, elem in u:
    print(f"{elem} : {it}")

print(*u)
    
print("Final")
        

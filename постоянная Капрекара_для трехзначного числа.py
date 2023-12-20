# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:27:58 2023

@author: S.Stycenkov

"""

import random

def Kaprekara(numbe):
    numb = list(str(numbe))
    a=sorted(numb)
    c=a[::-1]
    b=int(''.join(a))
    d=int(''.join(c))
    return d-b

delta=0
m=random.randint(100,999)
print(m)

# for i in range(10):
while delta!= 495:
    delta=Kaprekara(m)
    print(delta)
    m=delta
# print(m)
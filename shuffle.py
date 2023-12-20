# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:55:52 2023

@author: S.Stycenkov
"""

import random as rd

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@%&_abcdefghijklmnopqrstuvwxyz1234567890'

a=list(s)
rd.shuffle(a)
a=''.join(a)


print(a)
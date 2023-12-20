# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:48:59 2023

@author: S.Stycenkov
"""

import random as rd

s = 0
N = 1000
for i in range(N):
    # rd.seed(i + rd.randint(1,999))
    number_one = 10*rd.randint(0,9)
    #print(number_one)
    # rd.seed(i + rd.randint(1,999))
    number_two = rd.randint(0,99)
    if number_one == number_two:
        print(s,": ",number_one, sep ="")
        s += 1
print("Всего совпадений:", s, " вероятность: ", s/N*100, "%", sep="")
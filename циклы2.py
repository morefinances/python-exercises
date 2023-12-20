# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:10:31 2023

@author: S.Stycenkov
"""

def myint(x):
    return x - int(x) == 0

a = [[0] * 10 for i in range(10)] 


x = 0
xx = 0

for R in range(10, 20): #(5, 100, 5):
    for r in range(5, 15):
        #a[xx][x] = R / r
        i = 1
        while i<=r: #(i * R / r) // 10 != 0:
            if myint(i * R / r):
                print("R= ", R, "r= ", r, "i=", i, i * R / r, myint(i * R / r))
                a[xx][x] = i * R / r
                # i = r
                break
            else:
                i += 1
        else:
            a[xx][x] = R
        x += 1
        if x >= 10:
            x = 0
            xx += 1



for row in a:
    print('\t'.join([str(int(elem)) for elem in row]))

for row in a:
    print(*row)

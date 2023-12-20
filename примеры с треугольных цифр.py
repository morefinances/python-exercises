# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:11:40 2023

@author: S.Stycenkov
"""

N = 5

def hr_line():
    print()
    print('-'*25)
    print()

hr_line()
for i in range(1, N + 1):
    print(str(i)*i)

hr_line()

for i in range(1, N + 1):
    print(str(i)* (6 - i))
    
hr_line()

for i in range(1, N + 1):
    print(str(5)* (6 - i))

hr_line()

for i in range(N, 0 , -1):
    for u in range(1, i + 1):
        if u == 1:
            print("0", end = '')
        print(u, end = '')
    print()
    
hr_line()

for i in range(1, N + 1):
    for u in range(i,0,-1):
        print(u, end = '  ')
    print()
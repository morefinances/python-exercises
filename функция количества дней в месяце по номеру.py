# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:36:13 2023

@author: S.Stycenkov
"""

def lastdayofmonth(xmon):
    # if xmon == 1 or xmon == 3 or xmon == 5 or xmon == 7 or xmon ==8 or xmon == 10 or xmon == 12
    if (xmon <=7 and xmon%2 == 1) or (xmon>=8 and xmon%2 == 0):
        return 31
    elif xmon==4 or xmon==6 or xmon==9 or xmon==11:
        return 30
    else:
        return 28
for i in range(12):
    print(i + 1,' = ',lastdayofmonth(i + 1))
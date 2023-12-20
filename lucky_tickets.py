# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:39:09 2023

@author: S.Stycenkov
"""

import datetime as dtm



def luckytickets(numb):
    numb_discr = len(numb)
    if numb_discr%2 == 0:
        half_discr = int(len(numb) / 2)
        # print(half_discr)
        sum_one = 0
        sum_two = 0
        for i in range(half_discr):
            # print(numb[i])
            sum_one += int(numb[i])
            # print(numb[i + half_discr])
            sum_two += int(numb[i + half_discr])
        # print(str(abs(numb))[:half_discr])
        # print(str(abs(numb))[half_discr:])
        if sum_one == sum_two:
            return 1
        else:
            return 0
    # else:
    #     print('Введенное число не четное')
    #     return 0 
    

u = int(input())
t1 = dtm.datetime.now()
print(t1)
if u%2 == 1:
    print('Введенное число не четное')
maxnumb = -1  + 10**u
print(maxnumb)

lucky_sum = 0 
for ii in range(maxnumb + 1):
    if len(str(ii))<len(str(maxnumb)):
        number_string = "0" * (len(str(maxnumb)) - len(str(ii))) + str(ii)
    else:
        number_string = str(ii)
    ticket = luckytickets(number_string)
    lucky_sum += ticket
    print(ii, ': ', number_string, ' /', ticket, ' // ',lucky_sum)
    
    
t2 = dtm.datetime.now()
print(t2)
    
print(lucky_sum)
print('Время работы скрипта:', t2-t1)
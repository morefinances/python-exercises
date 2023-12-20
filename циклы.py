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
                a[xx][x] = i
                # i = r
                break
            else:
                i += 1
        else:
            a[xx][x] = r
        x += 1
        if x >= 10:
            x = 0
            xx += 1



for row in a:
    print('\t'.join([str(elem) for elem in row]))

#print(10/5 // 10)


# a[1][0] = 1
# print(a[1][0])    
# print(a[0][0])    
# print(*a)

# i = 1 #счетчик
# R = 35
# r = 10

# while (i * R / r ) // 10 == 0:
#     print(i, i * R / r)
#     i += 1

# a = [[0] * 5 for i in range(5)] 
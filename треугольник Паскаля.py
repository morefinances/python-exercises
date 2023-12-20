# -*- coding: utf-8 -*-
"""
Created on Mon May 29 13:45:25 2023

@author: S.Stycenkov
"""

def pascalo(numb):
    # m = [[1], [1,1]]    
    m = []
    for i in range(numb):
        n = [1 for i in range(i+1)]
        if i>=2:
            for t in range(len(n)):
                if t == 0 or t == len(n):
                    continue
                if t == 1 or t == (len(n)-2):
                    n[t] = i
                if t >1 and t<(len(n)-2):
                    n[t] = m[i-1][t]+m[i-1][t-1]
        print(*n)
        m.append(n)
    # return m[numb]

pascalo(int(input()))


#----------- компактное решение -----------------
# n = int(input())

# li = [1]
# for i in range(n):
#     for j in range(len(li) - 1):
#         li[j] = li[j] + li[j + 1]
#     li.insert(0, 1)

# print(li)


# ----------------------------------------------
# v = [1]
# for i in range(int(input())):
#     print(*v)
#     v = [1, *[v[i] + v[i + 1] for i in range(len(v) - 1)], 1]
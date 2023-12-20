# -*- coding: utf-8 -*-
"""
Created on Mon May 22 10:37:48 2023

@author: S.Stycenkov
"""

res = ""
t = [int(i) for i in str(input())]
for i in range(len(t)):
    # print(len(t) - i - 1)
    if t[len(t) - i - 1] == 0:
        continue
    if i == 0:
        res = str(t[len(t) - i - 1])
    else:
        res = str(t[len(t) - i - 1] * 10 ** i) + ' + ' + res

if res[-2] == "+":
    print(res[:-2])
else:
    print(res)
 


# result = []
# opens = 0
# ind = 0

# for i in t:
#     if i == "(" and opens == 0:
#         opens = 1
#         ind = 1
#     elif i == ")" and opens ==1:
#         opens = 0
#         result.append(ind+1)
#     else:
#         ind += 1

# print(result)
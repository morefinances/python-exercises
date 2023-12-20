# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:49:24 2023

@author: S.Stycenkov
"""

ENG1 = 'abcdefghijklmnopqrstuvwxyz'
ENG2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
RUS1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
RUS2 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# print(len(ENG1), len(RUS1))

def position(key, string):
    ind = -1
    ind_err = -1 
    for a in string:
        ind +=1
        if a == key:
            ind_err = 0
            break
    if ind_err == 0: 
        return ind
    else:
        return -1
    

def cesar_code(s, key, direct):
# s, key, direct = input(), int(input()), int(input())
    result = ""
    for i in s:
        if i not in RUS1 and i not in RUS2 and i not in ENG1 and i not in ENG2:
            result += i
        if i in RUS1:
            pos=position(i, RUS1)
            if direct == 1:
                if (pos + key) < 32:
                    # print("<=32")
                    # print(i, pos, key, pos + key - 32, result)
                    result +=  RUS1[pos + key]
                else:
                    # print(">32")
                    # print(i, pos, key, pos + key - 32, result)
                    result +=  RUS1[pos + key - 32]
            else:
                if (pos - key) >= 0:
                    result +=  RUS1[pos - key]
                else:
                    result +=  RUS1[pos - key + 32]
        if i in RUS2:
            pos=position(i, RUS2)
            if direct == 1:
                if (pos + key) < 32:
                    result +=  RUS2[pos + key]
                else:
                    result +=  RUS2[pos + key - 32]
            else:
                if (pos - key) >= 0:
                    result +=  RUS2[pos - key]
                else:
                    result +=  RUS2[pos - key + 32]
        if i in ENG1:
            pos=position(i, ENG1)
            if direct == 1:
                if (pos + key) < 26:
                    result +=  ENG1[pos + key]
                else:
                    result +=  ENG1[pos + key - 26]
            else:
                if (pos - key) >= 0:
                    result +=  ENG1[pos - key]
                else:
                    result +=  ENG1[pos - key + 26]
        if i in ENG2:
            pos=position(i, ENG2)
            if direct == 1:
                if (pos + key) < 26:
                    result +=  ENG2[pos + key]
                else:
                    result +=  ENG2[pos + key - 26]
            else:
                if (pos - key) >= 0:
                    result +=  ENG2[pos - key]
                else:
                    result +=  ENG2[pos - key + 26]
    return(result)
    # print(result)

u = "Hawnj pk swhg xabkna ukq nqj."
for x in range(26):
    print(x, cesar_code(u,x,-1))

# print(position("я", RUS1))


# компактный вариант:

# text =  input()

# def eng_scaesar(symbol, key):
#     if not symbol.isalpha():
#         return symbol
#     wA = ord('A') if symbol.isupper() else ord('a')
#     return chr((ord(symbol) - wA + key) % 26 + wA)

# key = int(input())
# s = "".join(eng_scaesar(c, key) for c in text)
# print(s)
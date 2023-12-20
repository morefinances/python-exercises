# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:59:58 2023

@author: S.Stycenkov
"""

# исключаем повторы

import random as rnd
from colorama import Fore, Style, Back

txt = []
distribution = []

txt.append("qwertyuiopasdfghjklzxcvbnm")
distribution.append(0.45)

txt.append("QWERTYUIOPASDFGHJKLZXCVBNM")
distribution.append(0.35)

txt.append("1234567890")
distribution.append(0.1)

txt.append("!@#$%^&*()_-|{}")
distribution.append(0.1)

numb = int(input())
print()


def blueprint(txt_s):
    print(Fore.BLUE, end = "")
    print(txt_s, end = '')
    print(Style.RESET_ALL, end = "")

def grayprint(txt_s):
    print(Fore.WHITE, end = "")
    print(txt_s, end = '')
    print(Style.RESET_ALL, end = "")


for _ in range(20):
    data = rnd.choices(txt, weights=distribution, k=numb)
    passw = ""
    for i in range(len(data)):
        endind = True
        while endind:
            u = rnd.randint(0, len(data[i])-1)
            if str(data[i][u]) not in passw:
                endind = False
        passw += str(data[i][u])
        
    print('{:2d}'.format(_ + 1), ': ', passw, sep = '', end = '')
    
    aa , AA , numb_sym, txt_symb = 0, 0, 0, 0
    
    for x in range(len(passw)):
        if passw[x] in txt[0]:
            aa += 1
        if passw[x] in txt[1]:
            AA += 1
        if passw[x] in txt[2]:
            numb_sym += 1
        if passw[x] in txt[3]:
            txt_symb += 1
    aaa = int(100 * aa / numb)
    AAA = int(100 * AA / numb)
    numb_sym_a = int(100 * numb_sym / numb)
    txt_symb_a = int(100 * txt_symb / numb)
    
    blueprint('\ta: ')
    print('{:2d}'.format(aa), end ='')
    blueprint('\tA: ')
    print('{:2d}'.format(AA), end ='')
    blueprint('\tn: ')
    print('{:2d}'.format(numb_sym), end ='')
    blueprint('\ts: ')
    print('{:2d}'.format(txt_symb), end ='')
    grayprint('\ta: ')
    print('{:2d}'.format(aaa), end ='')
    grayprint('\tA: ')
    print('{:2d}'.format(AAA), end ='')
    grayprint('\tn: ')
    print('{:2d}'.format(numb_sym_a), end ='')
    grayprint('\ts: ')
    print('{:2d}'.format(txt_symb_a))

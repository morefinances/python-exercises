# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:21:21 2023

@author: S.Stycenkov
"""

text = input().split()
position = 0
while len(text) - position > 1: 
    print(text[position + 1],text[position], end=" ")
    position += 2
if len(text)%2 != 0:
    print(text[len(text)-1])
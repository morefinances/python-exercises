# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 14:44:07 2023

@author: S.Stycenkov
"""


function nonzero(text):
    if int(text)<10:
        return '0' + text
    else
        return text

print(nonzero(2))
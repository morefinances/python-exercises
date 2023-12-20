# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:27:17 2023

@author: S.Stycenkov
"""

def out_red(text):
    print("\033[34m{}".format(text))
out_red("ПРИВЕТ")
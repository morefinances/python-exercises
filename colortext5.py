# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:29:18 2023

@author: S.Stycenkov
"""

from termcolor import colored, cprint
print(colored('Привет мир!', 'red', attrs=['underline']))
print('Привет!')
cprint('Вывод с помощью cprint', 'green', 'on_blue')
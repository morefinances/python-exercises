# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:49:15 2023

@author: S.Stycenkov
"""

# import pandas as pd

# df = pd.read_csv('C:\\files\\text.csv')

file1 = open("C:\\files\\AAAcorp.csv", "r")

tikers = []
index = 1

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    if line.strip()[:2] == "RU" and line.strip()[2] != "R":
        print(index, ": ", line.strip())
        tikers.append(line.strip())
        index += 1
        
# закрываем файл
file1.close

print(len(tikers),'\n'*2)

print('"', end="")
print(*tikers, sep = '", "', end='')
print('"', end="")
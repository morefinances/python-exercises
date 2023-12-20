# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:34:30 2023

@author: S.Stycenkov
"""

for i in range(20):
    print("-", end='')
    
Ag=10
AG=1
ag=0.1
print()
print(Ag, AG, ag, sep="\t")
print(type(Ag), type(ag))

s="Добрый вечер! Символьные изменения."
news=''
for a in range(len(s)):
    if a%2==0:
        news += s[a]
    else:
        if s[a] !=' ':
            news += str(a%10)
        else:
            news += s[a]

print(news)
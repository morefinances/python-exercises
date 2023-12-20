# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:17:35 2023

@author: S.Stycenkov
"""

# mylist = "Дракон Змея Лошадь Овца Обезьяна Петух Собака Свинья Крыса Бык Тигр Заяц".split()
# c = int(input())
# print((c+4)%12)
# print(mylist[(c + 4)%12])

# c = int(input())
# print(f'{c:,}')

c = str(input())

txt = ''

for i in range(len(c),-1,-1):
    txt += c[len(i)] 
    # if (len(c) - i - 1) % 3 == 1:
    #     txt = ',' + txt

print(txt)
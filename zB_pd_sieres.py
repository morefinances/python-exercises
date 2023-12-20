

# list_of_number = [1, 10, 110]
# print(str(list_of_number))

import pandas as pd

s = pd.Series([10, 20, 30, 40, 50], ['a', 'b', 'c', 'd', 'e'])
print(s['a':'c'])
print(s[1])
print(s.iloc[1])
print(s[[1,2,3]])
print(s[:3])

w = [0.1, 0.05, 0.68, 0.05, 0.12] # вероятности появления, в сумме =1
print(s.sample(n = 3, weights = w))

s['f']=60
print(s[lambda x: x >= 20])
print(s[s < 30])
print(s.a, '//',s.c)
print(s.sample()) # вывод случайного элемента
print(s.sample(n=3))
print(s.sample(frac=0.8)) #доля от обзего числа объектов в структуре


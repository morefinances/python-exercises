

# list_of_number = [1, 10, 110]
# print(str(list_of_number))

import pandas as pd

d = {"price":[1, 2, 3], "count": [10, 20, 30], "percent": [24, 51, 71]}

df = pd.DataFrame(d, index=['a', 'b', 'c'])

print(df)
print(df['count'])
print(df[['count','price']])
print(df['a':'b'])
print(df[lambda x: x['count'] > 15])
print(df[df['price'] >=3])

print(df.sample())
print(df.sample(axis=1))
print(df.sample(n=2, axis=1))
print(df.sample(n=2))

df['value'] = [3, 14, 7]
print(df)

print(df[df['price']>=2])
print('-'*50)
print(df)
print(df.columns)
print(df.index)
print('количество строк =',len(df))
print('количество столбцов =',len(df.columns))
print('количество строк и столбцов =',df.shape)
print('количество значений =', df.size)
print(df.price[:3])
print(df[df.price>=2])
print(df.loc['a']) # получить строку
print(df['a':'c'])
print(df.iloc[[0, 1]]) #отбор строк по позициям
print(df[:1]) # первая строка
print(df[:-1]) # последняя строка

print(df.percent>=50)       #bool серия
print(df[df.percent>=50])   #отбор строк по ней
print(df[(df.percent>=50) & (df.price == 2)]) # множественные условия
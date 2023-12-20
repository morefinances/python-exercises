import pandas as pd

df = pd.read_excel('C:/files/marketdata/m5.xlsx', sheet_name='B', usecols=[1,2])

#вырезает конкретные строки
# df2 = pd.read_excel('C:/files/marketdata/m2.xlsx', skiprows=[1,2])

print(df)
print(df.columns[-1])
print(max(df.index))

print('\n', 'количество строк и столбцов:', sep="")
print(df.shape)

print('\n', 'количество строк', sep="")
print(len(df))

print('\n', 'количество значений', sep="")
print(df.size)



# print(df.columns.ravel())

# b = df[1].tolist()

# print(b)
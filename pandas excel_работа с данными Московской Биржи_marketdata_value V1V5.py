import pandas as pd
import time


start_script=time.time()

df = pd.read_excel('C:/files/marketdata/market_value.xlsx')

#, sheet_name='B', usecols=[1,2]

#вырезает конкретные строки
# df2 = pd.read_excel('C:/files/marketdata/m2.xlsx', skiprows=[1,2])

# print(df)
# print(df.columns[-1])
# print(max(df.index))

# print('\n', 'количество строк и столбцов:', sep="")
# print(df.shape)

# print('\n', 'количество строк', sep="")
# print(len(df))

# print('\n', 'количество значений', sep="")
# print(df.size)


TOD = df.columns[-1]
YEST = df.columns[-2]



deltaValue=pd.DataFrame(df[df.columns[0]])
deltaValue.columns=['Ticker']
deltaValue['Name']=df[df.columns[1]]
deltaValue['V1/V2']=df[TOD]/df[YEST]
 


# # print(type(deltaValue))
# deltaValue.insert(0, 'Name', df[df.columns[0]], False)
# deltaValue.insert(1, 'Name', df[df.columns[1]], False)

# deltaValue.index = df[df.columns[0]]








deltaValue['V1/V2']=deltaValue['V1/V2'].map(lambda x: round (x, 2))


# расчет V1/V2
# ValueRating = deltaValue['V1/V2'].sort_values(ascending=False)
ValueRating = deltaValue.sort_values(by=['V1/V2'], ascending=False)
ValueRating=ValueRating.dropna()

ValueRating.reset_index(drop= True , inplace= True )
ValueRating.index += 1
# финал

#  сортировка объема, убираем нулевые
totalResult=pd.DataFrame(df[df.columns[0]])
totalResult.columns=['Ticker']
totalResult['Name']=df[df.columns[1]]
totalResult['Volume']=df[TOD]
totalResult = totalResult.sort_values(by=['Volume'], ascending=False)
totalResult = totalResult[totalResult['Volume']>0]

totalResult.reset_index(drop= True , inplace= True )
totalResult.index += 1



# находим SMA
namelist=[]
for i in range(-1, -6, -1):
    namelist.append(df.columns[i])

totalResult2=pd.DataFrame(df[df.columns[0]])
totalResult2.columns=['Ticker']
totalResult2['Name']=df[df.columns[1]]
totalResult2['5SMA']=df[namelist].mean(axis=1)

totalResult3=totalResult2

totalResult2 = totalResult2.sort_values(by=['5SMA'], ascending=False)
totalResult2 = totalResult2[totalResult2['5SMA']>0]

totalResult2.reset_index(drop= True , inplace= True )
totalResult2.index += 1

totalResult3[]

print(totalResult3)




# print(totalResult)




# p1 = ValueRating.index
# print(p1)
# print(list(p1))

# ValueRating=ValueRating.dropna()

# # print(deltaValue)

# print()

# print(ValueRating)

# print()

# # print(df[df.columns[0]])

finish_script=time.time()

print('time=', finish_script - start_script)



#  запись в файл
# ValueRating.to_csv('C:/files/marketdata/V1V5.csv', sep=',', encoding='utf-8-sig')


# encoding='utf-8'
# print(df.columns.ravel())
# b = df[1].tolist()
# print(b)
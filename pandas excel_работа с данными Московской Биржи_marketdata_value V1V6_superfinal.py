import pandas as pd
import time


start_script=time.time()

df = pd.read_excel('C:/files/marketdata/market_value2.xlsx')

#, sheet_name='B', usecols=[1,2]

#вырезает конкретные строки
# df2 = pd.read_excel('C:/files/marketdata/m2.xlsx', skiprows=[1,2])

# print(df)
# print(df.columns[-1])
# print(max(df.index))


#создание первого df
#объемы: тикеры и название бумаг
# в дальнейшем остальные скопируются по аналогии
Volume=pd.DataFrame(df[df.columns[0]])
Volume.columns=['Ticker']
Volume['Name']=df[df.columns[1]]


#копируем все df
V1bV2 = Volume.copy(deep=True)
SMA5V = Volume.copy(deep=True)
VbSMA5V = Volume.copy(deep=True)
SMA20V = Volume.copy(deep=True)
VbSMA20V = Volume.copy(deep=True) 
SMA5b20SMAV = Volume.copy(deep=True)


#столбец объемов
Volume['V']=pd.DataFrame(df[df.columns[-1]])
# сортировка 
Volume=Volume.sort_values(by=['V'], ascending=False)
# исключаем нулевые
Volume=Volume[Volume['V']>0]
# правка индексов
Volume.reset_index(drop= True , inplace= True )
Volume.index += 1

# последние и предпоследние объемы
TOD = df.columns[-1]
YEST = df.columns[-2]

# находим отношение, сортировка и исключаем NaN
V1bV2['V1/V2']=df[TOD]/df[YEST]
V1bV2 = V1bV2.sort_values(by=['V1/V2'], ascending=False)
V1bV2 = V1bV2.dropna()

# правка индексов
V1bV2.reset_index(drop= True , inplace= True )
V1bV2.index += 1
# округление
V1bV2['V1/V2']=V1bV2['V1/V2'].map(lambda x: round (x, 2))

# объединяем результаты
totalResult = pd.concat([Volume, V1bV2], axis=1)

# расчет средней за 5
# номера дней
namelist5=[]
for i in range(-1, -6, -1):
    namelist5.append(df.columns[i])

print('namelist=', namelist5)

# расчет средней 5SMA
SMA5V['5SMA']=df[namelist5].mean(axis=1)
# здесь же сразу расчет V/5SMA, т.к. далее средняя будет сортироваться и урезаться
VbSMA5V['VbSMA5V']=df[TOD]/SMA5V['5SMA']

SMA5c=SMA5V.copy(deep=True)

# сортировка средней
SMA5V = SMA5V.sort_values(by=['5SMA'], ascending=False)
# отсекаем нулевые
SMA5V=SMA5V[SMA5V['5SMA']>0]
# правка индексов
SMA5V.reset_index(drop= True , inplace= True )
SMA5V.index += 1

# сортировка V/5SMA
VbSMA5V = VbSMA5V.sort_values(by='VbSMA5V', ascending=False)
# отсекаем нулевые
VbSMA5V =VbSMA5V[VbSMA5V['VbSMA5V']>0]
VbSMA5V['VbSMA5V']=VbSMA5V['VbSMA5V'].map(lambda x: round (x, 2))
# правка индексов
VbSMA5V.reset_index(drop= True , inplace= True )
VbSMA5V.index += 1

print(SMA5V)

# объединение таблиц
totalResult = pd.concat([totalResult, SMA5V], axis=1)
totalResult = pd.concat([totalResult, VbSMA5V], axis=1)


print(VbSMA5V)
#... продложение





# расчет средней за 20
# номера дней
namelist20=[]
for i in range(-1, -21, -1):
    namelist20.append(df.columns[i])

print('namelist20=', namelist5)

# расчет средней 5SMA
SMA20V['20SMA']=df[namelist20].mean(axis=1)
# здесь же сразу расчет V/5SMA, т.к. далее средняя будет сортироваться и урезаться
VbSMA20V['VbSMA20V']=df[TOD]/SMA20V['20SMA']

SMA20c=SMA20V.copy(deep=True)

# сортировка средней
SMA20V = SMA20V.sort_values(by=['20SMA'], ascending=False)
# отсекаем нулевые
SMA20V=SMA20V[SMA20V['20SMA']>0]

SMA20V.reset_index(drop= True , inplace= True )
SMA20V.index += 1


VbSMA20V = VbSMA20V.sort_values(by=['VbSMA20V'], ascending=False)
# VbSMA20V = VbSMA20V.dropna()
VbSMA20V = VbSMA20V[VbSMA20V['VbSMA20V']>0]

VbSMA20V['VbSMA20V']=VbSMA20V['VbSMA20V'].map(lambda x: round (x, 2))

VbSMA20V.reset_index(drop= True , inplace= True )
VbSMA20V.index += 1

print(VbSMA20V)

totalResult = pd.concat([totalResult, SMA20V], axis=1)
totalResult = pd.concat([totalResult, VbSMA20V], axis=1)



SMA5b20SMAV['SMA5b20'] = SMA5c['5SMA'] / SMA20c['20SMA']
SMA5b20SMAV = SMA5b20SMAV.sort_values(by=['SMA5b20'], ascending=False)
SMA5b20SMAV =SMA5b20SMAV.dropna()

SMA5b20SMAV['SMA5b20'] = SMA5b20SMAV['SMA5b20'].map(lambda x: round (x, 2))

# правка индексов
SMA5b20SMAV.reset_index(drop= True , inplace= True )
SMA5b20SMAV.index += 1


print(SMA5b20SMAV)

totalResult = pd.concat([totalResult, SMA5b20SMAV], axis=1)

# финально: запись в файл csv
# totalResult.to_csv('C:/files/marketdata/V1V6.csv', sep=',', encoding='utf-8-sig')
print(totalResult)

totalResult.to_excel('./marketdata/' + str(namelist5[0]) + '_Volume.xlsx', sheet_name='Volume data' + str(namelist5[0]))




print('\n', 'количество строк и столбцов:', sep="")
print(totalResult.shape)

print('\n', 'количество строк', sep="")
print(len(totalResult))

print('\n', 'количество значений', '\n', sep="")
print(totalResult.size)



finish_script=time.time()
print('time=', finish_script - start_script)

 

'''

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

# totalResult3[]

print(totalResult3)



finish_script=time.time()

print('time=', finish_script - start_script)








#  запись в файл
#totalResult.to_csv('C:/files/marketdata/V1V6.csv', sep=',', encoding='utf-8-sig')

# запись с дополнением вниз
# ValueRating.to_csv('C:/files/marketdata/V1V6.csv', sep=',', mode='a', encoding='utf-8-sig')




# encoding='utf-8'
# print(df.columns.ravel())
# b = df[1].tolist()
# print(b)

'''
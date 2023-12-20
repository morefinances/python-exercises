import pandas as pd
import random as rnd
from time import sleep

# количество заявок 
N = 1000

ind = 1
inditer = 0

# считываем тикеры
file = "C:\\files\\tickers_for_work.csv"
offers = pd.read_csv(file, delimiter=';')

uniq_offers = []

# удаляем дублирование тикеров
for i in range(len(offers.columns)):
    if "." not in offers.columns[i]:
        uniq_offers.append(offers.columns[i])

# генерация рандомного пула заявок по полученным тикерам
while ind <= N:
    print(f"index = {ind}", end = ' ')
    timeout = rnd.randint(1, 5)
    print(f"timeout = {timeout}")
    numberorders = rnd.randint(1,10)
    print(f"number_orders={numberorders}")
    A = []
    B = []
    C = []
    D = []
    for i in range(numberorders):
        A.append(ind)
        ind += 1
        direction = rnd.randint(1,2)
        if direction == 1:
            B.append("Buy")
        else:
            B.append("Sell")
        C.append(10 * rnd.randint(1,9))
        D.append(rnd.choice(uniq_offers))  
    df=pd.DataFrame({
        'id': A,
        'direct': B,
        'size': C,
        'tiker': D
    })    
    print(df)
    df.to_csv("C:/files/offers.csv", sep=" ", index = False, header = False)
    sleep(timeout/100)
    inditer += 1

print('<-- все заявки отправлены -->')

sleep(timeout/10)
df=pd.DataFrame({})
df.to_csv("C:/files/offers.csv", sep=" ", index = False, header = False)

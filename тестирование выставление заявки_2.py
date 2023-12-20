import pandas as pd
import random as rnd
from time import sleep

ind = 1
inditer = 0

while ind < 200:
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
        D.append(rnd.choice(['SBER', 'GAZP', 'RIZ3', 'SRZ3']))  
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



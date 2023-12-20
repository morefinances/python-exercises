import time

start=time.time()

import random
import matplotlib.pyplot as plt


def myplot(x, y ,a):
        plt.plot(x, y, ls='None', marker='s', ms=3, mfc='b', alpha=a, mew=0)

plt.figure(figsize=(8,8))
plt.rcParams['font.size'] = '8'
#plt.xlabel('x', fontsize=10)
#plt.ylabel('y', fontsize=10)

tx=[[] for i in range(10)]
for u in range(len(tx)):
    tx[u]=[0] * 100
    for i in range(100):
        tx[u][i]=[0] * 100
#yy=[0 for i in range(100)]


xx=[]
yy=[]

#print(tx)




#print(xx[0][0])
print("<-- создание слоя случайных данных -->")

totalpoint=0

while totalpoint<100:
    
    random.seed()
    a = random.randint(0, 99)
    b = random.randint(0, 99)
   
    if a not in xx and not b in yy:
        totalpoint += 1
        xx.append(a)
        yy.append(b)
        
        #print (a, b)



for m in range(len(xx)):
    
    tx[0][xx[m]][yy[m]] = 0.9
    
#     if xx[m]>1:
#         tx[xx[m]-1][yy[m]] = int(10 * (tx[xx[m]-1][yy[m]] + tx[xx[m]-2][yy[m]] + tx[xx[m]][yy[m]]) / 2) / 10
#         #print(tx[xx[m]-1][yy[m]])
#     if xx[m]==1:    
#         tx[xx[m]-1][yy[m]] = int(10 * (tx[xx[m]-1][yy[m]] + tx[xx[m]][yy[m]]) / 2) / 10
#     if xx[m]<98: 
#         tx[xx[m]+1][yy[m]] = int(10 * (tx[xx[m]+1][yy[m]] + tx[xx[m]+2][yy[m]] + tx[xx[m]][yy[m]]) / 2) / 10
#     if xx[m]==98: 
#         tx[xx[m]+1][yy[m]] = int(10 * (tx[xx[m]+1][yy[m]] + tx[xx[m]][yy[m]]) / 2) / 10
#     if yy[m]>1:
#         tx[xx[m]][yy[m]-1] = int(10 * (tx[xx[m]][yy[m]-1] + tx[xx[m]][yy[m]-2] + tx[xx[m]][yy[m]]) / 2) / 10
    
    
    #print(xx[m],yy[m])


#отрисовка массива
for x in range(100):
    for y in range(100):
        myplot(x,y,tx[0][x][y])

plt.show()


for ty in range(1,10):
    plt.figure(figsize=(8,8))
    print(f"<-- создание {ty}-го слоя сглаживания -->")
    #первый слой
    for x in range(100):
        for y in range(100):
            #AA
            if x==0 and y==0:
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                    tx[ty-1][x+1][y] +
                    tx[ty-1][x][y+1] +
                    tx[ty-1][x+1][y+1])/4
                    )               
            # #AC
            if x==99 and y==0:
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                      tx[ty-1][x-1][y] + 
                      tx[ty-1][x-1][y+1] +
                      tx[ty-1][x][y+1])/4
                    )
            #CA
            if x==0 and y==99:
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                     tx[ty-1][x][y-1] +
                     tx[ty-1][x+1][y] +
                     tx[ty-1][x+1][y-1])/4
                    )
            #CC
            if x==99 and y==99:
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                    tx[ty-1][x-1][y] +
                    tx[ty-1][x][y-1] +
                    tx[ty-1][x-1][y-1])/4
                    )           
            #центральная
            if 0<x<99 and 0<y<99: 
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                    tx[ty-1][x-1][y-1] +
                    tx[ty-1][x][y-1] +
                    tx[ty-1][x+1][y-1] +
                    tx[ty-1][x-1][y] +
                    tx[ty-1][x+1][y] +
                    tx[ty-1][x-1][y+1] +
                    tx[ty-1][x][y+1] +
                    tx[ty-1][x+1][y+1])/9
                    )
            #ось 1
            if x==0 and 0<y<99:
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                    tx[ty-1][x][y-1] +
                    tx[ty-1][x+1][y-1] +
                    tx[ty-1][x+1][y] +
                    tx[ty-1][x][y+1] +
                    tx[ty-1][x+1][y+1])/6
                    )
            #ось 2
            if x==99 and 0<y<99:
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                    tx[ty-1][x-1][y-1] +
                    tx[ty-1][x][y-1] +
                    tx[ty-1][x-1][y] +
                    tx[ty-1][x-1][y+1] +
                    tx[ty-1][x][y+1])/6
                    )    
            #ось 3
            if 0<x<99 and y==0:
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                    tx[ty-1][x-1][y] +
                    tx[ty-1][x+1][y] +
                    tx[ty-1][x-1][y+1] +
                    tx[ty-1][x][y+1] +
                    tx[ty-1][x+1][y+1])/6
                    )   
            #ось 4
            if 0<x<99 and y==99:
                tx[ty][x][y] = ( 
                    (tx[ty-1][x][y] +
                    tx[ty-1][x-1][y-1] +
                    tx[ty-1][x][y-1] +
                    tx[ty-1][x+1][y-1] +
                    tx[ty-1][x-1][y] +
                    tx[ty-1][x+1][y])/6
                    )
            myplot(x,y,tx[ty][x][y])
    plt.show()

finish=time.time()
print("Время выполнения :", finish-start)   


     
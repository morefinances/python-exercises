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

tx=[[],[]]
for u in range(2):
    tx[u]=[0] * 100
    for i in range(100):
        tx[u][i]=[0] * 100
#yy=[0 for i in range(100)]


xx=[]
yy=[]




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


plt.figure(figsize=(8,8))

print("<-- создание первого слоя сглаживания -->")
#первый слой
for x in range(100):
    for y in range(100):
        #AA
        if x==0 and y==0:
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                tx[0][x+1][y] +
                tx[0][x][y+1] +
                tx[0][x+1][y+1])/4
                )               
        # #AC
        if x==99 and y==0:
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                  tx[0][x-1][y] + 
                  tx[0][x-1][y+1] +
                  tx[0][x][y+1])/4
                )
        #CA
        if x==0 and y==99:
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                 tx[0][x][y-1] +
                 tx[0][x+1][y] +
                 tx[0][x+1][y-1])/4
                )
        #CC
        if x==99 and y==99:
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                tx[0][x-1][y] +
                tx[0][x][y-1] +
                tx[0][x-1][y-1])/4
                )           
        #центральная
        if 0<x<99 and 0<y<99: 
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                tx[0][x-1][y-1] +
                tx[0][x][y-1] +
                tx[0][x+1][y-1] +
                tx[0][x-1][y] +
                tx[0][x+1][y] +
                tx[0][x-1][y+1] +
                tx[0][x][y+1] +
                tx[0][x+1][y+1])/9
                )
        #ось 1
        if x==0 and 0<y<99:
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                tx[0][x][y-1] +
                tx[0][x+1][y-1] +
                tx[0][x+1][y] +
                tx[0][x][y+1] +
                tx[0][x+1][y+1])/6
                )
        #ось 2
        if x==99 and 0<y<99:
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                tx[0][x-1][y-1] +
                tx[0][x][y-1] +
                tx[0][x-1][y] +
                tx[0][x-1][y+1] +
                tx[0][x][y+1])/6
                )    
        #ось 3
        if 0<x<99 and y==0:
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                tx[0][x-1][y] +
                tx[0][x+1][y] +
                tx[0][x-1][y+1] +
                tx[0][x][y+1] +
                tx[0][x+1][y+1])/6
                )   
        #ось 4
        if 0<x<99 and y==99:
            tx[1][x][y] = ( 
                (tx[0][x][y] +
                tx[0][x-1][y-1] +
                tx[0][x][y-1] +
                tx[0][x+1][y-1] +
                tx[0][x-1][y] +
                tx[0][x+1][y])/6
                )
        myplot(x,y,tx[1][x][y])


plt.show()

finish=time.time()
print("Время выполнения :", finish-start)   


    
 

'''         

   
    if xx[a][b] == 0:
        xx[a][b] = 0.9


for x in range(100):
    for y in range(100):
        if xx[x][y]>0:
            if (x-2)>0:
                xx[x-1][y]=int(5*(xx[x-2][y]+xx[x][y]))/10
                print(xx[x-1][y])
            else:
                if (x-1)>0:
                    xx[x-1][y]=int(5*(xx[x][y]))/10


for x in range(100):
    for y in range(100):
        myplot(x,y,xx[x][y])
        

plt.show()
    
finish=time.time()
print("Время выполнения :", finish-start)



yy=[i for i in range(100)]

for i in range(10000):
    random.seed()
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    
    if xx
    

for x in range(100):
    for y in range(100):
    #plt.plot(a, m, ls='None', marker='s', ms=3, mfc='b', alpha=0.1, mew=0)
    #plt.scatter(xx, yy, s=8, marker="s", linewidth=0, c="b", alpha=0.2)
    
plt.show()
    
finish=time.time()
print("Время выполнения :", finish-start)
'''
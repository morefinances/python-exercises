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

tx=[0] * 100
for i in range(100):
    tx[i]=[0] * 100
#yy=[0 for i in range(100)]

xx=[]
yy=[]


#print(xx[0][0])


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
    
    tx[xx[m]][yy[m]] = 0.9
    
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
        myplot(x,y,tx[x][y])

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
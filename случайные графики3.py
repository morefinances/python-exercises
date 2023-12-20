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

xx=[0] * 100
for i in range(100):
    xx[i]=[0] * 100
#yy=[0 for i in range(100)]


print(xx[0][0])


for i in range(10000):
    random.seed()
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    
     
    
    if xx[a][b]>0:
        xx[a][b] += 0.1
    else:
        xx[a][b] = 0.1


for x in range(100):
    for y in range(100):
        myplot(x,y,xx[x][y])
        

plt.show()
    
finish=time.time()
print("Время выполнения :", finish-start)


'''
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
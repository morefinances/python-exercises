import random
import matplotlib.pyplot as plt
import time


start=time.time()

c=0
xx=[i for i in range(100)]
yy=[i for i in range(100)]

for i in range(10000):
    random.seed()
    a = random.randint(0, 100)
    m = random.randint(0, 100)
    #c = m + a
    '''
    if c < 0: 
        c = 0 - c
    if c > 100:
        c = c%100
    '''
    if a in xx: xx.remove(a)
    if m in yy: yy.remove(m)
    #print(c)
        
    #xx.append(a)
    #yy.append(c)
    plt.plot(a, m, ls='None', marker='s', ms=3, mfc='b', alpha=0.1, mew=0)
    #plt.scatter(xx, yy, s=8, marker="s", linewidth=0, c="b", alpha=0.2)

print("X:", *xx)    
print("Y:", *yy)


#plt.plot(xx, yy, '', marker='s', markerfacecolor='b')
plt.show()
    
finish=time.time()
print("Время выполнения :", finish-start)
import random
import matplotlib.pyplot as plt
import time


start=time.time()

plt.figure(figsize=(8,8))
plt.rcParams['font.size'] = '8'

xx=[i for i in range(100)]
yy=[i for i in range(100)]

for i in range(10000):
    random.seed()
    a = random.randint(0, 100)
    m = random.randint(0, 100)
    
    
    plt.plot(a, m, ls='None', marker='s', ms=2, mfc='b', alpha=0.1, mew=0)
    #plt.scatter(xx, yy, s=8, marker="s", linewidth=0, c="b", alpha=0.2)
    
plt.show()
    
finish=time.time()
print("Время выполнения :", finish-start)
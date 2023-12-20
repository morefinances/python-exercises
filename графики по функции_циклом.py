import matplotlib.pyplot as plt
import time
import math


start=time.time()

plt.figure(figsize=(5,5))


for i in range(1000):
    
    m = (1000**2-i**2)**0.5#2 * i  +  100*math.sin(2*i*3.141592657/180)
  
    plt.plot(i, m, ls='None', marker='s', ms=2, mfc='b', alpha=0.5, mew=0)
    #plt.scatter(xx, yy, s=8, marker="s", linewidth=0, c="b", alpha=0.5)

plt.show()
    
finish=time.time()
print("Время выполнения :", finish-start)

plt.ioff()
plt.close()
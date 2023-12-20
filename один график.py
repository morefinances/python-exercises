import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100,50)
y1=45*x

y2=[i**2 for i in x]

plt.title("вывод y1 и y2")
plt.xlabel("ось х")
plt.ylabel('ось игрек')
plt.grid()
plt.plot(x, y1, x, y2)

plt.show()
 

import matplotlib.pyplot as plt
import math

plt.figure(figsize=(8,8))
plt.rcParams['font.size'] = '8'
plt.xlabel('', fontsize=10)
plt.ylabel('', fontsize=10)

R = 35
r = 15
h = 3
m = r / R

N = 2520 # 360 * R / r * i

xx = [
      R * (1 - m) * math.cos(m * i * math.pi / 180) + h * math.cos((1 - m) * i * math.pi / 180)
      for i in range(N)
]

yy = [
      R * (1 - m) * math.sin(m * i * math.pi / 180) - h * math.sin((1 - m) * i * math.pi / 180) 
      for i in range(N)
]
# yy2 = [-(50**2-y**2)**0.5 for y in xx]
#print(xx)

plt.plot(xx, yy, ls='None', marker='o', ms=3, mfc='b', alpha=0.1, mew=0)
# plt.plot(xx, yy2, ls='None', marker='o', ms=3, mfc='b', alpha=0.5, mew=0)

plt.show()
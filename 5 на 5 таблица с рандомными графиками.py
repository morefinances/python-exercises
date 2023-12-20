import matplotlib.pyplot as plt
import numpy as np
import random

a = 0
b = 0

figure, axis = plt.subplots(5, 5)

for ii in range(25):

    rowLCy = []
    rowLCx = []
    rowLCi = 0


    random.seed()
    x=random.randint(2,1000)


    while x != 1:
        if x % 2 == 0:
            x = x / 2
            rowLCy.append(int(x))
            rowLCi += 1
            rowLCx.append(int(rowLCi))
        else:
            x = 3 * x + 1
            rowLCy.append(int(x))
            rowLCi += 1
            rowLCx.append(int(rowLCi))

    axis[a, b].plot(rowLCx, rowLCy)
    axis[a, b].set_title(ii)

    b += 1

    if b >= 5:
        b = 0
        a += 1

    if a >= 5:
        a = 0


# Get the angles from 0 to 2 pie (360 degree) in narray object
#X = np.arange(0, math.pi * 2, 0.05)

# Using built-in trigonometric function we can directly plot
# the given cosine wave for the given angles


# Initialise the subplot function using number of rows and columns


# Combine all the operations and display
plt.show()
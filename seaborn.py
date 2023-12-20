import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random as rnd

x = [i for i in range(10)]
y = [i for i in range(10, 20)]
print(y)



aa = [i for i in range(100)]

rnd.seed()

d = {'a': [ 100 * rnd.random() for i in aa],
     'b': [ 100 * rnd.random() for i in aa]}

df = pd.DataFrame(d)

print(df)

plt.relplot(data=df, x='a', y='b')

plt.show()
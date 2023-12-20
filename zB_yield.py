

# list_of_number = [1, 10, 110]
# print(str(list_of_number))

import pandas as pd

s = pd.Series([10, 20, 30, 40, 50], ['a', 'b', 'c', 'd', 'e'])
print(s['a':'c'])
print(s[1])
print(s.iloc[1])
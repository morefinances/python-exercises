import pandas as pd

df=pd.DataFrame({
    'A': ['text1', 'text2', 'text3'],
    'B': [28, 2, 15],
    'C': [228,28,155]
})

print(df)

ind = 0

while ind < 100:
    print(ind)
    ind += 1


# df.to_csv("C:/files/4one.csv", sep=" ", index = False, header = False)
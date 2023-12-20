import pandas as pd

df=pd.DataFrame({
    'A': ['text1', 'text2', 'text3'],
    'B': [28, 2, 15],
    'C': [228,28,155]
})

print(df)

df.to_json("C:/files/2one.json")
import json
import pandas as pd

# d = {
#  'fruit':{"Grapes": "10","color": "green"},
#  'vegetable':{"chilli": "4","color": "red"},
# }

d = {i: i**2 for i in range(10)}
#print(list(d.keys())[1])  # ['a', 'b']



e=json.dumps(d, indent=2)
le=json.loads(e)

df=pd.read_json(e, orient="index")

df.columns = ['no txt']

print(d)
print(e)
print(df)
print(df.columns)

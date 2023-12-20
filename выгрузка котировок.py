
import requests
import json
import pandas as pd

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

dictdata=json.dumps(data, sort_keys=True, indent=4)
dictdata2=json.loads(dictdata)

 
print(dictdata2)
dataset=dictdata2['Time Series (5min)']
print(pd.DataFrame(dataset.values()))
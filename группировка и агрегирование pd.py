import pandas as pd

titanic_df = pd.read_csv('C:/files/titanic.csv')
print(titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())
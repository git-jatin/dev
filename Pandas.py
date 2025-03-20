import pandas as pd
import matplotlib.pyplotlot
data=pd.read_csv('/Users/jatinrai/Downloads/matches - matches.csv')
print(data.describe())
print(data["winner"])
print(data['winner'].value_counts().plot(kind='bar'))
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('big-mac-historical-source-data.csv')

usa_data = data[data['name'] == 'United States']
print(usa_data.head())

data['year'] = pd.to_datetime(data['date']).dt.year

annual_data = data.groupby('year').agg({'local_price': 'median', 'dollar_ex': 'mean'}).reset_index()  # Group data by year and calculate mean

x = annual_data[['dollar_ex']]
y = annual_data[['local_price']]

srcemodel = LinearRegression()
srcemodel.fit(x,y)

plt.scatter(x,y, color = 'orange')
plt.plot(x, srcemodel.predict(x), color = 'pink')
plt.title('Big Mac Prices vs Exchange Rate')
plt.xlabel('Exchange rate to USD')
plt.ylabel('Big Mac Prices')
plt.show()

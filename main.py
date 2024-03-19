import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

import numpy as np

df = pd.read_csv('books_data (1).csv', index_col=0)

#filter out non english publications
# Filter for English books

# Define a function to extract the first year from a range
df['Language'] = df['Language'].fillna("Unknown")  # Handle any NaN values in 'Language' column
english_books_df = df[df['Language'] == 'English']
english_books_df.loc[:,'First_Published'] = english_books_df['First_Published'].apply(lambda x: x.split('–')[0].strip())
english_books_df.loc[:,'First_Published'] = pd.to_numeric(english_books_df['First_Published'], errors='coerce')

# Check for NaN values and remove them
print(english_books_df.isnull().sum())
english_books_df = english_books_df.dropna(subset=['First_Published', 'Sales_in_millions'])

# Split the data into training and testing sets
X = english_books_df[['First_Published']]
y = english_books_df['Sales_in_millions']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting the test set results
y_pred = model.predict(X_test)

# Calculating Mean Squared Error and R2 Score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Squared Error:', mse)
print('R2 Score:', r2)


plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Sales')
line_values = model.coef_ * X_test + model.intercept_
plt.plot(X_test, line_values, color='red', label='Predicted Sales')
plt.title('Linear Regression: Sales in Millions vs. First Published Year')
plt.xlabel('First Published Year')
plt.ylabel('Sales in Millions')
plt.legend()
plt.show()

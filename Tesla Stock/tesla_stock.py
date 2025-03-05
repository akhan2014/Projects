'''

Title: Tesla Stock Price Analysis (2015 - 2024)

Objective: Analyze Tesla's stock price trends, votility, and KPIs over time to uncover insights for investors and enthusiasts.

Goal: Understand how Tesla's stock price has evolved from 2015 to 2024, identify major trends and calculate basic metrics like returns and volitility

Deliverables: 
    1. summary of key statistics(high/low prices, average returns)
    2. Visualizations (price trends, moving averages, volatility)
    3. Insights ( periods of high growth or significant drops)

Tools: Python (Pandas for data manipulation, Matplotlib/seaborn for visualization)
'''

import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv("/Users/alex/Desktop/Projects/Tesla Stock/tesla_stock.csv")

# convert 'date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# select relevant columns
df = df[['Date', 'Adj Close', 'Volume']]

# check for total number of missing values
# print(df.isnull().sum())

# sort by date
df = df.sort_values('Date')


### EDA (Exploratory Data Analysis) ###

# basic stats
# print(df['Adj Close'].describe())

# highest and lowest prices
max_price = df['Adj Close'].max()
min_price = df['Adj Close'].min()
max_date = df[df['Adj Close'] == max_price]['Date'].iloc[0]
min_date = df[df['Adj Close'] == min_price]['Date'].iloc[0]

# print(f"Highest Price: {max_price} on {max_date}")
# print(f"Lowest Price: {min_price} on {min_date}")

# Calculate Daily Returns
# Daily return = (Adj Close today - Adj Close Yesterday) / Adj Close Yesterday

df['Daily Return'] = df['Adj Close'].pct_change() * 100
# print(df[['Date', 'Adj Close', 'Daily Return']].head())

'''
         Date   Adj Close  Volume  Daily Return
0  2015-01-12  13.480667  89254500          NaN
1  2015-01-13  13.616667  67159500    0.010093  ## (13.616667 - 13.480667) / 13.480667 ≈ 0.0101
2  2015-01-14  12.846000  173278500  -0.056592  ## (12.846000 - 13.616667) / 13.616667 ≈ -0.0566
3  2015-01-15  12.791333  78247500   -0.004279  ## (12.791333 - 12.846000) / 12.846000 ≈ -0.0043
4  2015-01-16  12.871333  54048000    0.006268  ## (12.871333 - 12.791333) / 12.791333 ≈ 0.0063
'''

### Visualize the Data ###

#1. Stock Price Trend

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Adj Close'], label='Adjusted Close')
plt.title('Tesla Stock Price (2015-2024)')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid()
# plt.show()

#Tesla saw a signifigant raise in stock price from 2020 to 2021 and again from 21 to 22. 

#2. Moving Average (moving average can help smooth out short term volitility)

df['50-Day MA'] = df['Adj Close'].rolling(window=50).mean()

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Adj Close'], label='Adjusted Close')
plt.plot(df['Date'], df['50-Day MA'], label='50-Day Moving Average', color='orange')
plt.title('Tesla Stock Price with 50-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid()
# plt.show()

#3. Daily Returns Histogram

plt.figure(figsize=(12,6))
plt.hist(df['Daily Return'].dropna(), bins=50, color='purple', alpha=0.7)
plt.title('Distribution of Tesla Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.grid()
# plt.show()

# 4. Volume vs Price

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Volume'], label='Volume', color='green')
plt.title('Tesla Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid()
plt.show()
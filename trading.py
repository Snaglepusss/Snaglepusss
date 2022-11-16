#Importing the modules...

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

#Creating the Array "test_ticker"...

test_ticker=["SNDL","O","LAC"]

#Createing "test_stocks" Varibale and assign it a value downloaded using yf between dates spefecied...

test_stocks = yf.download(test_ticker, start = "2020-01-01",end ="2022-10-31")

# Creating the Variable close to hold the closing price data for each stock...

close=test_stocks.loc[:,"close"].copy()

# creating the varibale normclose which will hold the smoothed out aka make sit look nicer... 
# We will then use nthe normclose varibale to create a better looking graph

normclose=close.div(close.iloc[0]).mul(100)

# Actually creating the graph

normclose.plot(figsize=(12,8),fontsize=12)
plt.legend(fontsize=12)
plt.show()



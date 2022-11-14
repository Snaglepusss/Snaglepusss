#Importing the modules...

import yfinance as yf
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#Creating the Array "test_ticker"...

test_ticker=["SNDL","O","LAC"]

#Createing "test_stocks" Varibale and assign it a value downloaded using yf between dates spefecied...

test_stocks = yf.download(test_ticker, start = "2020-01-01",end ="2022-10-31")
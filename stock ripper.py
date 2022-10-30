import yfinance as yf
import pandas as pd


## Ticker module to import objects that extarct data

# create object from import
apple = yf.Ticker("AAPL")

apple_info = apple;.info
apple_info

import yfinance as yf
import pandas as pd


## Ticker module to import objects that extarct data

# create object from import
apple = yf.Ticker("AAPL")
print(apple)
apple.dividends
apple.dvidints.plot()



# get stock information
apple.info
apple_info = apple.info
apple_info = apple.info
print(apple.info)

apple_info['country'] # to retreive a specefic part from apple.info
apple.dividends.plot()

## to download data from multiple stock tickers
## .use .download method for threading - makes it faster
data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

# get historical Data
## history paramaters - period, interval, start, end, prepost, autoadjust, actions
apple.history(period = "max")
apple_history = apple.history

print(apple_history)

# show actions / divident splits:A
apple.actions
print(apple.actions)

# show dividends
apple.dividends
print (apple.divideds)
apple.dividints.plot()


# show splits
apple.splits
print(apple.splits)

import streamlit as st
import datetime as dt
import pandas as pd
from datetime import timedelta, time
import yfinance as yf
import PIL; from PIL import Image
import pandas_datareader as web
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


image = Image.open('wsb.png')
st.image(image, use_column_width=True)
st.write('''
    # Simple webapp to display *opening* and **closing** of stock prices.
    ***  ''')

#get user input for stocks

#
# ## display dataframe:
# stock_info = {}
# st.subheader('Stock Information [DATA FRAME]')
# df = pd.DataFrame.from_dict(stock_info)
# df.reset_index(inPlace=True)
# st.write(df)
# st.write(''' *** ''')
#
# ## display barchart
# st.subheader('Bar Chart')
# b_chart = alt.Chart(df).mark_bar().encode(x = 'Volume', y = 'Date')
# p = pd.properties(width=alt.step(80))
# st.write(p)
# #braker line
# st.write('''***''')

def additional_data(tickerSymbol):
    st.subheader(' [5-DAY] Stock Information [DATA FRAME]')
    start = dt.datetime.now() - dt.timedelta(days=365)
    end = dt.datetime.now()

    df = web.DataReader(tickerSymbol, f'yahoo', start, end)
    print(df.head())
    st.write(df.head())

    df.to_csv(f"{tickerSymbol} + {dt.date.today()}.csv")  # Write df Object to .CSV
    df['Pct Change'] = df['Adj Close'].pct_change()
    df['stock_return'] = (df['Pct Change'] + 1).cumprod()
    #df = df[['Open', 'High', 'Low', 'Close']]
    #df['Date'] = df['Date'].map(mdates.date2num)
    df.reset_index(inplace=True)

    st.subheader(' [5-DAY] Stock Information with PCT change and Return.')
    st.write(df.head())
    print(df.head())

def graph_display(tickerSymbol):
    ''' Takes User Input and displays graphs, accordingly '''

    # fetch data from ticker passed from main()
    # set tickerData OBJ and retrieve data in tickerDf

    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

    st.subheader(f'{tickerSymbol} [Stock Information] ')
    print(tickerDf.head())
    st.write(tickerDf.head())

    ## Graphs
    st.subheader(f'{tickerSymbol} [Stock Information -- 5-Year] ')
    st.line_chart(tickerDf)

    st.subheader(f'{tickerSymbol} [Stock Information -- 2 -Year] ')
    st.line_chart(tickerDf.head(2))

    st.header(f'{tickerSymbol} [Volume]')
    st.line_chart(tickerDf.Volume)

    st.header(f'{tickerSymbol} [Opening Prices]')
    st.line_chart(tickerDf.Open)

    st.header(f'{tickerSymbol} [Closing Prices]')
    st.line_chart(tickerDf.Close)

    st.header(f'{tickerSymbol} [Trading Volume]')
    st.line_chart(tickerDf.Volume)

    stock_input = ">STOCK INPUT \n "
    stock = st.text_area('Text Area', stock_input, height=25)
    stock = stock.splitlines()
    stock = stock[1:]  # isolate the the 2nd line to retrieve user input
    st.write(''' *** ''')

    ## function recursion IF frontend recieves new stock symbol, reload page with new info
    if st.write():
        graph_display(tickerSymbol)
        additional_data(tickerSymbol)


def main():
    ticker = input('Enter The Stock Symbol, ex: GOOG: ')
    graph_display(ticker)
    additional_data(ticker)

main()

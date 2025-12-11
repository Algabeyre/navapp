import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         # Simple Stock Price App
         Shown are the stock closing price and volume of Google!
         """)
# https://towardsdatascience.com/build-a-stock-price-app-using-streamlit-and-yahoo-finance-api-3ec9122c9624
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
ticketData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
ticketDf = ticketData.history(start='2010-05-31', end='2020-05-31')  # Only start and end dates
# open    high	low	close	volume	dividends	stock splits
st.write("""
         ## Closing Price
            """)
st.line_chart(ticketDf.Close)
st.write("""
         ## Volume Price
            """)
st.line_chart(ticketDf.Volume)
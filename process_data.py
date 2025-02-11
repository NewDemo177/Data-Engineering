import pandas as pd
import numpy as np

def process_data(stock):
    if 'Adj Close' in stock.columns:
        stock['Daily Return'] = stock['Adj Close'].pct_change()
        stock['50-day MA'] = stock['Adj Close'].rolling(window=50).mean()
        stock['200-day MA'] = stock['Adj Close'].rolling(window=200).mean()
    elif 'Close' in stock.columns:
        stock['Daily Return'] = stock['Close'].pct_change()
        stock['50-day MA'] = stock['Close'].rolling(window=50).mean()
        stock['200-day MA'] = stock['Close'].rolling(window=200).mean()
    else:
        print("Error: Neither 'Adj Close' nor 'Close' found in stock data")
        return None
    
    return stock

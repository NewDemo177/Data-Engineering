import yfinance as yf
def fetch_stock_data(ticker, start, end):
    return yf.download(ticker, start=start, end=end)

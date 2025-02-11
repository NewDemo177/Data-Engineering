import matplotlib.pyplot as plt

def plot_stock(stock, ticker):
    plt.figure(figsize=(12,6))
    
    # Check if 'Adj Close' or 'Close' exists before plotting
    if 'Adj Close' in stock.columns:
        plt.plot(stock.index, stock['Adj Close'], label="Stock Price", color='blue')
    elif 'Close' in stock.columns:
        plt.plot(stock.index, stock['Close'], label="Stock Price", color='blue')
    else:
        print("Error: Neither 'Adj Close' nor 'Close' found in stock data")
        return  # Exit function if no valid price column exists

    # Check for moving averages before plotting
    if '50-day MA' in stock.columns:
        plt.plot(stock.index, stock['50-day MA'], label="50-day MA", color='red', linestyle='dashed')
    if '200-day MA' in stock.columns:
        plt.plot(stock.index, stock['200-day MA'], label="200-day MA", color='green', linestyle='dashed')

    plt.title(f"{ticker} Stock Price Analysis")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.grid()
    plt.show()

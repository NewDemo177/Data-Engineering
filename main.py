from fetch_data import fetch_stock_data
from process_data import process_data
from visualize import plot_stock

if __name__ == "__main__":
    stock_data = fetch_stock_data("TSLA", "2023-01-01", "2024-01-01")
    processed_stock = process_data(stock_data)
    plot_stock(processed_stock, "TSLA")

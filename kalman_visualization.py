from kalman_filter import kalman_filter
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    if start_date >= end_date:
        raise ValueError("Start date must be before end date.")
    stock_data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
    if stock_data.empty:
        raise ValueError(f"No data found for ticker {ticker} between {start_date} and {end_date}.")
    return stock_data[['Close']]

def visualize_kalman(ticker, start_date, end_date):
    stock_data = get_stock_data(ticker, start_date, end_date)
    close_prices = np.array(stock_data["Close"].values).flatten()


    F = np.array([[1, 1], [0, 1]])
    H = np.array([[1, 0]])
    Q = np.eye(2) * 0.01
    R = np.eye(1) * 0.1

    filtered_prices = kalman_filter(close_prices, F, H, Q, R)

    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, close_prices, label='Actual Close Price', color='blue')
    plt.plot(stock_data.index, filtered_prices, label='Kalman Filtered Price', color='red')
    plt.title(f'Kalman Filter Visualization for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()
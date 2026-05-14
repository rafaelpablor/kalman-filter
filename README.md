# Kalman Filter for Stock Data

A minimal Python project applying Kalman filters to stock market data for price smoothing and trend estimation.

## Project Structure

* `kalman_filter.py` - Core Kalman filter implementation using NumPy
* `kalman_visualization.py` - Stock data loading and Kalman filter visualization

## Parameters

* **Ticker** - Stock symbol (e.g. AAPL, TSLA, MSFT)
* **Start Date** - Start of the historical data range (YYYY-MM-DD)
* **End Date** - End of the historical data range (YYYY-MM-DD)
* **F** - State transition matrix (defines how the state evolves)
* **H** - Measurement matrix (maps state to observations)
* **Q** - Process noise covariance (model uncertainty)
* **R** - Measurement noise covariance (observation uncertainty)

## Installation

```
pip install numpy matplotlib yfinance
```

## Usage

```
python kalman_visualization.py
```

## How It Works

The Kalman filter estimates the true underlying price of a stock by combining a model prediction with noisy market observations. The state vector tracks both price and trend. At each time step the filter predicts the next state using the transition matrix F, then corrects the prediction based on the new observed price. The balance between trusting the model and trusting the observation is controlled by Q and R.

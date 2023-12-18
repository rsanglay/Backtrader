#Backtrader Momentum Strategy 
This Python script leverages the Backtrader framework to implement a trading strategy based on the Momentum indicator. The financial data is sourced from the Alpha Vantage API.

## Features:

### AlphaVantageData Class:
Custom data feed class tailored for incorporating Alpha Vantage time series data into Backtrader.

### MomentumStrategy Class:
Backtrader strategy class implementing a simple momentum-based trading algorithm.
Buys assets when the Momentum indicator is positive.

### run_backtest Function:
Downloads historical financial data for a specified symbol (e.g., "XAUUSD" for Gold) from Alpha Vantage.
Initializes Backtrader with the custom data feed and the Momentum strategy.
Sets initial capital, commission, and runs the backtest.
Prints starting and ending portfolio values, along with the return percentage.
Visualizes the results using Backtrader's plotting functionality.


### Dependencies:

Backtrader

Pandas

Alpha Vantage Python API

### How to Run:

Execute the script, and the Backtrader framework will simulate the Momentum strategy on the provided financial data. The results, including portfolio values and return percentages, will be displayed in the console. Additionally, a plot of the trading performance will be generated for visual analysis.

Feel free to customize the script or integrate additional features based on your trading preferences or requirements.

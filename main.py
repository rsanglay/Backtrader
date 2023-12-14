import backtrader as bt
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import datetime

ALPHAVANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

class AlphaVantageData(bt.feeds.PandasData):
    params = (
        ('datetime', None),
        ('open', '1. open'),
        ('high', '2. high'),
        ('low', '3. low'),
        ('close', '4. close'),
        ('volume', '5. volume'),
        ('openinterest', -1),
    )

def download_alpha_vantage_data(symbol, api_key, from_date, to_date, timeframe='daily', output_size='full'):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize=output_size)
    data.index = pd.to_datetime(data.index)
    data.sort_index(ascending=True, inplace=True)
    return data.loc[from_date:to_date]  # Filter data between from_date and to_date

class MomentumStrategy(bt.Strategy):
    params = (
        ("momentum_period", 14),
    )

    def __init__(self):
        self.momentum = bt.indicators.Momentum(self.data.close, period=self.params.momentum_period)

    def next(self):
        if self.momentum > 0:
            self.buy()

def run_backtest():
    cerebro = bt.Cerebro()

    # Set end date
    end_date = datetime.datetime(2023, 12, 1)

    # Download data from Alpha Vantage
    symbol = "XAUUSD"  # Gold
    data = download_alpha_vantage_data(symbol, ALPHAVANTAGE_API_KEY,
                                       from_date=datetime.datetime(2019, 1, 1), to_date=end_date,
                                       output_size='compact')  # Use compact to get data for the specified date range
    data_feed = AlphaVantageData(dataname=data, fromdate=datetime.datetime(2019, 1, 1))

    # Add data feed
    cerebro.adddata(data_feed)

    # Add strategy
    cerebro.addstrategy(MomentumStrategy)

    # Set initial capital
    cerebro.broker.set_cash(100000)

    # Set commission
    cerebro.broker.setcommission(commission=0.001)

    print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")

    # Run the strategy
    cerebro.run()

    ending_portfolio_value = cerebro.broker.getvalue()
    print(f"Ending Portfolio Value: {ending_portfolio_value}")

    # Calculate and print the return percentage
    initial_portfolio_value = 100000
    return_percentage = ((ending_portfolio_value - initial_portfolio_value) / initial_portfolio_value) * 100
    print(f"Return Percentage: {return_percentage:.2f}%")

    # Plot the results with improved clarity
    cerebro.plot(style='candlestick', barup='green', bardown='red', volume=False, hlines=[0])
    plt.show()

if __name__ == "__main__":
    run_backtest()

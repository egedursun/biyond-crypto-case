import random as r

import pandas as pd


class NaiveLongShortStrategy:
    """
    Naive long/short strategy. This strategy is used to benchmark the backtesting engine.
    """
    def __init__(self):
        self.name = 'NaiveLongShortStrategy'
        self.description = 'Naive long/short strategy. This strategy is used to benchmark the backtesting engine.'
        self.signals = [
            'long',
            'short',
            'hold',
        ]

    @staticmethod
    def evaluate_symbol(date, symbol, dataframe, window=10):
        # check last 30 days
        # if the price is higher than the price 10 days ago, buy
        # if the price is lower than the price 10 days ago, sell
        # otherwise, hold

        window = int(window)

        signals = {
            0: 'up',
            1: 'down',
            2: 'hold',
        }

        if not date - pd.Timedelta(days=window) in dataframe['Date'].values:
            return signals[2]

        price_today = dataframe[dataframe['Date'] == date]['Close'].values[0]
        price_30_days_ago = dataframe[dataframe['Date'] == date - pd.Timedelta(days=window)]['Close'].values[0]

        if price_today > price_30_days_ago:
            return signals[0]
        elif price_today < price_30_days_ago:
            return signals[1]
        else:
            return signals[2]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe, kwargs['window'])
            signals[symbol] = signal
        return signals

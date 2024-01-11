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
            'up',
            'down',
            'hold',
        ]

    def evaluate_symbol(self, date, symbol, dataframe, window=10):
        window = int(window)
        if not date - pd.Timedelta(days=window) in dataframe['Date'].values:
            return self.signals[2]
        price_today = dataframe[dataframe['Date'] == date]['Close'].values[0]
        price_30_days_ago = dataframe[dataframe['Date'] == date - pd.Timedelta(days=window)]['Close'].values[0]
        if price_today > price_30_days_ago:
            return self.signals[0]
        elif price_today < price_30_days_ago:
            return self.signals[1]
        else:
            return self.signals[2]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe, kwargs['window'])
            signals[symbol] = signal
        return signals

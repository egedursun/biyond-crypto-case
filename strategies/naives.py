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
    def evaluate_symbol(date, symbol, dataframe):
        # check last 10 days
        # if the price is higher than the price 10 days ago, buy
        # if the price is lower than the price 10 days ago, sell
        # otherwise, hold
        price_today = dataframe[dataframe['Date'] == date]['Close'].values[0]
        if len(dataframe[dataframe['Date'] == date - pd.Timedelta(days=10)]) == 0:
            return 'hold'
        else:
            price_10_days_ago = dataframe[dataframe['Date'] == date - pd.Timedelta(days=10)]['Close'].values[0]

        if price_today > price_10_days_ago:
            return 'long'
        elif price_today < price_10_days_ago:
            return 'short'
        else:
            return 'hold'

    def generate_signals(self, date, universe, portfolio):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe)
            signals[symbol] = signal
        return signals

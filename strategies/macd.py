import pandas as pd


class MACDLongShortStrategy:
    """
    Moving Average Convergence Divergence long/short strategy.
    """
    def __init__(self):
        self.name = 'MACDLongShortStrategy'
        self.description = 'Moving Average Convergence Divergence long/short strategy.'
        self.signals = [
            'long',
            'short',
            'hold',
        ]

    @staticmethod
    def evaluate_symbol(date, symbol, dataframe):
        return 'hold'

    def generate_signals(self, date, universe, portfolio):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe)
            signals[symbol] = signal
        return signals

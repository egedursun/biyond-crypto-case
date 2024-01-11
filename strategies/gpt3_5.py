import pandas as pd


class GPT_3_5LongShortStrategy:
    """
    GPT-3.5 long/short strategy.
    """
    def __init__(self):
        self.name = 'GPT3_5LongShortStrategy'
        self.description = 'GPT-3.5 long/short strategy.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]

    def evaluate_symbol(self, date, symbol, dataframe):
        return 'hold'

    def generate_signals(self, date, universe, portfolio):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe)
            signals[symbol] = signal
        return signals

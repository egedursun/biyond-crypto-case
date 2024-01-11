import pandas as pd


class SMALongShortStrategy:
    """
    Simple moving average long/short strategy.
    """
    def __init__(self):
        self.name = 'SMALongShortStrategy'
        self.description = 'Simple moving average long/short strategy.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]

    def evaluate_symbol(self, date, symbol, dataframe, window=10):
        if not date - pd.Timedelta(days=window) in dataframe['Date'].values:
            return self.signals[2]
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]
        last_10_days = dataframe.tail(window)
        sma = last_10_days['Close'].mean()
        last_close = last_10_days['Close'].iloc[-1]
        if last_close > sma:
            return self.signals[0]
        elif last_close < sma:
            return self.signals[1]
        elif last_close == sma:
            return self.signals[2]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe, window=kwargs['window'])
            signals[symbol] = signal
        return signals

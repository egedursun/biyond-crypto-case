import pandas as pd


class BollingerLongShortStrategy:
    """
    Bollinger Bands long/short strategy.
    """
    def __init__(self):
        self.name = 'BoilingerLongShortStrategy'
        self.description = 'Boilinger Bands long/short strategy.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]

    def evaluate_symbol(self, date, symbol, dataframe, window=20, k=2):
        if not date - pd.Timedelta(days=window) in dataframe['Date'].values:
            return self.signals[2]
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]
        last_20_days = dataframe.tail(window)
        sma = last_20_days['Close'].mean()
        std = last_20_days['Close'].std()
        upper_band = sma + k * std
        lower_band = sma - k * std
        last_close = last_20_days['Close'].iloc[-1]
        if last_close > upper_band:
            return self.signals[0]
        elif last_close < lower_band:
            return self.signals[1]
        else:
            return self.signals[2]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe, window=kwargs['window'], k=kwargs['k'])
            signals[symbol] = signal
        return signals

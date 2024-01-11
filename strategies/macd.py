import pandas as pd


class MACDLongShortStrategy:
    """
    Moving Average Convergence Divergence long/short strategy.
    """
    def __init__(self):
        self.name = 'MACDLongShortStrategy'
        self.description = 'Moving Average Convergence Divergence long/short strategy.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]

    def evaluate_symbol(self, date, symbol, dataframe, short_window=12, long_window=26, signal_window=9):
        if not date - pd.Timedelta(days=long_window) in dataframe['Date'].values:
            return self.signals[2]

        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]

        dataframe['EMA_12'] = dataframe['Close'].ewm(span=12, adjust=False).mean()
        dataframe['EMA_26'] = dataframe['Close'].ewm(span=26, adjust=False).mean()
        dataframe['MACD'] = dataframe['EMA_12'] - dataframe['EMA_26']
        dataframe['Signal_Line'] = dataframe['MACD'].ewm(span=9, adjust=False).mean()

        current_macd = dataframe['MACD'].iloc[-1]
        current_signal = dataframe['Signal_Line'].iloc[-1]
        previous_macd = dataframe['MACD'].iloc[-2]
        previous_signal = dataframe['Signal_Line'].iloc[-2]

        if current_macd > current_signal and previous_macd <= previous_signal:
            return "up"
        elif current_macd < current_signal and previous_macd >= previous_signal:
            return "down"
        else:
            return "hold"

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe,
                                          short_window=kwargs['short_window'],
                                          long_window=kwargs['long_window'],
                                          signal_window=kwargs['signal_window'])
            signals[symbol] = signal
        return signals

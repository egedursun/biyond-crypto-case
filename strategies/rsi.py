import pandas as pd


class RSILongShortStrategy:
    """
    Relative Strength Index long/short strategy.
    """
    def __init__(self):
        self.name = 'RSILongShortStrategy'
        self.description = 'Relative Strength Index long/short strategy.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]

    def evaluate_symbol(self, date, symbol, dataframe, window=14, down_threshold=30, up_threshold=70):
        # calculate the RSI for long/short

        # get the last 14 days of data
        window = int(window)

        if not date - pd.Timedelta(days=window) in dataframe['Date'].values:
            return self.signals[2]

        # get the last 14 days of data
        last_14_days = dataframe[dataframe['Date'] >= date - pd.Timedelta(days=window)]

        # calculate the change in price
        changes = last_14_days['Close'].diff()

        # get the positive and negative changes
        positive_change = changes[changes >= 0].sum()
        negative_change = changes[changes < 0].sum()

        # calculate the average gain and loss
        average_gain = positive_change / window
        average_loss = negative_change / window

        # calculate the relative strength
        relative_strength = average_gain / average_loss if average_loss != 0 else 0

        # calculate the relative strength index
        relative_strength_index = 100.0 - (100.0 / (1.0 + relative_strength) if (1.0 + relative_strength) != 0 else 0)

        if relative_strength_index > up_threshold:
            return self.signals[0]
        elif relative_strength_index < down_threshold:
            return self.signals[1]
        else:
            return self.signals[2]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe,
                                          kwargs['window'], kwargs['down_threshold'], kwargs['up_threshold'])
            signals[symbol] = signal
        return signals

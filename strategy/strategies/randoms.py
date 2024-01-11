import random as r


class RandomLongShortStrategy:
    """
    Random long/short strategy. This strategy is used to test the backtesting engine.
    """
    def __init__(self):
        self.name = 'RandomLongShortStrategy'
        self.description = 'Random long/short strategy. This strategy is used to test the backtesting engine.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, _ in universe.items():
            signal = r.choice(self.signals)
            signals[symbol] = signal
        return signals

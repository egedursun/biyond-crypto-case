import random as r


class RandomLongShortStrategy:
    """
    Random long/short strategy. This strategy is used to test the backtesting engine.
    """
    def __init__(self):
        self.name = 'RandomLongShortStrategy'
        self.description = 'Random long/short strategy. This strategy is used to test the backtesting engine.'
        self.signals = [
            'long',
            'short',
            'hold',
        ]

    def generate_signals(self, date, universe, portfolio):
        signals = {}
        # print(f"Who cares about the {portfolio.positions}? YOLO!")
        for symbol, _ in universe.items():
            signal = r.choice(self.signals)
            # print(f'[{self.name}] Generating signals for {symbol}:  {signal}')
            signals[symbol] = signal
        return signals

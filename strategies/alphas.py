
class AlphaStrategy:
    """
    Alpha strategy base class.
    """
    def __init__(self):
        self.name = 'AlphaStrategy'
        self.description = 'Alpha strategy base class.'
        self.signals = [
            'long',
            'short',
            'hold',
        ]

    @staticmethod
    def evaluate_symbol_001(date, symbol, dataframe):
        return 'hold'

    @staticmethod
    def evaluate_symbol_002(date, symbol, dataframe):
        return 'hold'

    @staticmethod
    def evaluate_symbol_003(date, symbol, dataframe):
        return 'hold'

    @staticmethod
    def evaluate_symbol_004(date, symbol, dataframe):
        return 'hold'

    @staticmethod
    def evaluate_symbol_005(date, symbol, dataframe):
        return 'hold'

    def generate_signals(self, date, universe, portfolio, *command):
        signals = {}
        for symbol, dataframe in universe.items():
            for cmd in command:
                if cmd == '001':
                    signal = self.evaluate_symbol_001(date, symbol, dataframe)
                elif cmd == '002':
                    signal = self.evaluate_symbol_002(date, symbol, dataframe)
                elif cmd == '003':
                    signal = self.evaluate_symbol_003(date, symbol, dataframe)
                elif cmd == '004':
                    signal = self.evaluate_symbol_004(date, symbol, dataframe)
                elif cmd == '005':
                    signal = self.evaluate_symbol_005(date, symbol, dataframe)
                else:
                    signal = self.evaluate_symbol_001(date, symbol, dataframe)
                signals[symbol] = signal
        return signals

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class ForestLongShortStrategy:
    """
    Forest long/short strategy.
    """
    def __init__(self):
        self.name = 'ForestLongShortStrategy'
        self.description = 'Forest long/short strategy.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]
        self.classifier = None

    def evaluate_symbol(self, date, symbol, dataframe, training_data_limit=20, n_estimators=10):
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]

        if len(dataframe) < training_data_limit:
            return self.signals[2]

        elif len(dataframe) == training_data_limit:
            clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
            X = dataframe[['Open', 'High', 'Low', 'Close', 'Volume']][:-1]
            X_shifted = X.shift(1)
            X_shifted.fillna(0, inplace=True)
            y = X['Close'] > X_shifted['Close']
            self.classifier = clf.fit(X, y)

        # predict the price for the next day
        last_row = dataframe.tail(1)
        X_pred = last_row[['Open', 'High', 'Low', 'Close', 'Volume']]
        y_pred = self.classifier.predict(X_pred)

        # return the signal
        if y_pred[0]:
            return self.signals[1]
        else:
            return self.signals[0]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe,
                                          training_data_limit=kwargs['training_data_limit'],
                                          n_estimators=kwargs['n_estimators'])
            signals[symbol] = signal
        return signals

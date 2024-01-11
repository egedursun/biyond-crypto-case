from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import pandas as pd
import numpy as np


class DeepLongShortStrategy:
    """
    Deep Long/Short strategy.
    """
    def __init__(self):
        self.name = 'DeepLongShortStrategy'
        self.description = 'Deep Long/Short strategy.'
        self.signals = [
            'down',
            'up',
            'hold',
        ]
        self.model = Sequential([
            Dense(64, input_dim=5, activation='relu'),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])

    def evaluate_symbol(self, date, symbol, dataframe, training_data_limit=10, learning_rate=0.001, epochs=3):
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]
        if not date - pd.Timedelta(days=training_data_limit) in dataframe['Date'].values:
            return self.signals[2]
        X = dataframe[['Open', 'High', 'Low', 'Close', 'Volume']][:-1]
        X_shifted = X.shift(1).fillna(0)
        y = X['Close'] > X_shifted['Close']
        if len(dataframe) < training_data_limit:
            self.model.compile(optimizer=Adam(learning_rate=learning_rate), loss='binary_crossentropy',
                               metrics=['accuracy'])
            self.model.fit(X, y, epochs=epochs, verbose=0)

            return self.signals[2]
        last_row = dataframe.tail(1)
        X_pred = last_row[['Open', 'High', 'Low', 'Close', 'Volume']]
        y_pred = self.model.predict(X_pred, verbose=0) > 0.5
        return self.signals[1] if y_pred[0][0] else self.signals[0]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe,
                                          learning_rate=kwargs['learning_rate'], epochs=kwargs['epochs'])
            signals[symbol] = signal
        return signals

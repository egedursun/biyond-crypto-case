import numpy as np
import pandas as pd


class MainLongShortStrategy:
    """
    Main long/short strategy.
    """

    def __init__(self):
        self.name = 'MainLongShortStrategy'
        self.description = 'Main long/short strategy.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]

    # MAIN CASE STRATEGY : (Momentum + Volume + Volatility) + (OPEN<>CLOSE<>HIGH<>LOW)
    def evaluate_symbol(self, date, symbol, dataframe,
                        macd_short_window=10,
                        macd_long_window=20,
                        macd_signal_window=3,

                        atr_window=5,

                        volatility_threshold=0.001,
                        macd_threshold=0.05,

                        oc_diff_threshold=0.05,
                        hl_diff_threshold=0.05):

        if not date - pd.Timedelta(days=1) in dataframe['Date'].values:
            return self.signals[2]

        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]

        def calculate_macd(df, short_window=macd_short_window, long_window=macd_long_window,
                           signal_window=macd_signal_window):
            short_ema = df['Close'].ewm(span=short_window, adjust=False).mean()
            long_ema = df['Close'].ewm(span=long_window, adjust=False).mean()
            macd = short_ema - long_ema
            signal_line = macd.ewm(span=signal_window, adjust=False).mean()
            return macd.iloc[-1] - signal_line.iloc[-1]

        def calculate_atr(df, window=atr_window):
            high_low = df['High'] - df['Low']
            high_close = np.abs(df['High'] - df['Close'].shift())
            low_close = np.abs(df['Low'] - df['Close'].shift())
            ranges = pd.DataFrame({
                'high_low': high_low,
                'high_close': high_close,
                'low_close': low_close
            })
            true_range = ranges.max(axis=1)
            atr = true_range.rolling(window=window).mean()
            return atr.iloc[-1]

        # Calculate indicators
        macd = calculate_macd(dataframe, macd_short_window, macd_long_window, macd_signal_window)
        atr = calculate_atr(dataframe, atr_window)

        # Volume
        avg_volume = dataframe['Volume'].rolling(window=macd_long_window).mean().iloc[-1]
        last_day_volume = dataframe['Volume'].iloc[-1]

        # Price action
        last_day_data = dataframe.iloc[-1]
        open_close_diff = last_day_data['Close'] - last_day_data['Open']
        high_low_diff = last_day_data['High'] - last_day_data['Low']

        # Calculate signal
        if atr > volatility_threshold:
            if macd > macd_threshold:
                if last_day_volume > avg_volume:
                    if open_close_diff > oc_diff_threshold:
                        if high_low_diff > hl_diff_threshold:
                            return 'down'
                        else:
                            return 'hold'
                    else:
                        return 'down'
                else:
                    return 'up'
            else:
                return 'up'
        else:
            if macd > macd_threshold:
                if last_day_volume > avg_volume:
                    if open_close_diff > oc_diff_threshold:
                        if high_low_diff > hl_diff_threshold:
                            return 'up'
                        else:
                            return 'hold'
                    else:
                        return 'up'
                else:
                    return 'down'
            else:
                return 'down'

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            signal = self.evaluate_symbol(date, symbol, dataframe, macd_short_window=kwargs['macd_short_window'],
                                          macd_long_window=kwargs['macd_long_window'],
                                          macd_signal_window=kwargs['macd_signal_window'],
                                          atr_window=kwargs['atr_window'],
                                          volatility_threshold=kwargs['volatility_threshold'],
                                          macd_threshold=kwargs['macd_threshold'],
                                          oc_diff_threshold=kwargs['oc_diff_threshold'],
                                          hl_diff_threshold=kwargs['hl_diff_threshold'])
            signals[symbol] = signal
        print(signals)
        return signals

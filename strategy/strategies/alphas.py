import pandas as pd


class AlphaStrategy:
    """
    Alpha strategy base class.
    """
    def __init__(self):
        self.name = 'AlphaStrategy'
        self.description = 'Alpha strategy base class.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]

    # VOLUME WEIGHTED PRICE MOMENTUM
    def evaluate_symbol_001(self, date, symbol, dataframe, window=10, short_period=5, long_period=20):
        self.name = 'AlphaStrategy_001'
        if not date - pd.Timedelta(days=window) in dataframe['Date'].values:
            return self.signals[2]
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]

        def calculate_vwap(dataframe, period=window):
            cum_vol = dataframe['Volume'].rolling(window=period).sum()
            cum_vol_price = (dataframe['Close'] * dataframe['Volume']).rolling(window=period).sum()
            vwap = cum_vol_price / cum_vol
            return vwap

        dataframe['VWAP_Short'] = calculate_vwap(dataframe, short_period)
        dataframe['VWAP_Long'] = calculate_vwap(dataframe, long_period)
        if dataframe['VWAP_Short'].iloc[-1] > dataframe['VWAP_Long'].iloc[-1] and dataframe['VWAP_Short'].iloc[-2] <= \
                dataframe['VWAP_Long'].iloc[-2]:
            return self.signals[0]
        elif dataframe['VWAP_Short'].iloc[-1] < dataframe['VWAP_Long'].iloc[-1] and dataframe['VWAP_Short'].iloc[-2] >= \
                dataframe['VWAP_Long'].iloc[-2]:
            return self.signals[1]
        else:
            return self.signals[2]

    # MEAN REVERSION WITH VOLUME CONFIRMATION
    def evaluate_symbol_002(self, date, symbol, dataframe, window=30, mean_window=10, volume_window=10,
                            z_score_threshold=1.5):
        self.name = 'AlphaStrategy_002'
        if not date - pd.Timedelta(days=1) in dataframe['Date'].values:
            return self.signals[2]
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]

        def calculate_z_score(dataframe, window=window):
            mean = dataframe['Close'].rolling(window=window).mean()
            std_dev = dataframe['Close'].rolling(window=window).std()
            z_score = (dataframe['Close'] - mean) / std_dev
            return z_score

        dataframe['Z_Score'] = calculate_z_score(dataframe, window=mean_window)
        dataframe['Avg_Volume'] = dataframe['Volume'].rolling(window=volume_window).mean()
        if dataframe['Z_Score'].iloc[-1] < -z_score_threshold and dataframe['Volume'].iloc[-1] > \
                dataframe['Avg_Volume'].iloc[-1]:
            return self.signals[0]
        elif dataframe['Z_Score'].iloc[-1] > z_score_threshold and dataframe['Volume'].iloc[-1] > \
                dataframe['Avg_Volume'].iloc[-1]:
            return self.signals[1]
        else:
            return self.signals[2]

    # PRICE MOMENTUM WITH VOLATILITY ADJUSTMENT
    def evaluate_symbol_003(self, date, symbol, dataframe, period=14, momentum_period=10, atr_period=14):
        self.name = 'AlphaStrategy_003'
        if not date - pd.Timedelta(days=1) in dataframe['Date'].values:
            return self.signals[2]
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]

        def calculate_price_momentum(dataframe, period=period):
            momentum = dataframe['Close'].pct_change(periods=period)
            return momentum

        def calculate_atr(dataframe, period=period):
            high_low = dataframe['High'] - dataframe['Low']
            high_close = (dataframe['High'] - dataframe['Close'].shift()).abs()
            low_close = (dataframe['Low'] - dataframe['Close'].shift()).abs()

            ranges = pd.concat([high_low, high_close, low_close], axis=1)
            true_range = ranges.max(axis=1)
            atr = true_range.rolling(window=period).mean()
            return atr

        dataframe['Momentum'] = calculate_price_momentum(dataframe, period=momentum_period)
        dataframe['ATR'] = calculate_atr(dataframe, period=atr_period)
        if dataframe['Momentum'].iloc[-1] > 0 and dataframe['ATR'].iloc[-1] < dataframe['ATR'].mean():
            return self.signals[0]
        elif dataframe['Momentum'].iloc[-1] < 0 and dataframe['ATR'].iloc[-1] < dataframe['ATR'].mean():
            return self.signals[1]
        else:
            return self.signals[2]

    def evaluate_symbol_004(self, date, symbol, dataframe, period=14, fast_period=12, slow_period=26,
                            smooth_period=9):
        self.name = 'AlphaStrategy_004'
        if not date - pd.Timedelta(days=2) in dataframe['Date'].values:
            return self.signals[2]
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]

        def calculate_weighted_close(dataframe):
            weighted_close = (dataframe['Open'] + dataframe['High'] + dataframe['Low'] + dataframe['Close'] * 2) / 5
            return weighted_close

        def calculate_ema(dataframe, period=period):
            ema = dataframe.ewm(span=period, adjust=False).mean()
            return ema

        dataframe['Weighted_Close'] = calculate_weighted_close(dataframe)
        dataframe['Fast_EMA'] = calculate_ema(dataframe['Weighted_Close'], fast_period)
        dataframe['Slow_EMA'] = calculate_ema(dataframe['Weighted_Close'], slow_period)
        dataframe['Oscillator'] = dataframe['Fast_EMA'] - dataframe['Slow_EMA']
        dataframe['Smoothed_Oscillator'] = calculate_ema(dataframe['Oscillator'], smooth_period)
        if dataframe['Smoothed_Oscillator'].iloc[-1] > dataframe['Smoothed_Oscillator'].iloc[-2]:
            return self.signals[0]
        elif dataframe['Smoothed_Oscillator'].iloc[-1] < dataframe['Smoothed_Oscillator'].iloc[-2]:
            return self.signals[1]
        else:
            return self.signals[2]

    def evaluate_symbol_005(self, date, symbol, dataframe, period=20, short_period=12, long_period=26, signal_period=9,
                            threshold=1.5):
        self.name = 'AlphaStrategy_005'
        if not date - pd.Timedelta(days=1) in dataframe['Date'].values:
            return self.signals[2]
        dataframe = dataframe.copy()
        dataframe = dataframe[dataframe['Date'] < date]

        def calculate_macd(dataframe, short_period=short_period, long_period=long_period, signal_period=signal_period):
            short_ema = dataframe['Close'].ewm(span=short_period, adjust=False).mean()
            long_ema = dataframe['Close'].ewm(span=long_period, adjust=False).mean()
            macd = short_ema - long_ema
            signal_line = macd.ewm(span=signal_period, adjust=False).mean()
            return macd - signal_line

        def calculate_ppo(dataframe, short_period=short_period, long_period=long_period):
            short_ema = dataframe['Close'].ewm(span=short_period, adjust=False).mean()
            long_ema = dataframe['Close'].ewm(span=long_period, adjust=False).mean()
            ppo = ((short_ema - long_ema) / long_ema) * 100
            return ppo

        def calculate_dpo(dataframe, period=period):
            shifted_sma = dataframe['Close'].shift(period // 2 + 1).rolling(window=period).mean()
            dpo = dataframe['Close'] - shifted_sma
            return dpo

        dataframe['MACD_Score'] = calculate_macd(dataframe).apply(lambda x: 1 if x > 0 else -1)
        dataframe['PPO_Score'] = calculate_ppo(dataframe).apply(lambda x: 1 if x > 0 else -1)
        dataframe['DPO_Score'] = calculate_dpo(dataframe).apply(lambda x: 1 if x > 0 else -1)
        dataframe['Composite_Score'] = dataframe[['MACD_Score', 'PPO_Score', 'DPO_Score']].sum(axis=1)
        last_day_score = dataframe['Composite_Score'].iloc[-1]
        if last_day_score > threshold:
            return self.signals[0]
        elif last_day_score < -threshold:
            return self.signals[1]
        else:
            return self.signals[2]

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        for symbol, dataframe in universe.items():
            if kwargs['cmd'] == '01':
                signal = self.evaluate_symbol_001(date, symbol, dataframe, window=kwargs['window'],
                                                  short_period=kwargs['short_period'],
                                                  long_period=kwargs['long_period'])
            elif kwargs['cmd'] == '02':
                signal = self.evaluate_symbol_002(date, symbol, dataframe, window=kwargs['window'],
                                                  mean_window=kwargs['mean_window'],
                                                  volume_window=kwargs['volume_window'],
                                                  z_score_threshold=kwargs['z_score_threshold'])
            elif kwargs['cmd'] == '03':
                signal = self.evaluate_symbol_003(date, symbol, dataframe, period=kwargs['period'],
                                                  momentum_period=kwargs['momentum_period'],
                                                  atr_period=kwargs['atr_period'])
            elif kwargs['cmd'] == '04':
                signal = self.evaluate_symbol_004(date, symbol, dataframe, period=kwargs['period'],
                                                  fast_period=kwargs['fast_period'],
                                                  slow_period=kwargs['slow_period'],
                                                  smooth_period=kwargs['smooth_period'])
            elif kwargs['cmd'] == '05':
                signal = self.evaluate_symbol_005(date, symbol, dataframe, period=kwargs['period'],
                                                  short_period=kwargs['short_period'],
                                                  long_period=kwargs['long_period'],
                                                  signal_period=kwargs['signal_period'],
                                                  threshold=kwargs['threshold'])
            else:
                signal = self.evaluate_symbol_001(date, symbol, dataframe)
            signals[symbol] = signal
        return signals

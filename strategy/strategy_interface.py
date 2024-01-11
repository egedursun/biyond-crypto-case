import os
import copy as cp

from strategy.additional_tests.compare import compare_and_visualize, visualize_stock_positions
from strategy.exchange.Exchange import Exchange
from strategy.models.HyperParameters import HyperParameters
from strategy.models.Portfolio import Portfolio
from strategy.scraper.ScraperAgent import ScraperAgent
import pandas as pd

from strategy.strategies import rsi, macd, forest, randoms, deep_neural, main_case, bollinger, gpt_4, alphas, gpt3_5, \
    ema, naives, sma


def simulate(strategy, download_data=False, external_data=True, hyper_parameters=None, **kwargs):
    if hyper_parameters is None:
        hyper_parameters = HyperParameters

    if download_data:
        while hyper_parameters.Data.universe_size > len(hyper_parameters.Data.symbols):
            # take samples from csv
            df = pd.read_csv('strategy/data/metadata/coins_metadata.csv')
            for i in range(hyper_parameters.Data.universe_size):
                hyper_parameters.Data.symbols.append(df['symbol'][i])

            count_success_train = ScraperAgent(
                hyper_parameters.Data.symbols,
                hyper_parameters.Train.start_date,
                hyper_parameters.Train.end_date).download_price_data(is_training_data=True)
            count_success_test = ScraperAgent(
                hyper_parameters.Data.symbols,
                hyper_parameters.Test.start_date,
                hyper_parameters.Test.end_date).download_price_data(is_training_data=False)

            if count_success_train < hyper_parameters.Data.universe_size or \
                    count_success_test < hyper_parameters.Data.universe_size or \
                    len(os.listdir('strategy/data/train')) < hyper_parameters.Data.universe_size or \
                    len(os.listdir('strategy/data/test')) < hyper_parameters.Data.universe_size:
                print(f'[WARNING] Not enough data was found, retrying the process again...')
                hyper_parameters.Data.symbols = []
                for file in os.listdir('strategy/data/train'):
                    os.remove(f'strategy/data/train/{file}')
                for file in os.listdir('strategy/data/test'):
                    os.remove(f'strategy/data/test/{file}')
                continue
            print(f'[SUCCESS] Successfully downloaded {hyper_parameters.Data.universe_size} instruments...')

    if external_data:
        universe = {
            # 'symbol': pd.DataFrame
        }

        for file_name in os.listdir('strategy/data/external'):
            data = pd.read_csv(f'strategy/data/external/{file_name}')
            if "Date" not in data.columns:
                print(f'[ERROR] Date column not found in {file_name}')
                continue
            data = data.bfill(axis=0)
            data = data[
                (data['Date'] >= hyper_parameters.Test.start_date) & (data['Date'] <= hyper_parameters.Test.end_date)]

            length_days = len(pd.date_range(start=hyper_parameters.Test.start_date, end=hyper_parameters.Test.end_date))
            if len(data) != length_days:
                continue
            universe[file_name[:-4].replace(" ", "_")] = data

        for symbol, dataframe in universe.items():
            dataframe['Date'] = pd.to_datetime(dataframe['Date'])
            full_date_range = pd.date_range(start=hyper_parameters.Test.start_date, end=hyper_parameters.Test.end_date)
            dataframe = dataframe.set_index('Date').reindex(full_date_range, fill_value=None).reset_index()
            dataframe.rename(columns={'index': 'Date'}, inplace=True)
            dataframe.sort_values('Date', inplace=True)
            dataframe.reset_index(drop=True, inplace=True)

        for symbol, dataframe in universe.items():
            dataframe.drop_duplicates(subset=['Date'], keep='first', inplace=True)
            dataframe.reset_index(drop=True, inplace=True)

        ################################################################################################################
        # Run the strategy
        ################################################################################################################
        portfolio = Portfolio(
            hyper_parameters.Fund.initial_cash,
            hyper_parameters.Fund.transaction_volume,
            hyper_parameters.Fund.risk_free_rate,
            hyper_parameters.Fund.safety_margin)

        inst = strategy()
        exchange = Exchange()
        current_prices = {}
        benchmark = pd.DataFrame(columns=["Date", "Close"])
        p_values = []
        for i, date in enumerate(
                pd.date_range(start=hyper_parameters.Test.start_date, end=hyper_parameters.Test.end_date)):
            signals = inst.generate_signals(date, universe, portfolio, **kwargs)

            if i % hyper_parameters.Fund.trade_frequency != 0:
                continue

            if i % hyper_parameters.Fund.gpt_trade_frequency != 0 and inst.name in ["GPT3_5LongShortStrategy",
                                                                                    "GPT4LongShortStrategy"]:
                continue

            # current prices
            for symbol, dataframe in universe.items():
                current_prices[symbol] = dataframe[dataframe['Date'] == date]['Close'].values[0]

            current_prices_list = []
            for symbol, dictionary in current_prices.items():
                current_prices_list.append(dictionary)
            average_close = (sum(current_prices_list) / len(current_prices_list))
            benchmark = pd.concat([benchmark, pd.DataFrame([[date, average_close]], columns=["Date", "Close"])],
                                  ignore_index=True)
            portfolio, res = exchange.execute_orders(date, universe, portfolio, average_close, signals, current_prices,
                                                     hyper_parameters.Fund.transaction_cost,
                                                     hyper_parameters.Fund.transaction_volume_change_aggression,
                                                     hyper_parameters.Fund.transaction_volume_adjustment_window,
                                                     hyper_parameters.Fund.transaction_volume_minimum,
                                                     hyper_parameters.Fund.transaction_volume_maximum)

            positives = 0
            negatives = 0
            neutrals = 0
            if res is not None and type(res) == dict:
                positives = res["positives"]
                negatives = res["negatives"]
                neutrals = res["neutrals"]

            if i % 1 == 0:
                print(f"==========================================")
                print(f"DATE: {date.strftime('%Y-%m-%d')}")
                print(f"Total Portfolio Value: {portfolio.current_portfolio_value}")
                print(f"   - Cash ($): {portfolio.cash}")
                print(f"   - Asset Value ($): {portfolio.current_asset_value}")
                print(f"Positions: {portfolio.positions}")
                print(f"   - Positive Sentiments: {positives}")
                print(f"   - Negative Sentiments: {negatives}")
                print(f"   - Neutral Sentiments: {neutrals}")
                print(f"Total Orders: {positives + negatives + neutrals}")

            if res is not None and res == "BANKRUPT":
                print(f"==========================================")
                print(f"DATE: {date.strftime('%Y-%m-%d')}")
                print(f"BANKRUPTCY, failing the simulation...")
                print(f"==========================================")
                break

            p_values.append(cp.deepcopy(portfolio.positions))

        portfolio.visualize_metrics(strategy_name=inst.name)
        visualize_stock_positions(p_values, smoothen_days=20)
        cumulative_return_history = []
        for data in portfolio.portfolio_history:
            cumulative_return_history.append(data['portfolio_value'])
        return cumulative_return_history


def run(hyper_parameters=HyperParameters, test_set=None):
    print(f"Running simulation with hyper parameters: {hyper_parameters}")
    print(f"Running simulation with test set: {test_set}")
    overall_rets = {}

    if test_set is None:
        test_set = {
            "randoms": False,
            "naives": False,
            "rsi": True,
            "macd": False,
            "sma": False,
            "ema": False,
            "bollinger": False,
            "forest": False,
            "alphas": {
                "01": False,
                "02": False,
                "03": False,
                "04": False,
                "05": False,
            },
            "deep_neural": False,
            "gpt-3.5": False,
            "gpt-4": False,
            "main_case": False,
        }

    # Try the 'Random Long Short Strategy'
    if test_set["randoms"]:
        randoms_rets = simulate(strategy=randoms.RandomLongShortStrategy, download_data=False, external_data=True,
                                hyper_parameters=hyper_parameters)
        overall_rets["randoms"] = randoms_rets

    # Try the 'Naive Long Short Strategy'
    if test_set["naives"]:
        naives_rets = simulate(strategy=naives.NaiveLongShortStrategy, download_data=False, external_data=True,
                               window=15, hyper_parameters=hyper_parameters)
        overall_rets["naives"] = naives_rets

    # Try the 'RSI Long Short Strategy'
    if test_set["rsi"]:
        rsi_rets = simulate(strategy=rsi.RSILongShortStrategy, download_data=False, external_data=True, window=10,
                            down_threshold=30, up_threshold=70, hyper_parameters=hyper_parameters)
        overall_rets["rsi"] = rsi_rets

    # Try the 'MACD Long Short Strategy'
    if test_set["macd"]:
        macd_rets = simulate(strategy=macd.MACDLongShortStrategy, download_data=False, external_data=True,
                             short_window=12,
                             long_window=26, signal_window=9, hyper_parameters=hyper_parameters)
        overall_rets["macd"] = macd_rets

    # Try the 'SMA Long Short Strategy'
    if test_set["sma"]:
        sma_rets = simulate(strategy=sma.SMALongShortStrategy, download_data=False, external_data=True, window=15,
                            hyper_parameters=hyper_parameters)
        overall_rets["sma"] = sma_rets

    # Try the 'EMA Long Short Strategy'
    if test_set["ema"]:
        ema_rets = simulate(strategy=ema.EMALongShortStrategy, download_data=False, external_data=True, window=15,
                            hyper_parameters=hyper_parameters)
        overall_rets["ema"] = ema_rets

    # Try the 'Bollinger Bands Long Short Strategy'
    if test_set["bollinger"]:
        bollinger_rets = simulate(strategy=bollinger.BollingerLongShortStrategy, download_data=False,
                                  external_data=True,
                                  window=20, k=1,
                                  hyper_parameters=hyper_parameters)
        overall_rets["bollinger"] = bollinger_rets

    # Try the 'Forest Long Short Strategy'
    if test_set["forest"]:
        forest_rets = simulate(strategy=forest.ForestLongShortStrategy, download_data=False, external_data=True,
                               training_data_limit=20, n_estimators=10, hyper_parameters=hyper_parameters)
        overall_rets["forest"] = forest_rets

    # Try the 'Alphas Long Short Strategies'
    if test_set["alphas"]["01"]:
        a01_rets = simulate(strategy=alphas.AlphaStrategy, download_data=False, external_data=True,
                            cmd="01", window=10, short_period=20, long_period=30,
                            hyper_parameters=hyper_parameters)
        overall_rets["a01"] = a01_rets
    if test_set["alphas"]["02"]:
        a02_rets = simulate(strategy=alphas.AlphaStrategy, download_data=False, external_data=True,
                            cmd="02", window=5, mean_window=10, volume_window=20, z_score_threshold=1.1,
                            hyper_parameters=hyper_parameters)
        overall_rets["a02"] = a02_rets
    if test_set["alphas"]["03"]:
        a03_rets = simulate(strategy=alphas.AlphaStrategy, download_data=False, external_data=True,
                            cmd="03", period=10, momentum_period=5, atr_period=5,
                            hyper_parameters=hyper_parameters)
        overall_rets["a03"] = a03_rets
    if test_set["alphas"]["04"]:
        a04_rets = simulate(strategy=alphas.AlphaStrategy, download_data=False, external_data=True,
                            cmd="04", period=14, fast_period=12, slow_period=26, smooth_period=9,
                            hyper_parameters=hyper_parameters)
        overall_rets["a04"] = a04_rets
    if test_set["alphas"]["05"]:
        a05_rets = simulate(strategy=alphas.AlphaStrategy, download_data=False, external_data=True,
                            cmd="05", period=20, short_period=2, long_period=5, signal_period=3, threshold=1.5,
                            hyper_parameters=hyper_parameters)
        overall_rets["a05"] = a05_rets

    # Try the 'Deep Learning Long Short Strategy'
    if test_set["deep_neural"]:
        deep_rets = simulate(strategy=deep_neural.DeepLongShortStrategy, download_data=False, external_data=True,
                             learning_rate=0.1, epochs=1, hyper_parameters=hyper_parameters)
        overall_rets["deep"] = deep_rets

    # Try the 'GPT-3.5 Long Short Strategy'
    if test_set["gpt-3.5"]:
        gpt3_rets = simulate(strategy=gpt3_5.GPT_3_5LongShortStrategy, download_data=False, external_data=True,
                             hard_limit=1, lookback_limit=5, hyper_parameters=hyper_parameters)
        overall_rets["gpt-3.5"] = gpt3_rets

    # Try the 'GPT-4 Long Short Strategy'
    if test_set["gpt-4"]:
        gpt4_rets = simulate(strategy=gpt_4.GPT_4LongShortStrategy, download_data=False, external_data=True,
                             hard_limit=1, lookback_limit=5, hyper_parameters=hyper_parameters)
        overall_rets["gpt-4"] = gpt4_rets

    # MAIN CASE STRATEGY : (Momentum + Volume + Volatility) + (OPEN<>CLOSE<>HIGH<>LOW)
    if test_set["main_case"]:
        main_rets = simulate(strategy=main_case.MainLongShortStrategy, download_data=False, external_data=True,
                             macd_short_window=12, macd_long_window=26, macd_signal_window=9,
                             atr_window=14, volatility_threshold=0.1, macd_threshold=0.1, oc_diff_threshold=0.1,
                             hl_diff_threshold=0.1, hyper_parameters=hyper_parameters)
        overall_rets["main_case"] = main_rets

    compare_and_visualize(overall_rets)
    return

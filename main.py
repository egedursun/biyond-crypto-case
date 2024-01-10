import os

from exchange.Exchange import Exchange
from models.Portfolio import Portfolio
from scraper.ScraperAgent import ScraperAgent
import pandas as pd

from strategies import randoms, naives, rsi


class HyperParameters:

    class Fund:
        initial_cash = 1_000_000  # initial cash
        risk_free_rate = 0.01  # 1% per annum risk free rate
        safety_margin = 5  # 500% of the initial cash

        transaction_volume = 10  # N of shares per transaction
        trade_frequency = 1  # Every N days

        # TODO: extra parameters --- '''Not Implemented Yet'''
        transaction_cost = 0.01  # 1% of the transaction volume

    class Data:
        universe_size = 5
        symbols = []

    # redundant for direct datasets / non-training based datasets
    class Train:
        start_date = '2018-01-01'
        end_date = '2019-12-31'

    class Test:
        start_date = '2021-01-01'
        end_date = '2022-01-01'


def simulate(strategy, download_data=False, external_data=True, **kwargs):
    if download_data:
        while HyperParameters.Data.universe_size > len(HyperParameters.Data.symbols):
            # take samples from csv
            df = pd.read_csv('data/metadata/coins_metadata.csv')
            for i in range(HyperParameters.Data.universe_size):
                HyperParameters.Data.symbols.append(df['symbol'][i])

            # Download training data
            count_success_train = ScraperAgent(
                HyperParameters.Data.symbols,
                HyperParameters.Train.start_date,
                HyperParameters.Train.end_date).download_price_data(is_training_data=True)

            # Download testing data
            count_success_test = ScraperAgent(
                HyperParameters.Data.symbols,
                HyperParameters.Test.start_date,
                HyperParameters.Test.end_date).download_price_data(is_training_data=False)

            if count_success_train < HyperParameters.Data.universe_size or \
                    count_success_test < HyperParameters.Data.universe_size or \
                    len(os.listdir('data/train')) < HyperParameters.Data.universe_size or \
                    len(os.listdir('data/test')) < HyperParameters.Data.universe_size:
                print(f'[WARNING] Not enough data was found, retrying the process again...')
                HyperParameters.Data.symbols = []
                # clean the directories
                for file in os.listdir('data/train'):
                    os.remove(f'data/train/{file}')
                for file in os.listdir('data/test'):
                    os.remove(f'data/test/{file}')
                continue
            print(f'[SUCCESS] Successfully downloaded {HyperParameters.Data.universe_size} instruments...')

    if external_data:
        universe = {
            # 'symbol': pd.DataFrame
        }

        # Read external data by using the directory
        for file_name in os.listdir('data/external'):
            # read file as csv
            data = pd.read_csv(f'data/external/{file_name}')
            if "Date" not in data.columns:
                print(f'[ERROR] Date column not found in {file_name}')
                continue
            # fill the missing dates by back-filling in accordance to the max date
            data = data.bfill(axis=0)
            # get the relevant time period
            data = data[(data['Date'] >= HyperParameters.Test.start_date) & (data['Date'] <= HyperParameters.Test.end_date)]

            length_days = len(pd.date_range(start=HyperParameters.Test.start_date, end=HyperParameters.Test.end_date))
            if len(data) != length_days:
                continue

            # add to universe
            universe[file_name[:-4].replace(" ", "_")] = data

        for symbol, dataframe in universe.items():
            # Convert all dates to Timestamp if they are not already
            dataframe['Date'] = pd.to_datetime(dataframe['Date'])

            full_date_range = pd.date_range(start=HyperParameters.Test.start_date, end=HyperParameters.Test.end_date)
            dataframe = dataframe.set_index('Date').reindex(full_date_range, fill_value=None).reset_index()

            dataframe.rename(columns={'index': 'Date'}, inplace=True)
            dataframe.sort_values('Date', inplace=True)
            dataframe.reset_index(drop=True, inplace=True)

        # remove duplicates
        for symbol, dataframe in universe.items():
            dataframe.drop_duplicates(subset=['Date'], keep='first', inplace=True)
            dataframe.reset_index(drop=True, inplace=True)

        ################################################################################################################
        # Run the strategy
        ################################################################################################################
        portfolio = Portfolio(
            HyperParameters.Fund.initial_cash,
            HyperParameters.Fund.transaction_volume,
            HyperParameters.Fund.risk_free_rate,
            HyperParameters.Fund.safety_margin)

        inst = strategy()
        exchange = Exchange()
        current_prices = {}
        benchmark = pd.DataFrame(columns=["Date", "Close"])
        for i, date in enumerate(pd.date_range(start=HyperParameters.Test.start_date, end=HyperParameters.Test.end_date)):
            signals = inst.generate_signals(date, universe, portfolio, **kwargs)

            if i % HyperParameters.Fund.trade_frequency != 0:
                # print(f"Skipping trade on {date}")
                continue

            # current prices
            for symbol, dataframe in universe.items():
                current_prices[symbol] = dataframe[dataframe['Date'] == date]['Close'].values[0]

            # benchmark for the day
            current_prices_list = []
            for symbol, dictionary in current_prices.items():
                current_prices_list.append(dictionary)
            average_close = sum(current_prices_list) / len(current_prices_list)
            # add the average close to the benchmark
            benchmark = pd.concat([benchmark, pd.DataFrame([[date, average_close]], columns=["Date", "Close"])],
                                  ignore_index=True)

            # run the orders
            portfolio, res = exchange.execute_orders(date, universe, portfolio, average_close, signals, current_prices)

            positives = 0
            negatives = 0
            neutrals = 0
            if res is not None and type(res) == dict:
                positives = res["positives"]
                negatives = res["negatives"]
                neutrals = res["neutrals"]

            # show the portfolio
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

        # print the metrics
        portfolio.visualize_metrics(strategy_name=inst.name)


test_set = {
    "randoms": True,
    "naives": True,
    "rsi": True
}

if __name__ == '__main__':

    # Try the 'Random Long Short Strategy'
    if test_set["randoms"]:
        simulate(strategy=randoms.RandomLongShortStrategy, download_data=False, external_data=True)

    # Try the 'Naive Long Short Strategy'
    if test_set["naives"]:
        simulate(strategy=naives.NaiveLongShortStrategy, download_data=False, external_data=True, window=15)

    # Try the 'RSI Long Short Strategy'
    if test_set["rsi"]:
        simulate(strategy=rsi.RSILongShortStrategy, download_data=False, external_data=True, window=5,
                 down_threshold=20, up_threshold=99)

    pass

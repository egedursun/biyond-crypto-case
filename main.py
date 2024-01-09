import json
import os

from exchange.Exchange import Exchange
from models.Portfolio import Portfolio
from scraper.ScraperAgent import ScraperAgent
import pandas as pd

from strategies import randoms, naives


class HyperParameters:

    class Fund:
        initial_cash = 1_000_000  # initial cash
        risk_free_rate = 0.01  # 1% per annum risk free rate
        min_short_position = -10_000  # min short position per instrument
        max_long_position = 10_000  # max long position per instrument

        transaction_quantity = 100  # N of shares per transaction
        trade_frequency = 1  # Every N days

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


def simulate(strategy, download_data=False, external_data=True):
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
            HyperParameters.Fund.risk_free_rate,
            HyperParameters.Fund.min_short_position,
            HyperParameters.Fund.max_long_position,
            HyperParameters.Fund.transaction_quantity)

        inst = strategy()
        exchange = Exchange()
        positions = []
        for i, date in enumerate(pd.date_range(start=HyperParameters.Test.start_date, end=HyperParameters.Test.end_date)):
            signals = inst.generate_signals(date, universe, portfolio)

            if i % HyperParameters.Fund.trade_frequency != 0:
                # print(f"Skipping trade on {date}")
                continue

            # run the orders
            portfolio = exchange.execute_orders(date, universe, portfolio, signals)

            # show the portfolio
            if i % 10 == 0:
                print(f"Positions on {date}: {portfolio.positions}")
                print(f"Cash on {date}: {portfolio.cash}")
                print(f"Total returns on {date}: {portfolio.total_returns[-1]}")
                print(f"Portfolio Value on {date}: {portfolio.portfolio_values[-1]}")
                print(f"Sharpe ratio on {date}: {portfolio.sharpe_ratios[-1]}")
                print(f"Max Drawdown on {date}: {portfolio.max_drawdowns[-1]}")
                print("==========================================")

            positions.append({
                'date': date.strftime('%Y-%m-%d'),
                'positions': portfolio.positions,
            })

        print("==========================================")
        print("FINAL RESULTS")
        print("==========================================")
        print(f"Final portfolio value: {portfolio.total_value}")
        print(f"Final portfolio cash: {portfolio.cash}")
        print(f"Final portfolio positions: {portfolio.positions}")
        print(f"Final portfolio total returns: {portfolio.total_returns[-1]}")
        print(f"Final portfolio sharpe ratio: {portfolio.sharpe_ratios[-1]}")
        print(f"Final portfolio max drawdown: {portfolio.max_drawdowns[-1]}")

        # visualize the portfolio
        portfolio.visualize_financial_metrics(strategy.__name__.replace("/", "_"))

        # save the positions
        try:
            with open(f'output_portfolios/{strategy.__name__.replace("/", "_")}/positions.json', 'w') as f:
                json.dump(positions, f)
        except Exception as e:
            print(f"Error saving positions: {e}")


if __name__ == '__main__':

    # Try the 'Random Long Short Strategy', which is unlikely to produce promising results.
    simulate(strategy=randoms.RandomLongShortStrategy, download_data=False, external_data=True)

    # Try the 'Naive Long Short Strategy', which is a simple strategy that buys if the price is higher than the price
    # 10 days ago, sells if the price is lower than the price 10 days ago, and holds otherwise.
    """
    simulate(strategy=naives.NaiveLongShortStrategy, download_data=False, external_data=True)
    """

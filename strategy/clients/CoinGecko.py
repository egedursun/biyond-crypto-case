import datetime
from time import sleep

import requests
import dotenv


BASE_CURRENCY = 'usd'
RETRY_COUNT = 100

# Initialize dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values()


def is_retry_approved():
    global RETRY_COUNT
    max_retries = 2
    while RETRY_COUNT < max_retries:
        yield True
        RETRY_COUNT += 1
    RETRY_COUNT = 0
    yield False


class CoinGecko:

    def __init__(self):
        self.root = 'https://api.coingecko.com/api/v3/'
        self.api_key = config['COINGECKO_API_KEY']
        self.coin_ids = self.retrieve_coin_ids()

    def build_query_params_string(self, *param):
        query_params = ''
        if "?" not in self.root:
            query_params += '?'
        for p in param:
            query_params += f'{p[0]}={p[1]}&'
        query_params = query_params[:-1]
        return query_params

    def retrieve_coin_ids(self):
        route = 'coins/list'
        url = self.root + route
        try:
            response = requests.get(url, headers={
                'Accept': 'application/json', 'x-cg-pro-api-key': self.api_key})
        except Exception as err:
            exit(err)
        if response is None:
            exit(response)
        if response.status_code != 200:
            exit(response.json())
        coin_ids = {}
        for coin in response.json():
            coin_ids[coin['symbol']] = coin
        return coin_ids

    def get_price_data(self, symbol, start_date, end_date):
        symbol = symbol.lower()
        # convert start_date and end_date to unix timestamp
        start_date_object = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        start_date_timestamp = int(datetime.datetime.timestamp(start_date_object))
        end_date_object = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        end_date_timestamp = int(datetime.datetime.timestamp(end_date_object))
        if symbol not in self.coin_ids or self.coin_ids[symbol] is None or self.coin_ids[symbol]['id'] is None:
            print(f'[ERROR] {symbol} is not supported by CoinGecko...')
            return None
        coin_id = self.coin_ids[symbol]['id']
        route = f'coins/{coin_id}/market_chart/range'
        query_params = self.build_query_params_string(
            ('vs_currency', BASE_CURRENCY), ('from', start_date_timestamp), ('to', end_date_timestamp))
        url = self.root + route + query_params
        try:
            response = requests.get(url, headers={
                'Accept': 'application/json'})
        except Exception as err:
            exit(err)
        if response is None:
            exit(response)
        if str(response.status_code)[0] == '4':
            if not is_retry_approved():
                print(f'[ERROR] {response.json()}')
                return None
            print(f'[WARNING] The rate limit has been reached. Retrying in 60 seconds...')
            sleep(60)  # bypass rate limit
            return self.get_price_data(symbol, start_date, end_date)
        if "prices" not in response.json():
            return None
        print(f'[SUCCESS] Fetched {symbol} data from {start_date} to {end_date}...')
        return response.json()


# Test CoinGecko client
if __name__ == '__main__':
    cg = CoinGecko()
    print(cg.coin_ids)
    print(len(cg.coin_ids))

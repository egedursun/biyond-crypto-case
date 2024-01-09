import datetime
import os

from clients.CoinGecko import CoinGecko

# This value is used to determine how many days of missing data is acceptable
interpolation_cutoff = 0.2


class ScraperAgent:

    def __init__(self, symbols, start_date, end_date):
        self.cg = CoinGecko()
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def process_raw_price_data(raw_data, years_data):
        if raw_data is None:
            return None
        total_volumes = raw_data["total_volumes"]
        market_caps = raw_data["market_caps"]

        lines = 'date,price,total_volume,market_cap\n'

        # Simplification for now
        if "prices" not in raw_data or "total_volumes" not in raw_data or "market_caps" not in raw_data or \
                len(raw_data["prices"]) != len(raw_data["total_volumes"]) or \
                len(raw_data["prices"]) != len(raw_data["market_caps"]):
            print(f'[WARNING] Instrument has missing data, skipping...')
            return None
        if len(raw_data["prices"]) < ((365-int(365*interpolation_cutoff))*years_data) or\
                len(raw_data["prices"]) < (((365-int(365*interpolation_cutoff))*years_data)+1):
            print(f'[WARNING] Instrument as {len(raw_data["prices"])} days of data, skipping...')
            return None

        for i, data in enumerate(raw_data["prices"]):
            timestamp = data[0]
            # from unix timestamp to date
            date = datetime.datetime.utcfromtimestamp(int(str(timestamp)[:-3])).strftime('%Y-%m-%d')
            price = data[1]
            total_volume = total_volumes[i][1]
            market_cap = market_caps[i][1]
            new_line = f'{date},{price},{total_volume},{market_cap}\n'
            lines += new_line
        return lines

    def process_metadata(self):
        lines = 'symbol,id,name\n'
        for symbol, content in self.cg.coin_ids.items():
            if "," in symbol or "," in content["id"] or "," in content["name"]:
                continue
            new_line = f'{symbol},{content["id"]},{content["name"]}\n'
            lines += new_line
        return lines

    def download_price_data(self, is_training_data=True):
        sub_directory = 'train' if is_training_data else 'test'

        # Simplification for now
        years_data = 2 if is_training_data else 1

        metadata = self.process_metadata()
        try:
            with open(f'data/metadata/coins_metadata.csv', 'w') as f:
                f.write(metadata)
        except Exception as err:
            print(err)
            exit(1)

        count_success = 0
        for symbol in self.symbols:
            if f'{symbol}.csv' in os.listdir(f'data/{sub_directory}'):
                print(f'[WARNING] {symbol} already exists in data/{sub_directory}, skipping...')
                continue
            price_data = self.cg.get_price_data(symbol, self.start_date, self.end_date)
            if price_data is None:
                continue
            processed_price_data = self.process_raw_price_data(price_data, years_data)
            if processed_price_data is None:
                continue
            try:
                with open(f'data/{sub_directory}/{symbol}.csv', 'w') as f:
                    f.write(processed_price_data)
                count_success += 1
            except Exception as err:
                print(err)
                continue
        print(f'[SUCCESS] Downloaded price data successfully for ({count_success}/{len(self.symbols)}) symbols.')
        return count_success


if __name__ == '__main__':
    pass

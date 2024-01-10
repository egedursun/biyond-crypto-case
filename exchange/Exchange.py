from models import Portfolio


class Exchange:

    def __init__(self):
        pass

    @staticmethod
    def execute_orders(date, universe, portfolio: Portfolio, current_benchmark: list, orders: dict, current_prices: dict):
        portfolio.portfolio_value(current_prices=current_prices, benchmark=current_benchmark, date=date)

        r = ""
        positives = 0
        negatives = 0
        neutrals = 0
        for symbol, sentiment in orders.items():
            # get the price on the date, which is an index
            current_price = current_prices[symbol]
            if sentiment == 'up':
                r = portfolio.assign_upward(symbol, current_price, date)
                positives += 1
            elif sentiment == 'down':
                r = portfolio.assign_downward(symbol, current_price, date)
                negatives += 1
            elif sentiment == 'hold':
                r = portfolio.assign_hold(symbol, current_price, date)
                neutrals += 1
            else:
                print(f"Unknown sentiment: {sentiment} for symbol {symbol}")

        if r == "BANKRUPT":
            return portfolio, r
        else:
            return portfolio, {
                "positives": positives,
                "negatives": negatives,
                "neutrals": neutrals,
            }


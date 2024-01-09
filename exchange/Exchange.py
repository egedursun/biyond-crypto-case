from models import Portfolio


class Exchange:

    def __init__(self):
        pass

    @staticmethod
    def execute_orders(date, universe, portfolio: Portfolio, orders: dict, current_prices: dict):
        portfolio.portfolio_value(current_prices=current_prices, date=date)

        r = ""
        buys = 0
        sells = 0
        shorts = 0
        covers = 0
        holds = 0
        for symbol, order in orders.items():
            # get the price on the date, which is an index
            current_price = current_prices[symbol]

            if order == 'buy':
                r = portfolio.buy(symbol, current_price, date)
                buys += 1
            elif order == 'sell':
                r = portfolio.sell(symbol, current_price, date)
                sells += 1
            elif order == 'short':
                r = portfolio.short(symbol, current_price, date)
                shorts += 1
            elif order == 'cover':
                r = portfolio.cover(symbol, current_price, date)
                covers += 1
            elif order == 'hold':
                r = portfolio.hold(symbol, current_price, date)
                holds += 1
            else:
                print(f"Unknown order: {order} for symbol {symbol}")

        if r == "BANKRUPT":
            return portfolio, r
        else:
            return portfolio, {
                "buys": buys,
                "sells": sells,
                "shorts": shorts,
                "covers": covers,
                "holds": holds,
            }


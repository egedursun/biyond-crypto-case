from strategy.models import Portfolio


class Exchange:

    def __init__(self):
        pass

    @staticmethod
    def execute_orders(date, universe, portfolio: Portfolio, current_benchmark: list, orders: dict,
                       current_prices: dict,
                       transaction_cost=0.0, risk_tolerance=0.0,
                       returns_window=20, minimum_transaction_volume=10, maximum_transaction_volume=1000):
        portfolio.portfolio_value(current_prices=current_prices, benchmark=current_benchmark, date=date)
        r = ""
        positives = 0
        negatives = 0
        neutrals = 0
        for symbol, sentiment in orders.items():
            current_price = current_prices[symbol]
            if sentiment == 'up':
                r = portfolio.assign_upward(symbol, current_price, date, transaction_cost=transaction_cost,
                                            risk_tolerance=risk_tolerance,
                                            returns_window=returns_window,
                                            minimum_transaction_volume=minimum_transaction_volume,
                                            maximum_transaction_volume=maximum_transaction_volume)
                positives += 1
            elif sentiment == 'down':
                r = portfolio.assign_downward(symbol, current_price, date, transaction_cost=transaction_cost,
                                              risk_tolerance=risk_tolerance,
                                              returns_window=returns_window,
                                              minimum_transaction_volume=minimum_transaction_volume,
                                              maximum_transaction_volume=maximum_transaction_volume)
                negatives += 1
            elif sentiment == 'hold':
                r = portfolio.assign_hold(symbol, current_price, date, transaction_cost=transaction_cost,
                                          risk_tolerance=risk_tolerance,
                                          returns_window=returns_window,
                                          minimum_transaction_volume=minimum_transaction_volume,
                                          maximum_transaction_volume=maximum_transaction_volume)
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

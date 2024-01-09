class Exchange:

    def __init__(self):
        pass

    @staticmethod
    def execute_orders(date, universe, portfolio, orders: dict):
        for symbol, order in orders.items():
            # get the price on the date, which is an index
            dataframe = universe[symbol]
            current_price = dataframe[dataframe['Date'] == date]['Close'].values[0]

            if order == 'long':
                portfolio.buy(symbol, current_price, date)
            elif order == 'short':
                portfolio.sell(symbol, current_price, date)
            elif order == 'hold':
                portfolio.hold(symbol, current_price, date)
            else:  # hold on default or invalid
                # print(f"Invalid order: {order} for {symbol} on {date}.")
                portfolio.hold(symbol, current_price, date)

        return portfolio


import os

import numpy as np
from matplotlib import pyplot as plt


class Portfolio:
    def __init__(self, initial_cash, transaction_quantity, margin=0.2, risk_free_rate=0):
        self.cash = initial_cash
        self.transaction_quantity = transaction_quantity
        self.positions = {}
        self.negative_margin = margin

        self.initial_cash = initial_cash
        self.current_portfolio_value = 0
        self.current_asset_value = 0
        self.risk_free_rate = risk_free_rate

        # metrics
        self.daily_return = 0
        self.daily_return_std = 0
        self.daily_excess_return = 0
        self.cumulative_return = 0
        self.sharpe_ratio = 0
        self.max_drawdown = 0

        # history
        self.portfolio_history = []
        self.transaction_history = []

    def hold(self, ticker, price, date):
        if self.current_portfolio_value <= (0 - (max(self.cash, self.initial_cash) * self.negative_margin)):
            return "BANKRUPT"

        self.transaction_history.append({
            "date": date,
            "ticker": ticker,
            "action": "hold",
            "price": price,
            "quantity": 0,
            "total_cost": 0,
        })

    def buy(self, ticker, price, date):
        if self.current_portfolio_value <= (0 - (max(self.cash, self.initial_cash) * self.negative_margin)):
            return "BANKRUPT"

        cost = price * self.transaction_quantity
        if cost <= self.cash:
            self.cash -= cost
            self.positions[ticker] = self.positions.get(ticker, 0) + self.transaction_quantity

            self.transaction_history.append({
                "date": date,
                "ticker": ticker,
                "action": "buy",
                "price": price,
                "quantity": self.transaction_quantity,
                "total_cost": price * self.transaction_quantity,
            })
        else:
            self.hold(ticker, price, date)

    def sell(self, ticker, price, date):
        if self.current_portfolio_value <= (0 - (max(self.cash, self.initial_cash) * self.negative_margin)):
            return "BANKRUPT"

        if self.positions.get(ticker, 0) >= self.transaction_quantity:
            self.positions[ticker] -= self.transaction_quantity
            self.cash += price * self.transaction_quantity

            self.transaction_history.append({
                "date": date,
                "ticker": ticker,
                "action": "sell",
                "price": price,
                "quantity": self.transaction_quantity,
                "total_cost": price * self.transaction_quantity,
            })
        else:
            self.hold(ticker, price, date)

    def short(self, ticker, price, date):
        if self.current_portfolio_value <= (0 - (max(self.cash, self.initial_cash) * self.negative_margin)):
            return "BANKRUPT"

        self.positions[ticker] = self.positions.get(ticker, 0) - self.transaction_quantity
        self.cash += price * self.transaction_quantity

        self.transaction_history.append({
            "date": date,
            "ticker": ticker,
            "action": "short",
            "price": price,
            "quantity": self.transaction_quantity,
            "total_cost": price * self.transaction_quantity,
        })

    def cover(self, ticker, price, date):
        if self.current_portfolio_value <= (0 - (max(self.cash, self.initial_cash) * self.negative_margin)):
            return "BANKRUPT"

        if self.positions.get(ticker, 0) <= -self.transaction_quantity:
            self.positions[ticker] += self.transaction_quantity
            self.cash -= price * self.transaction_quantity

            self.transaction_history.append({
                "date": date,
                "ticker": ticker,
                "action": "cover",
                "price": price,
                "quantity": self.transaction_quantity,
                "total_cost": price * self.transaction_quantity,
            })

        else:
            self.hold(ticker, price, date)

    def portfolio_value(self, current_prices, date):
        value = self.cash
        for ticker, quantity in self.positions.items():
            value += quantity * current_prices[ticker]
        self.current_portfolio_value = value
        self.current_asset_value = value - self.cash

        # calculate metrics
        self.calculate_metrics()

        self.portfolio_history.append({
            "date": date,
            "portfolio_value": self.current_portfolio_value,
            "asset_value": self.current_asset_value,
            "cash": self.cash,
            "positions": self.positions,

            # metrics
            "daily_return": self.daily_return,
            "daily_return_std": self.daily_return_std,
            "daily_excess_return": self.daily_excess_return,
            "cumulative_return": self.cumulative_return,
            "sharpe_ratio": self.sharpe_ratio,
            "max_drawdown": self.max_drawdown,
        })
        return value

    def calculate_metrics(self):
        # calculate daily return
        self.daily_return = self.current_portfolio_value / self.portfolio_history[-1]["portfolio_value"] - 1 if len(self.portfolio_history) != 0 else 0
        # calculate daily return std
        self.daily_return_std = np.std([x["daily_return"] for x in self.portfolio_history]) if len(self.portfolio_history) != 0 else 0
        # calculate daily excess return
        self.daily_excess_return = self.daily_return - self.risk_free_rate
        # calculate total return
        self.cumulative_return = self.current_portfolio_value / self.initial_cash - 1 if len(self.portfolio_history) != 0 else 0
        # calculate sharpe ratio until now
        self.sharpe_ratio = self.daily_excess_return / self.daily_return_std if self.daily_return_std != 0 else 0
        print(self.daily_return_std)
        # calculate max draw-down
        self.max_drawdown = self.portfolio_history[-1]["portfolio_value"] if len(self.portfolio_history) != 0 else 0 / \
                            max([x["portfolio_value"] for x in self.portfolio_history] if self.portfolio_history != [] else [1])

    def visualize_metrics(self, strategy_name):

        # create output directory if not exists
        if not os.path.exists("results/" + strategy_name):
            os.makedirs("results/" + strategy_name)

        # visualize portfolio value, cash and asset value together
        plt.plot([x["date"] for x in self.portfolio_history], [x["portfolio_value"] for x in self.portfolio_history], label="Portfolio Value")
        plt.plot([x["date"] for x in self.portfolio_history], [x["cash"] for x in self.portfolio_history], label="Cash")
        plt.plot([x["date"] for x in self.portfolio_history], [x["asset_value"] for x in self.portfolio_history], label="Asset Value")
        plt.xlabel("Date")
        plt.ylabel("Value ($)")
        plt.xticks(rotation=45)
        plt.title("Portfolio Value, Cash and Asset Value")
        plt.legend()
        plt.grid()
        plt.savefig("results/" + strategy_name + "/portfolio_value_cash_asset_value.png")

        # visualize daily return
        plt.plot([x["date"] for x in self.portfolio_history], [x["daily_return"] for x in self.portfolio_history])
        plt.xlabel("Date")
        plt.ylabel("Daily Return")
        plt.xticks(rotation=45)
        plt.title("Daily Returns")
        plt.grid()
        plt.savefig("results/" + strategy_name + "/daily_returns.png")
        plt.clf()

        # visualize daily return std
        plt.plot([x["date"] for x in self.portfolio_history], [x["daily_return_std"] for x in self.portfolio_history])
        plt.xlabel("Date")
        plt.ylabel("Daily Return Std")
        plt.xticks(rotation=45)
        plt.title("Daily Return Std")
        plt.grid()
        plt.savefig("results/" + strategy_name + "/daily_return_std.png")
        plt.clf()

        # visualize daily excess return
        plt.plot([x["date"] for x in self.portfolio_history], [x["daily_excess_return"] for x in self.portfolio_history])
        plt.xlabel("Date")
        plt.ylabel("Daily Excess Return")
        plt.xticks(rotation=45)
        plt.title("Daily Excess Return")
        plt.grid()
        plt.savefig("results/" + strategy_name + "/daily_excess_return.png")
        plt.clf()

        # visualize cumulative return
        plt.plot([x["date"] for x in self.portfolio_history], [x["cumulative_return"] for x in self.portfolio_history])
        plt.xlabel("Date")
        plt.ylabel("Cumulative Return")
        plt.xticks(rotation=45)
        plt.title("Cumulative Return")
        plt.grid()
        plt.savefig("results/" + strategy_name + "/cumulative_return.png")
        plt.clf()

        # visualize sharpe ratio
        plt.plot([x["date"] for x in self.portfolio_history], [x["sharpe_ratio"] for x in self.portfolio_history])
        plt.xlabel("Date")
        plt.ylabel("Sharpe Ratio")
        plt.xticks(rotation=45)
        plt.title("Sharpe Ratio")
        plt.grid()
        plt.savefig("results/" + strategy_name + "/sharpe_ratio.png")
        plt.clf()

        # visualize max drawdown
        plt.plot([x["date"] for x in self.portfolio_history], [x["max_drawdown"] for x in self.portfolio_history])
        plt.xlabel("Date")
        plt.ylabel("Max Drawdown")
        plt.xticks(rotation=45)
        plt.title("Max Drawdown")
        plt.grid()
        plt.savefig("results/" + strategy_name + "/max_drawdown.png")
        plt.clf()


if __name__ == "__main__":
    # random walk
    prices = np.random.normal(0, 1, 100000).cumsum()
    portfolio = Portfolio(1000, 100)
    for i, p in enumerate(prices):
        c = np.random.choice([0, 1, 2, 3, 4])
        if c == 0:
            r = portfolio.buy("AAPL", p, i)
        elif c == 1:
            r = portfolio.sell("AAPL", p, i)
        elif c == 2:
            r = portfolio.short("AAPL", p, i)
        elif c == 3:
            r = portfolio.cover("AAPL", p, i)
        else:
            r = portfolio.hold("AAPL", p, i)
        if r == "BANKRUPT":
            print("BANKRUPTCY, failing the simulation...")
            break
        print("Portfolio Value: ", portfolio.current_portfolio_value)
        print("Cash: ", portfolio.cash)
        print("Positions: ", portfolio.positions)
        print("Action: ", "buy" if c == 0 else "sell" if c == 1 else "hold")
        print()
    print("Final - Portfolio Value: ", portfolio.current_portfolio_value)
    print("Final - Cash: ", portfolio.cash)
    print("Final - Positions: ", portfolio.positions)
    print()

import numpy as np


class Portfolio:
    def __init__(self, initial_cash, risk_free_rate=0.01, min_short_position=-10000, max_long_position=10000, transaction_quantity=100):
        self.cash = initial_cash
        self.positions = {}
        self.short_prices = {}
        self.current_portfolio_value = initial_cash

        # Financial metrics
        self.transaction_history = []
        self.portfolio_history = []
        self.portfolio_values = [initial_cash]
        self.sharpe_ratios = []
        self.max_drawdowns = [0]
        self.total_returns = [0]
        self.excess_daily_returns = []

        self.risk_free_rate = risk_free_rate
        self.min_short_position = min_short_position
        self.max_long_position = max_long_position
        self.transaction_quantity = transaction_quantity

    def _update_portfolio_value(self, asset_name, price_per_unit, date):
        new_portfolio_value = self.cash
        for asset, quantity in self.positions.items():
            if asset == asset_name:
                del self.positions[asset]
                new_value = (price_per_unit * quantity)
                self.positions[asset] = new_value
                new_portfolio_value += new_value

    def buy(self, asset_name, price_per_unit, date):
        self._update_portfolio_value(asset_name, price_per_unit, date)
        # Check if we have enough cash to buy
        if self.cash < (price_per_unit * self.transaction_quantity):
            self.hold(asset_name, date)
        # Check if we already have a position
        if asset_name in self.positions:
            if self.positions[asset_name] > 0:
                # long position
                # reduce cash
                self.cash -= (price_per_unit * self.transaction_quantity)
                # increase position
                self.positions[asset_name] += self.transaction_quantity
                pass
            elif self.positions[asset_name] < 0:
                # short position
                pass

    def sell(self, asset_name, price_per_unit, date):
        pass

    def hold(self, asset_name, date):
        self._record_transaction('hold', asset_name, 0, 0, date)

    def _record_transaction(self, transaction_type, asset_name, quantity, price_per_unit, date):
        self.transaction_history.append({
            'type': transaction_type,
            'asset': asset_name,
            'quantity': quantity,
            'unit_price': price_per_unit,
            'date': date,
        })

    def _record_portfolio(self, date):
        self.portfolio_history.append({
            'date': date,
            'positions': self.positions,
            'cash': self.cash,
            'portfolio_value': self.current_portfolio_value,

            'total_returns': self.total_returns[-1],
            'sharpe_ratio': self.sharpe_ratios[-1],
            'max_drawdown': self.max_drawdowns[-1],
            'excess_daily_returns': self.excess_daily_returns[-1],
        })

    def _update_financial_metrics(self, price_per_unit):
        pass

    def _visualize_financial_metrics(self):
        pass


if __name__ == "__main__":
    pass

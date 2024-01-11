import pandas as pd


def adjust_transaction_volume(portfolio_value, initial_portfolio_value, cash, initial_cash,
                              current_transaction_volume, daily_returns, risk_tolerance,
                              returns_window=20, minimum_transaction_volume=10,
                              maximum_transaction_volume=1000):
    daily_returns = pd.Series(daily_returns)
    internal_smooth__very_high = 1.0
    internal_smooth__high = 0.8
    internal_smooth__medium = 0.6
    internal_smooth__low = 0.4
    internal_smooth__very_low = 0.2
    internal_smooth__null = 0.0
    if portfolio_value > initial_portfolio_value:
        if cash > initial_cash:
            if daily_returns[-returns_window:].mean() > 0:
                return min(max(int(current_transaction_volume * (1 + internal_smooth__very_high * risk_tolerance)),
                           minimum_transaction_volume), maximum_transaction_volume)
            else:
                return min(max(int(current_transaction_volume * (1 + internal_smooth__high * risk_tolerance)),
                           minimum_transaction_volume), maximum_transaction_volume)
        else:
            if daily_returns[-returns_window:].mean() > 0:
                return min(max(int(current_transaction_volume * (1 + internal_smooth__medium * risk_tolerance)),
                           minimum_transaction_volume), maximum_transaction_volume)
            else:
                return min(max(int(current_transaction_volume * (1 + internal_smooth__low * risk_tolerance)),
                           minimum_transaction_volume), maximum_transaction_volume)
    else:
        if cash > initial_cash:
            if daily_returns[-returns_window:].mean() > 0:
                return min(max(int(current_transaction_volume * (1 - internal_smooth__medium * risk_tolerance)),
                           minimum_transaction_volume), maximum_transaction_volume)
            else:
                return min(max(int(current_transaction_volume * (1 - internal_smooth__low * risk_tolerance)),
                           minimum_transaction_volume), maximum_transaction_volume)
        else:
            if daily_returns[-returns_window:].mean() > 0:
                return min(max(int(current_transaction_volume * (1 - internal_smooth__very_low * risk_tolerance)),
                           minimum_transaction_volume), maximum_transaction_volume)
            else:
                return min(max(int(current_transaction_volume * (1 - internal_smooth__null * risk_tolerance)),
                           minimum_transaction_volume), maximum_transaction_volume)

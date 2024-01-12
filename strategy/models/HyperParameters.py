
class HyperParameters:
    class Fund:
        initial_cash = 1_000_000  # initial cash
        risk_free_rate = 0.01  # 1% per annum risk free rate
        safety_margin = 5  # 500% of the initial cash

        transaction_volume = 80  # N of shares per transaction
        trade_frequency = 1  # Every N days
        gpt_trade_frequency = 15  # Every N days for GPT requests

        transaction_cost = 0.001  # N% of the transaction volume

        transaction_volume_change_aggression = 0.02  # N% of the transaction volume - 0.0 means no change
        transaction_volume_adjustment_window = 20  # N days
        transaction_volume_minimum = 10  # min N of shares per transaction
        transaction_volume_maximum = 150  # max N of shares per transaction

    class Data:
        universe_size = 5
        symbols = []

    ###############################################################
    # Redundant for direct datasets / non-training based datasets
    ###############################################################
    class Train:
        start_date = '2018-01-01'
        end_date = '2019-12-31'

    class Test:
        start_date = '2021-01-01'
        end_date = '2022-01-01'

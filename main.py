from strategy.models.HyperParameters import HyperParameters
from strategy.strategy_interface import run

# Test set
test_set = {
    "randoms": True,
    "naives": True,
    "rsi": True,
    "macd": False,
    "sma": False,
    "ema": False,
    "bollinger": False,
    "forest": False,
    "alphas":
    {
        "01": False,
        "02": False,
        "03": False,
        "04": False,
        "05": False,
    },
    "deep_neural": False,
    "gpt-3.5": False,
    "gpt-4": False,
    "main_case": False,
}

# Hyperparameters
hyperparameters = HyperParameters()


if __name__ == '__main__':
    run(hyperparameters, test_set)

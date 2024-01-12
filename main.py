from auto_documentation.analyzer import generate_report
from strategy.models.HyperParameters import HyperParameters
from strategy.strategy_interface import run

ANALYSIS_MODE = True

# Test set
test_set = {
    "randoms": True,
    "naives": True,
    "rsi": True,
    "macd": True,
    "sma": True,
    "ema": True,
    "bollinger": True,
    "forest": True,
    "alphas":
    {
        "01": True,
        "02": True,
        "03": True,
        "04": True,
        "05": True,
    },
    "deep_neural": False,
    "gpt-3.5": False,
    "gpt-4": False,
    "main_case": True,
}

# Hyperparameters
hyperparameters = HyperParameters()


def analysis_mode():
    generate_report()


if __name__ == '__main__':
    if ANALYSIS_MODE:
        analysis_mode()
    else:
        run(hyperparameters, test_set)

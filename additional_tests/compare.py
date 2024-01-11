import datetime
import os
from typing import List

import pandas as pd
import matplotlib.pyplot as plt


def create_directory_if_not_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def compare_and_visualize(overall_rets: dict[str, List]):
    create_directory_if_not_exists('additional_tests/performance_outputs')

    for name, rets in overall_rets.items():
        if len(rets) == 0:
            continue
        plt.plot(rets, label=name)

    plt.title('Cumulative Return Comparison')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.grid()
    plt.savefig(f'additional_tests/performance_outputs/performance_comparison_chart_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
    plt.clf()


def visualize_stock_positions(portfolio_history, smoothen_days=20):
    create_directory_if_not_exists('additional_tests/performance_outputs')

    # retrieve first 'limit' stocks
    ys1 = [(p["IOTA"] if "IOTA" in p else 0) for p in portfolio_history]
    ys2 = [(p["chainlink"] if "chainlink" in p else 0) for p in portfolio_history]
    ys3 = [(p["Helium"] if "Helium" in p else 0) for p in portfolio_history]

    # smoothen the curve
    ys1 = pd.Series(ys1).rolling(smoothen_days).mean()
    ys2 = pd.Series(ys2).rolling(smoothen_days).mean()
    ys3 = pd.Series(ys3).rolling(smoothen_days).mean()

    plt.plot(list(range(len(portfolio_history))), ys1, label="IOTA")
    plt.plot(list(range(len(portfolio_history))), ys2, label="chainlink")
    plt.plot(list(range(len(portfolio_history))), ys3, label="Helium")

    plt.title('Stock Positions')
    plt.xlabel('Date')
    plt.ylabel('Position')
    plt.legend()
    plt.grid()
    plt.savefig(f'additional_tests/performance_outputs/stock_positions_chart_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
    plt.clf()

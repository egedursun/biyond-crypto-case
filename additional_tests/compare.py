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
        plt.plot(rets, label=name)

    plt.title('Cumulative Return Comparison')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.grid()
    plt.savefig(f'additional_tests/performance_outputs/performance_comparison_chart_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')


def visualize_stock_positions(portfolio_history, limit=1):
    create_directory_if_not_exists('additional_tests/performance_outputs')

    # retrieve first 'limit' stocks
    ys = [p['positions']["IOTA"] for p in portfolio_history]
    plt.scatter([p["date"] for p in portfolio_history], ys, label="IOTA")

    plt.title('Stock Positions')
    plt.xlabel('Date')
    plt.ylabel('Position')
    plt.legend()
    plt.grid()
    plt.savefig(f'additional_tests/performance_outputs/stock_positions_chart_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')

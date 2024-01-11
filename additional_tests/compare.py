import datetime
from typing import List

import pandas as pd
import matplotlib.pyplot as plt


def compare_and_visualize(overall_rets: dict[str, List]):
    for name, rets in overall_rets.items():
        plt.plot(rets, label=name)

    plt.title('Cumulative Return Comparison')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.grid()
    plt.savefig(f'performance_outputs/performance_comparison_chart_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')


def visualize_stock_positions(portfolio_history):
    for symbol in portfolio_history['positions'].keys():
        for position in portfolio_history['positions'][symbol]:
            plt.plot(position, label=symbol)

    plt.title('Stock Positions')
    plt.xlabel('Date')
    plt.ylabel('Position')
    plt.legend()
    plt.grid()
    plt.savefig(f'performance_outputs/stock_positions_chart_{datetime.datetime.now().strptime("%Y-%m-%d_%H-%M-%S")}.png')

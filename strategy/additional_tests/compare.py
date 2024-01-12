import datetime
import os
from typing import List

import pandas as pd
import matplotlib.pyplot as plt


def create_directory_if_not_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def compare_and_visualize(overall_rets: dict[str, List]):
    create_directory_if_not_exists('strategy/additional_tests/performance_outputs')
    for name, rets in overall_rets.items():
        if len(rets) == 0:
            continue
        plt.plot(rets, label=name)
    plt.title('Cumulative Return Comparison')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.grid()
    plt.savefig(f'strategy/additional_tests/performance_outputs/performance_comparison_chart.png')
    plt.clf()


def visualize_stock_positions(portfolio_history, smoothen_days=20, strategy_name="noname"):
    create_directory_if_not_exists('strategy/additional_tests/performance_outputs')
    ys1 = [(p["IOTA"] if "IOTA" in p else 0) for p in portfolio_history]
    ys2 = [(p["chainlink"] if "chainlink" in p else 0) for p in portfolio_history]
    ys3 = [(p["Helium"] if "Helium" in p else 0) for p in portfolio_history]
    ys4 = [(p["Aave"] if "Aave" in p else 0) for p in portfolio_history]
    ys5 = [(p["avalanche"] if "avalanche" in p else 0) for p in portfolio_history]
    ys6 = [(p["BNB"] if "BNB" in p else 0) for p in portfolio_history]
    ys7 = [(p["cardano"] if "cardano" in p else 0) for p in portfolio_history]
    ys8 = [(p["Celcius"] if "Celcius" in p else 0) for p in portfolio_history]
    ys9 = [(p["cosmos"] if "cosmos" in p else 0) for p in portfolio_history]
    ys10 = [(p["Cronos"] if "Cronos" in p else 0) for p in portfolio_history]
    ys11 = [(p["Dash"] if "Dash" in p else 0) for p in portfolio_history]
    ys12 = [(p["Decentraland"] if "Decentraland" in p else 0) for p in portfolio_history]
    ys13 = [(p["dogecoin"] if "dogecoin" in p else 0) for p in portfolio_history]
    ys14 = [(p["Elrond"] if "Elrond" in p else 0) for p in portfolio_history]
    ys15 = [(p["ethereum"] if "ethereum" in p else 0) for p in portfolio_history]
    ys16 = [(p["Flow"] if "Flow" in p else 0) for p in portfolio_history]
    ys17 = [(p["Gala"] if "Gala" in p else 0) for p in portfolio_history]
    ys18 = [(p["Hedera"] if "Hedera" in p else 0) for p in portfolio_history]
    ys19 = [(p["Holo"] if "Holo" in p else 0) for p in portfolio_history]
    ys20 = [(p["IOTA"] if "IOTA" in p else 0) for p in portfolio_history]
    ys21 = [(p["Kusama"] if "Kusama" in p else 0) for p in portfolio_history]
    ys22 = [(p["litecoin"] if "litecoin" in p else 0) for p in portfolio_history]
    ys23 = [(p["Maker"] if "Maker" in p else 0) for p in portfolio_history]
    ys24 = [(p["monero"] if "monero" in p else 0) for p in portfolio_history]
    ys25 = [(p["Nexo"] if "Nexo" in p else 0) for p in portfolio_history]
    ys1 = pd.Series(ys1).rolling(smoothen_days).mean()
    ys2 = pd.Series(ys2).rolling(smoothen_days).mean()
    ys3 = pd.Series(ys3).rolling(smoothen_days).mean()
    ys4 = pd.Series(ys4).rolling(smoothen_days).mean()
    ys5 = pd.Series(ys5).rolling(smoothen_days).mean()
    ys6 = pd.Series(ys6).rolling(smoothen_days).mean()
    ys7 = pd.Series(ys7).rolling(smoothen_days).mean()
    ys8 = pd.Series(ys8).rolling(smoothen_days).mean()
    ys9 = pd.Series(ys9).rolling(smoothen_days).mean()
    ys10 = pd.Series(ys10).rolling(smoothen_days).mean()
    ys11 = pd.Series(ys11).rolling(smoothen_days).mean()
    ys12 = pd.Series(ys12).rolling(smoothen_days).mean()
    ys13 = pd.Series(ys13).rolling(smoothen_days).mean()
    ys14 = pd.Series(ys14).rolling(smoothen_days).mean()
    ys15 = pd.Series(ys15).rolling(smoothen_days).mean()
    ys16 = pd.Series(ys16).rolling(smoothen_days).mean()
    ys17 = pd.Series(ys17).rolling(smoothen_days).mean()
    ys18 = pd.Series(ys18).rolling(smoothen_days).mean()
    ys19 = pd.Series(ys19).rolling(smoothen_days).mean()
    ys20 = pd.Series(ys20).rolling(smoothen_days).mean()
    ys21 = pd.Series(ys21).rolling(smoothen_days).mean()
    ys22 = pd.Series(ys22).rolling(smoothen_days).mean()
    ys23 = pd.Series(ys23).rolling(smoothen_days).mean()
    ys24 = pd.Series(ys24).rolling(smoothen_days).mean()
    ys25 = pd.Series(ys25).rolling(smoothen_days).mean()
    plt.figure(figsize=(20, 10))
    plt.plot(list(range(len(portfolio_history))), ys1, label="IOTA")
    plt.plot(list(range(len(portfolio_history))), ys2, label="chainlink")
    plt.plot(list(range(len(portfolio_history))), ys3, label="Helium")
    plt.plot(list(range(len(portfolio_history))), ys4, label="Aave")
    plt.plot(list(range(len(portfolio_history))), ys5, label="avalanche")
    plt.plot(list(range(len(portfolio_history))), ys6, label="BNB")
    plt.plot(list(range(len(portfolio_history))), ys7, label="cardano")
    plt.plot(list(range(len(portfolio_history))), ys8, label="Celcius")
    plt.plot(list(range(len(portfolio_history))), ys9, label="cosmos")
    plt.plot(list(range(len(portfolio_history))), ys10, label="Cronos")
    plt.plot(list(range(len(portfolio_history))), ys11, label="Dash")
    plt.plot(list(range(len(portfolio_history))), ys12, label="Decentraland")
    plt.plot(list(range(len(portfolio_history))), ys13, label="dogecoin")
    plt.plot(list(range(len(portfolio_history))), ys14, label="Elrond")
    plt.plot(list(range(len(portfolio_history))), ys15, label="ethereum")
    plt.plot(list(range(len(portfolio_history))), ys16, label="Flow")
    plt.plot(list(range(len(portfolio_history))), ys17, label="Gala")
    plt.plot(list(range(len(portfolio_history))), ys18, label="Hedera")
    plt.plot(list(range(len(portfolio_history))), ys19, label="Holo")
    plt.plot(list(range(len(portfolio_history))), ys20, label="IOTA")
    plt.plot(list(range(len(portfolio_history))), ys21, label="Kusama")
    plt.plot(list(range(len(portfolio_history))), ys22, label="litecoin")
    plt.plot(list(range(len(portfolio_history))), ys23, label="Maker")
    plt.plot(list(range(len(portfolio_history))), ys24, label="monero")
    plt.plot(list(range(len(portfolio_history))), ys25, label="Nexo")
    plt.title('Stock Positions')
    plt.xlabel('Date')
    plt.ylabel('Position')
    plt.legend()
    plt.grid()
    plt.savefig(f'strategy/additional_tests/performance_outputs/stock_positions_chart_{strategy_name}.png')
    plt.clf()

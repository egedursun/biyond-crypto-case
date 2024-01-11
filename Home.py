import time
import requests
import streamlit as st
from main import test_set


# TODO-2: make function parameters dynamic on Streamlit
hyperparameters = {
    'initial_cash': 1_000_000,
    'risk_free_rate': 0.01,
    'safety_margin': 5,
    'transaction_volume': 80,
    'trade_frequency': 1,
    'gpt_trade_frequency': 15,
    'transaction_cost': 0.002,
    'transaction_volume_change_aggression': 0.05,
    'transaction_volume_adjustment_window': 20,
    'transaction_volume_minimum': 10,
    'transaction_volume_maximum': 150,
}


def lit():
    st.title("Biyond - Crypto Case Study")
    st.write("A sample web app to showcase the portfolio performances of different strategies.")

    st.divider()

    st.write("## Strategies (Long/Short)")

    st.text("' ' ' ' '")

    st.markdown("### Hyper-Parameters")

    st.markdown("#### Portfolio")
    st.text_input("Initial Cash", value=1_000_000)
    st.text_input("Risk Free Rate", value=0.01)
    st.text_input("Safety Margin", value=5)

    st.empty()

    st.markdown("#### Transactions")
    st.text_input("Transaction Volume", value=80)
    st.text_input("Transaction Cost", value=0.002)
    st.text_input("Transaction Volume Change Aggression", value=0.05)
    st.text_input("Transaction Volume Adjustment Window", value=20)
    st.text_input("Transaction Volume Minimum", value=10)
    st.text_input("Transaction Volume Maximum", value=150)

    st.empty()

    st.markdown("#### Trade Frequency")
    st.text_input("Trade Frequency", value=1)
    st.text_input("GPT Trade Frequency", value=15)

    if st.button("Update Hyper-Parameters"):
        # TODO: update the hyperparameters
        pass

    st.text("' ' ' ' '")

    st.divider()

    st.subheader("**Random**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    if st.button("Simulate Random Strategy"):
        with st.spinner("Simulating Random Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/1",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass  # placeholder
            else:
                pass  # placeholder

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/RandomLongShortStrategy/cumulative_return.png")
                st.image("strategy/results/RandomLongShortStrategy/daily_returns.png")
                st.image("strategy/results/RandomLongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/RandomLongShortStrategy/daily_return_std.png")
                st.image("strategy/results/RandomLongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/RandomLongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**Naive**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    if st.button("Simulate Naive Strategy"):
        with st.spinner("Simulating Naive Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/2",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/NaiveLongShortStrategy/cumulative_return.png")
                st.image("strategy/results/NaiveLongShortStrategy/daily_returns.png")
                st.image("strategy/results/NaiveLongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/NaiveLongShortStrategy/daily_return_std.png")
                st.image("strategy/results/NaiveLongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/NaiveLongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**Simple Moving Average**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Window Size** ")

    if st.button("Simulate Simple Moving Average Strategy"):
        with st.spinner("Simulating Simple Moving Average Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/3",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/SMALongShortStrategy/cumulative_return.png")
                st.image("strategy/results/SMALongShortStrategy/daily_returns.png")
                st.image("strategy/results/SMALongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/SMALongShortStrategy/daily_return_std.png")
                st.image("strategy/results/SMALongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/SMALongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**Exponential Moving Average**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Window Size**")

    if st.button("Simulate Exponential Moving Average Strategy"):
        with st.spinner("Simulating Exponential Moving Average Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/4",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/EMALongShortStrategy/cumulative_return.png")
                st.image("strategy/results/EMALongShortStrategy/daily_returns.png")
                st.image("strategy/results/EMALongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/EMALongShortStrategy/daily_return_std.png")
                st.image("strategy/results/EMALongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/EMALongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**Bollinger Bands**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Window Size**")
    st.write("    - **Number of Standard Deviations**")

    if st.button("Simulate Bollinger Bands Strategy"):
        with st.spinner("Simulating Bollinger Bands Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/5",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/BoilingerLongShortStrategy/cumulative_return.png")
                st.image("strategy/results/BoilingerLongShortStrategy/daily_returns.png")
                st.image("strategy/results/BoilingerLongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/BoilingerLongShortStrategy/daily_return_std.png")
                st.image("strategy/results/BoilingerLongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/BoilingerLongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**Relative Strength Index**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Window Size**")
    st.write("    - **Upper Threshold**")
    st.write("    - **Lower Threshold**")

    if st.button("Simulate Relative Strength Index Strategy"):
        with st.spinner("Simulating Relative Strength Index Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/6",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/RSILongShortStrategy/cumulative_return.png")
                st.image("strategy/results/RSILongShortStrategy/daily_returns.png")
                st.image("strategy/results/RSILongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/RSILongShortStrategy/daily_return_std.png")
                st.image("strategy/results/RSILongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/RSILongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**Moving Average Convergence Divergence**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Fast Window Size**")
    st.write("    - **Slow Window Size**")
    st.write("    - **Signal Window Size**")

    if st.button("Simulate Moving Average Convergence Divergence Strategy"):
        with st.spinner("Simulating Moving Average Convergence Divergence Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/7",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/MACDLongShortStrategy/cumulative_return.png")
                st.image("strategy/results/MACDLongShortStrategy/daily_returns.png")
                st.image("strategy/results/MACDLongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/MACDLongShortStrategy/daily_return_std.png")
                st.image("strategy/results/MACDLongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/MACDLongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**GPT-3.5 Sentiment Analysis**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Hard Data Limit**")
    st.write("    - **Lookback Limit**")

    if st.button("Simulate GPT-3.5 Sentiment Analysis Strategy"):
        with st.spinner("Simulating Deep Neural Network Strategy..."):
            time.sleep(5)
            st.warning("This simulation is omitted on front-end application, since it takes too long to process.")

    st.divider()

    st.subheader("**GPT-4 Sentiment Analysis**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Hard Data Limit**")
    st.write("    - **Lookback Limit**")

    if st.button("Simulate GPT-4 Sentiment Analysis Strategy"):
        with st.spinner("Simulating Deep Neural Network Strategy..."):
            time.sleep(5)
            st.warning("This simulation is omitted on front-end application, since it takes too long to process.")

    st.divider()

    st.subheader("- **Deep Neural Network**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Learning Rate**")
    st.write("    - **Epochs**")

    if st.button("Simulate Deep Neural Network Strategy"):
        with st.spinner("Simulating Deep Neural Network Strategy..."):
            time.sleep(5)
            st.warning("This simulation is omitted on front-end application, since it takes too long to process.")

    st.divider()

    st.subheader("**Random Forest**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Training Data Limit**")
    st.write("    - **Estimators**")

    if st.button("Simulate Random Forest Strategy"):
        with st.spinner("Simulating Random Forest Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/10",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/ForestLongShortStrategy/cumulative_return.png")
                st.image("strategy/results/ForestLongShortStrategy/daily_returns.png")
                st.image("strategy/results/ForestLongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/ForestLongShortStrategy/daily_return_std.png")
                st.image("strategy/results/ForestLongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/ForestLongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**Alpha 01: Combined Strategies**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Window Size**")
    st.write("    - **Short Window Size**")
    st.write("    - **Long Window Size**")

    if st.button("Simulate Alpha 01 Strategy"):
        with st.spinner("Simulating Alpha 01 Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/11",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/AlphaStrategy_001/cumulative_return.png")
                st.image("strategy/results/AlphaStrategy_001/daily_returns.png")
                st.image("strategy/results/AlphaStrategy_001/daily_excess_return.png")
                st.image("strategy/results/AlphaStrategy_001/daily_return_std.png")
                st.image("strategy/results/AlphaStrategy_001/sharpe_ratio.png")
                st.image("strategy/results/AlphaStrategy_001/max_drawdown.png")

    st.divider()

    st.subheader("**Alpha 02: Combined Strategies**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Window Size**")
    st.write("    - **Mean Window**")
    st.write("    - **Volume Window**")
    st.write("    - **Z-Score Threshold**")

    if st.button("Simulate Alpha 02 Strategy"):
        with st.spinner("Simulating Alpha 02 Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/12",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/AlphaStrategy_002/cumulative_return.png")
                st.image("strategy/results/AlphaStrategy_002/daily_returns.png")
                st.image("strategy/results/AlphaStrategy_002/daily_excess_return.png")
                st.image("strategy/results/AlphaStrategy_002/daily_return_std.png")
                st.image("strategy/results/AlphaStrategy_002/sharpe_ratio.png")
                st.image("strategy/results/AlphaStrategy_002/max_drawdown.png")

    st.divider()

    st.subheader("**Alpha 03: Combined Strategies**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Window Size**")
    st.write("    - **Momentum Window**")
    st.write("    - **ATR Window**")

    if st.button("Simulate Alpha 03 Strategy"):
        with st.spinner("Simulating Alpha 03 Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/13",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/AlphaStrategy_003/cumulative_return.png")
                st.image("strategy/results/AlphaStrategy_003/daily_returns.png")
                st.image("strategy/results/AlphaStrategy_003/daily_excess_return.png")
                st.image("strategy/results/AlphaStrategy_003/daily_return_std.png")
                st.image("strategy/results/AlphaStrategy_003/sharpe_ratio.png")
                st.image("strategy/results/AlphaStrategy_003/max_drawdown.png")

    st.divider()

    st.subheader("**Alpha 04: Combined Strategies**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Period**")
    st.write("    - **Fast Window Size**")
    st.write("    - **Slow Window Size**")
    st.write("    - **Smooth Period**")

    if st.button("Simulate Alpha 04 Strategy"):
        with st.spinner("Simulating Alpha 04 Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/14",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/AlphaStrategy_004/cumulative_return.png")
                st.image("strategy/results/AlphaStrategy_004/daily_returns.png")
                st.image("strategy/results/AlphaStrategy_004/daily_excess_return.png")
                st.image("strategy/results/AlphaStrategy_004/daily_return_std.png")
                st.image("strategy/results/AlphaStrategy_004/sharpe_ratio.png")
                st.image("strategy/results/AlphaStrategy_004/max_drawdown.png")

    st.divider()

    st.subheader("**Alpha 05: Combined Strategies**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
            \n
            \n
            ' ' ' ' '
        """)

    st.write("    - **Period**")
    st.write("    - **Fast Window Size**")
    st.write("    - **Slow Window Size**")
    st.write("    - **Signal Window Size**")
    st.write("    - **Threshold**")

    if st.button("Simulate Alpha 05 Strategy"):
        with st.spinner("Simulating Alpha 05 Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/15",
                                    json={
                                        'hyperparameters': hyperparameters,
                                        'test_set': test_set,
                                    })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/AlphaStrategy_005/cumulative_return.png")
                st.image("strategy/results/AlphaStrategy_005/daily_returns.png")
                st.image("strategy/results/AlphaStrategy_005/daily_excess_return.png")
                st.image("strategy/results/AlphaStrategy_005/daily_return_std.png")
                st.image("strategy/results/AlphaStrategy_005/sharpe_ratio.png")
                st.image("strategy/results/AlphaStrategy_005/max_drawdown.png")

    st.divider()

    st.subheader("**Main Case: Combined Strategis & Thresholds**")

    st.markdown(
    """
        ' ' ' ' '
        \n\n
        ##### Strategy Description
        \n\n
        ###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies, nunc nisl ultrices odio, nec aliquam nisl nunc quis nunc. Nulla facilisi. Nulla facilisi.
        \n
        \n
        ' ' ' ' '
    """)

    d1 = st.text_input("**MACD Fast Window Size(days)**")
    d2 = st.text_input("**MACD Slow Window Size**")
    d3 = st.text_input("**MACD Signal Window Size**")
    d4 = st.text_input("**MACD Threshold**")
    d5 = st.text_input("**ATR Window Size**")
    d6 = st.text_input("**Volatility Threshold**")
    d7 = st.text_input("**High-Low Difference Threshold**")
    d8 = st.text_input("**Open-Close Difference Threshold**")

    if st.button("Simulate Main Case Strategy"):
        with st.spinner("Simulating Main Case Strategy..."):
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration/16",
                                    json={
                                        'hyperparameters': hyperparameters,
                                        'test_set': test_set,
                                    })
            if response:
                pass
            else:
                pass

            st.success("Simulation Complete!")
            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/MainLongShortStrategy/cumulative_return.png")
                st.image("strategy/results/MainLongShortStrategy/daily_returns.png")
                st.image("strategy/results/MainLongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/MainLongShortStrategy/daily_return_std.png")
                st.image("strategy/results/MainLongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/MainLongShortStrategy/max_drawdown.png")

    st.divider()


if __name__ == '__main__':
    lit()

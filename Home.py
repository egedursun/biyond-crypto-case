import time
import requests
import streamlit as st
from main import test_set

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
    initial_cash = st.text_input("Initial Cash", value=1_000_000)
    risk_free_rate = st.text_input("Risk Free Rate", value=0.01)
    safety_margin = st.text_input("Safety Margin", value=5)

    st.empty()

    st.markdown("#### Transactions")
    tx_volume = st.text_input("Transaction Volume", value=80)
    tx_cost = st.text_input("Transaction Cost", value=0.002)
    tx_aggr = st.text_input("Transaction Volume Change Aggression", value=0.05)
    txt_adj = st.text_input("Transaction Volume Adjustment Window", value=20)
    tx_min = st.text_input("Transaction Volume Minimum", value=10)
    tx_max = st.text_input("Transaction Volume Maximum", value=150)

    st.empty()

    st.markdown("#### Trade Frequency")
    trd_freq = st.text_input("Trade Frequency", value=1)
    gpt_freq = st.text_input("GPT Trade Frequency", value=15)

    if st.button("Update Hyper-Parameters"):
        with st.spinner("Updating Hyper-Parameters..."):
            response = requests.patch("http://localhost:5000/api/v1/strategies/1>", json={
                'name': 'name',
                'description': 'name',
                'hyperparameters': {
                    'initial_cash': initial_cash,
                    'risk_free_rate': risk_free_rate,
                    'safety_margin': safety_margin,
                    'transaction_volume': tx_volume,
                    'trade_frequency': trd_freq,
                    'gpt_trade_frequency': gpt_freq,
                    'transaction_cost': tx_cost,
                    'transaction_volume_change_aggression': tx_aggr,
                    'transaction_volume_adjustment_window': txt_adj,
                    'transaction_volume_minimum': tx_min,
                    'transaction_volume_maximum': tx_max,
                },
                'test_set': test_set,
            })
        st.success("Hyper-Parameters are updated.")
        if response:
            pass
        else:
            pass

    st.text("' ' ' ' '")

    st.divider()

    st.subheader("**Overall Performance Comparison**")

    st.image("strategy/additional_tests/performance_outputs/performance_comparison_chart_2024-01-12_13-14-23.png")

    st.divider()

    st.subheader("**Sample Stock Position Trends**")

    # TODO:

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
            response = requests.post("http://localhost:5000/api/v1/simulations/with_configuration",
                                     json={
                                         'hyperparameters': hyperparameters,
                                         'test_set': test_set,
                                     })
            if response:
                pass  # placeholder
            else:
                pass  # placeholder

            st.success("Simulation Complete!")

            # show the metrics
            try:
                with open("strategy/records/RandomLongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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

            # show the metrics
            try:
                with open("strategy/records/NaiveLongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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

    st.text_input("**Window Size**", value=14, key="01")

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

            # show the metrics
            try:
                with open("strategy/records/SMALongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

            # show the charts
            with st.expander("Show Charts"):
                st.image("strategy/results/SMALongShortStrategy/cumulative_return.png")
                st.image("strategy/results/SMALongShortStrategy/daily_returns.png")
                st.image("strategy/results/SMALongShortStrategy/daily_excess_return.png")
                st.image("strategy/results/SMALongShortStrategy/daily_return_std.png")
                st.image("strategy/results/SMALongShortStrategy/sharpe_ratio.png")
                st.image("strategy/results/SMALongShortStrategy/max_drawdown.png")

    st.divider()

    st.subheader("**Exponential Moving Average (EMA)**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            The EMALongShortStrategy class encapsulates a trading strategy based on the Exponential Moving Average (EMA), a popular tool in financial market analysis. The EMA is a type of moving average that gives more weight to recent prices, making it more responsive to new information compared to the simple moving average (SMA).

            In this strategy, the EMA is calculated over a specified window of days (10 days by default). This time frame can be adjusted to suit different trading styles – shorter windows for short-term trading and longer windows for long-term perspectives. The EMA provides a smoothed-out price trend over the specified period.
            
            The strategy's decision-making process is straightforward: it compares the stock's most recent closing price with its EMA. If the last closing price is higher than the EMA, it implies that the stock is in an uptrend, and the strategy generates an 'up' signal, suggesting a buying opportunity. This is based on the assumption that the stock price might continue to increase.
            
            Conversely, if the last closing price is below the EMA, it suggests that the stock is in a downtrend, and the strategy generates a 'down' signal, indicating a selling opportunity. The rationale here is that the stock price may continue to decrease.
            
            In cases where the last closing price is exactly equal to the EMA, the strategy issues a 'hold' signal, suggesting that the stock's price is currently stable, and it might not be an opportune time to make new trades.
            
            The EMA Long/Short Strategy is a classic example of a trend-following strategy and is widely used due to its simplicity and effectiveness. By focusing on recent price movements, it helps traders identify and potentially capitalize on developing trends in the stock market.
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Window Size**", value=14, key="02")

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

            # show the metrics
            try:
                with open("strategy/records/EMALongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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
            
            The Bollinger Long/Short Strategy, named BoilingerLongShortStrategy in the provided class, is a trading strategy that relies on Bollinger Bands to make investment decisions. Bollinger Bands are a type of statistical chart characterizing the prices and volatility of a financial instrument over time. They consist of a moving average and two standard deviation lines, one above and one below the moving average.

            In this strategy, the moving average is calculated over a specified window (20 days by default), which represents the average closing price over the previous 20 days. The standard deviation, which measures the price volatility, is then used to calculate the upper and lower bands. The upper band is set at a distance of 'k' standard deviations above the moving average, and the lower band is set the same distance below. The parameter 'k' is a multiplier that determines the width of the bands; a higher 'k' results in wider bands.
            
            The core of the strategy lies in how the current price relates to these bands. If the latest closing price is above the upper band, it's interpreted as a market being overbought, and the strategy signals a 'sell' (indicated by 'up' in the implementation). Conversely, if the latest closing price is below the lower band, the market is considered oversold, prompting a 'buy' signal (indicated by 'down'). If the price is within the bands, the market is seen as neither overbought nor oversold, and the strategy suggests holding the position (indicated by 'hold').
            
            This strategy is widely used for its simplicity and effectiveness in various market conditions. By accounting for market volatility and price trends, Bollinger Bands provide a relatively straightforward way to assess whether a stock is being traded at a price above or below its usual level, helping traders make more informed decisions on buying or selling assets.
            
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Window Size**", value=14, key="03")
    st.text_input("**Number of Standard Deviations**", value=2, key="04")

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

            # show the metrics
            try:
                with open("strategy/records/BoilingerLongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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

    st.text_input("**Window Size**", value=14, key="05")
    st.text_input("**Upper Threshold**", value=70, key="06")
    st.text_input("**Lower Threshold**", value=30, key="07")

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

            # show the metrics
            try:
                with open("strategy/records/RSILongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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

    st.text_input("**Fast Window Size**", value=12, key="08")
    st.text_input("**Slow Window Size**", value=26, key="09")
    st.text_input("**Signal Window Size**", value=9, key="10")

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

            # show the metrics
            try:
                with open("strategy/records/MACDLongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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

    st.text_input("**Hard Data Limit**", value=100, key="11")
    st.text_input("**Lookback Limit**", value=100, key="12")

    if st.button("Simulate GPT-3.5 Sentiment Analysis Strategy"):
        with st.spinner("Simulating GPT-3.5 Sentiment Analysis Strategy..."):
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

    st.text_input("**Hard Data Limit-**", value=100, key="13")
    st.text_input("**Lookback Limit-**", value=100, key="14")

    if st.button("Simulate GPT-4 Sentiment Analysis Strategy"):
        with st.spinner("Simulating GPT-4 Sentiment Analysis Strategy..."):
            time.sleep(5)
            st.warning("This simulation is omitted on front-end application, since it takes too long to process.")

    st.divider()

    st.subheader("**Deep Neural Network**")

    st.markdown(
        """
            ' ' ' ' '
            \n\n
            ##### Strategy Description
            \n\n
            The Deep Long/Short Strategy, encapsulated within the `DeepLongShortStrategy` class, is a trading strategy that leverages deep learning techniques to predict stock price movements and generate trading signals. This approach is distinct due to its use of a neural network model to analyze stock market data and make informed decisions.

            The core of this strategy is a Sequential neural network model from Keras, a popular deep learning library. The model comprises three layers: an input layer with 64 neurons, a hidden layer with 32 neurons, and an output layer with a single neuron. The model uses the 'relu' activation function for the input and hidden layers, which helps in handling non-linear data effectively. The output layer employs the 'sigmoid' activation function, ideal for binary classification tasks.
            
            In the `evaluate_symbol` method, the strategy takes the latest stock data up to the given date and constructs a feature set (X) comprising the stock's Open, High, Low, Close prices, and Volume. The target variable (y) is whether the stock’s closing price has increased compared to the previous day. The model is trained on this data to learn patterns that could suggest an upward or downward movement in the stock price.
            
            The deep learning model is compiled with the Adam optimizer and binary cross-entropy loss function, which is suitable for a binary classification problem. The model is trained over a specified number of epochs, where an epoch represents a complete pass through the entire training dataset.
            
            Once the model is trained, it predicts the movement of the stock's closing price for the next day. If the model predicts an upward movement (closing price higher than the previous day), the strategy generates an 'up' signal, suggesting a buying opportunity. Conversely, if the model predicts a downward movement, a 'down' signal is generated, indicating a selling opportunity. If the data is insufficient for making a prediction, the strategy advises holding the position.
            
            The Deep Long/Short Strategy showcases the integration of deep learning in financial markets, where complex models can identify subtle patterns in data that might be challenging to capture with traditional statistical methods. This strategy represents a sophisticated approach to algorithmic trading, leveraging the power of neural networks to navigate the stock market.
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Learning Rate**", value=0.001, key="15")
    st.text_input("**Epochs**", value=10, key="16")

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
            
            The ForestLongShortStrategy class is a sophisticated trading strategy that employs a machine learning model, specifically a Random Forest Classifier, to determine trading signals. This approach is rooted in predictive analytics and aims to leverage historical data patterns to forecast future stock price movements.

            At the core of this strategy is the Random Forest Classifier, a type of ensemble learning method. It operates by constructing a multitude of decision trees during training time and outputs the class (buy, sell, or hold) that is the mode of the classes of the individual trees. Random Forest is known for its high accuracy, ability to run efficiently on large datasets, and capability to handle many input variables without variable deletion.
            
            When evaluating a particular stock symbol, the strategy first checks if there is sufficient historical data available. The strategy requires a minimum amount of past data (specified by `training_data_limit`) to train the model effectively. If there's not enough data, the strategy defaults to a 'hold' signal.
            
            If the training data requirement is met, the strategy trains the Random Forest Classifier on the historical data. The features (`X`) include stock prices and volume, and the target variable (`y`) is a binary representation of whether the stock's closing price increased compared to the previous day.
            
            Once the model is trained, it predicts the next day's price movement using the most recent data. If the model predicts an upward movement (i.e., the closing price is expected to be higher than the previous day), it signals 'up', suggesting a potential buying opportunity. Conversely, if the model predicts a downward movement, it signals 'down', indicating a potential selling opportunity.
            
            This strategy exemplifies the application of machine learning in financial markets, where historical data is used to forecast future trends. The use of a Random Forest Classifier allows the strategy to capture complex patterns and relationships in the data, potentially leading to more informed and data-driven trading decisions.
                        
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Window Size**", value=14, key="17")
    st.text_input("**Number of Estimators**", value=100, key="18")

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

            # show the metrics
            try:
                with open("strategy/records/ForestLongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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
            The Alpha1 strategy, referred to as `evaluate_symbol_001` in the AlphaStrategy class, is a method used for making investment decisions based on market trends. This strategy primarily employs the concept of Volume Weighted Average Price (VWAP), which is an average price calculation that takes into account not only the price of the stocks but also the volume of stocks traded. In simpler terms, VWAP combines how much of a stock is being traded with its price to give investors a clearer idea of the current market trend.

            In this strategy, two different VWAP calculations are used – one for a short period and another for a long period. By comparing these two, the strategy attempts to determine the right moment to buy or sell a stock. If the short-term VWAP is above the long-term VWAP and this wasn’t the case just before, it might suggest a good time to buy (a signal termed 'up'). Conversely, if the short-term VWAP falls below the long-term VWAP, it might be an indication to sell (a signal termed 'down'). If neither of these conditions is met, the strategy advises to hold onto the stock without making any new trades (a signal termed 'hold').

            The beauty of the Alpha1 strategy lies in its ability to combine price trends with trading volumes, giving a more holistic view of the market. This approach is particularly useful in identifying the strength behind a price movement, helping investors make more informed decisions about when to enter or exit a trade. The strategy is dynamic and adjusts to recent market data, making it a potentially powerful tool for both short-term and long-term investment strategies.
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Window Size**", value=14, key="1")
    st.text_input("**Short Window Size**", value=12, key="2")
    st.text_input("**Long Window Size**", value=26, key="3")

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

            # show the metrics
            try:
                with open("strategy/records/AlphaStrategy_001/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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
            The Alpha2 strategy, identified as `evaluate_symbol_002` in the AlphaStrategy class, is centered around the concept of mean reversion and is supported by volume analysis. This approach is based on the idea that prices of stocks or securities tend to move back towards their average over time. In simpler terms, if a stock price has significantly deviated from its average, the Alpha2 strategy predicts it will eventually return to that average level.

            To implement this strategy, two key calculations are made: the Z-Score and the average trading volume. The Z-Score measures how far and in what direction a stock's price has deviated from its historical average. If the Z-Score is significantly high or low (determined by a threshold), it suggests that the stock price is unusually far from the average, potentially indicating a future return towards the mean. 
            
            However, the Alpha2 strategy adds another layer to this analysis by considering trading volume. It checks if the current volume is greater than the recent average volume. This is important because a high trading volume can validate the significance of the current price movement. For instance, if the stock price is far below the average (a low Z-Score) and the trading volume is high, it might be a good time to buy, expecting the price to rise. Conversely, a high Z-Score with high volume might signal a selling opportunity.
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Window Size**", value=14, key="4")
    st.text_input("**Mean Window**", value=12, key="5")
    st.text_input("**Volume Window**", value=26, key="6")
    st.text_input("**Z-Score Threshold**", value=9, key="7")

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

            # show the metrics
            try:
                with open("strategy/records/AlphaStrategy_002/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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
            The Alpha3 strategy, labeled as `evaluate_symbol_003` in the AlphaStrategy class, focuses on the combination of price momentum and market volatility adjustments. This strategy utilizes a specific technique to determine the right time to buy or sell a stock based on recent price changes and the stability of these changes.

            Firstly, Alpha3 calculates the price momentum, which is essentially the rate at which the price of a stock is changing. This is done by looking at the percentage change in the stock’s price over a set period. A positive momentum (where the price is going up) might suggest a good buying opportunity, while a negative momentum (where the price is dropping) might suggest a selling opportunity.
            
            However, Alpha3 adds another dimension to its strategy by incorporating the Average True Range (ATR), a measure of market volatility. The ATR helps to understand how much the price of a stock typically varies, which is an indicator of the stock's stability. In this strategy, if the momentum of a stock is positive and the current ATR is below its average, it suggests that the upward price movement is happening in a relatively stable market. This combination is seen as an ideal scenario for buying. On the flip side, if the momentum is negative and the ATR is below average, it suggests a stable downward trend, indicating a potential selling point.
            
            This strategy effectively combines the concepts of trend (via momentum) and market stability (via ATR) to provide more nuanced trading signals. By doing so, it aims to identify scenarios where a trend is likely to continue in a stable market environment, giving traders a higher confidence level in their decision to buy or sell.
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Window Size**", value=14, key="39")
    st.text_input("**Momentum Window**", value=12, key="40")
    st.text_input("**ATR Window**", value=26, key="41")

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

            # show the metrics
            try:
                with open("strategy/records/AlphaStrategy_003/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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
            The Alpha4 strategy, designated as `evaluate_symbol_004` in the AlphaStrategy class, employs a unique approach by integrating the concepts of Exponential Moving Averages (EMAs) and an oscillator derived from these averages. This strategy is crafted to identify potential buy or sell signals based on the momentum captured by the moving averages of a stock's price.

            In Alpha4, the strategy first calculates the weighted close price, which gives more importance to the closing price while still considering the opening, high, and low prices within a day. This weighted close is thought to provide a more accurate reflection of the market sentiment for that day.
            
            Following this, the strategy computes two EMAs: a fast EMA and a slow EMA, with the fast EMA having a shorter period than the slow one. The idea here is to capture both short-term and long-term price trends. The fast EMA responds quicker to price changes, while the slow EMA is more stable and slow to react.
            
            The core of the Alpha4 strategy lies in the oscillator, which is the difference between the fast and slow EMAs. This oscillator helps in understanding the momentum or the speed of the price movement. If the oscillator is increasing (where the fast EMA is moving away from the slow EMA), it suggests that the short-term trend is getting stronger compared to the long-term trend, potentially indicating a buying opportunity. Conversely, if the oscillator is decreasing (indicating the fast EMA is converging towards or going below the slow EMA), it might signal a weakening short-term trend and thus a selling opportunity.
            
            Alpha4 is particularly effective in capturing trends and reversals. By focusing on the relationship between the fast and slow EMAs, it provides insights into the strength and direction of the market trend, guiding investors on when to enter or exit a position. This method is especially useful in markets where catching momentum early can lead to significant gains.
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Period**", value=14, key="35")
    st.text_input("**Fast Window Size**", value=12, key="36")
    st.text_input("**Slow Window Size**", value=26, key="37")
    st.text_input("**Smooth Period**", value=9, key="38")

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

            # show the metrics
            try:
                with open("strategy/records/AlphaStrategy_004/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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
            
            The Alpha5 strategy, referred to as `evaluate_symbol_005` in the AlphaStrategy class, is a comprehensive approach that combines several technical indicators to identify trading signals. This strategy is distinct in its use of three key elements: the Moving Average Convergence Divergence (MACD), the Price Oscillator (PPO), and the Detrended Price Oscillator (DPO).

            Firstly, the MACD is used, which is a trend-following momentum indicator. It shows the relationship between two moving averages of a stock's price. The MACD is calculated by subtracting the long-term moving average from the short-term moving average, which gives an insight into the direction of the market momentum. The MACD score in this strategy is determined by whether the MACD is positive (indicating upward momentum) or negative (indicating downward momentum).
            
            Next, the Price Oscillator (PPO) is incorporated. The PPO, similar to the MACD, measures the difference between two moving averages but expresses this difference as a percentage, which makes it easier to compare stocks with different price levels. Like the MACD, a positive PPO indicates upward price momentum, while a negative PPO suggests downward momentum.
            
            Additionally, the Detrended Price Oscillator (DPO) is used. The DPO is an indicator designed to remove the influence of a long-term price trend from the current price, allowing a clearer view of the shorter-term price cycles. It's used to identify overbought or oversold levels and potential turning points in the market.
            
            In Alpha5, these three indicators are combined to form a composite score. Each indicator contributes to this score by indicating either a bullish (positive) or bearish (negative) signal. The final signal to buy, sell, or hold is determined based on the composite score. If the score is above a certain positive threshold, it suggests a strong bullish market and a potential buy signal. Conversely, if the score is below a certain negative threshold, it implies a strong bearish market, indicating a sell signal. In cases where the score is between these thresholds, the strategy suggests holding the position.
            
            By aggregating these three distinct indicators, Alpha5 offers a multi-faceted view of the market, leveraging different aspects of market data. This comprehensive approach aims to provide a more reliable and nuanced trading signal, catering to investors who prefer a multi-indicator strategy to guide their trading decisions.
            \n
            \n
            ' ' ' ' '
        """)

    st.text_input("**Period**", value=14, key="19")
    st.text_input("**Fast Window Size**", value=12, key="20")
    st.text_input("**Slow Window Size**", value=26, key="21")
    st.text_input("**Signal Window Size**", value=9, key="22")
    st.text_input("**Threshold**", value=0.01, key="23")

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

            # show the metrics
            try:
                with open("strategy/records/AlphaStrategy_005/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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

    d1 = st.text_input("**MACD Fast Window Size(days)**", value=12, key="24")
    d2 = st.text_input("**MACD Slow Window Size**", value=26, key="25")
    d3 = st.text_input("**MACD Signal Window Size**", value=9, key="26")
    d4 = st.text_input("**MACD Threshold**", value=0.01, key="27")
    d5 = st.text_input("**ATR Window Size**", value=14, key="28")
    d6 = st.text_input("**Volatility Threshold**", value=0.01, key="29")
    d7 = st.text_input("**High-Low Difference Threshold**", value=0.01, key="30")
    d8 = st.text_input("**Open-Close Difference Threshold**", value=0.01, key="31")

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

            # show the metrics
            try:
                with open("strategy/records/MainLongShortStrategy/metrics.txt", "r") as f:
                    for line in f.readlines():
                        st.markdown(line + "\n")
            except FileNotFoundError:
                pass

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

import pandas as pd

from clients.GPTClient import GPTClient

GPT_PROMPT = """
    You are a stock trader. You are trying to decide whether to buy or sell a stock for a long/short
    trading algorithm. For each stock, you have a dataframe of historical data. The dataframe has
    columns for the Date, Open, High, Low, Close, and Volume.
    
    You want to use the historical data to predict whether the stock will go up or down in the future.
    
    Based on your interpretation, you will return a signal to the backtesting engine.
    Your response MUST ONLY be one of the following:
    - up
    - down
    - hold
    
    Your response must not include any special characters or any additional strings. You must only
    return one of the three options above, and NOTHING ELSE!
    
    Example-1:
    '''
    up
    '''
    
    Example-2:
    '''
    down
    '''
    
    Example-3:
    '''
    hold
    '''
    
    ---
    
    Invalid Example-1:
    '''
    I think the stock will go up. My answer is 'up'.
    '''
    
    Invalid Example-2:
    '''
    Sure! I will share my answer with you. It's 'down'.
    '''
    
    Invalid Example-3:
    '''
    I think the stock will go up. My answer is 'up'. I am sure about it.
    '''
"""


class GPT_3_5LongShortStrategy:
    """
    GPT-3.5 long/short strategy.
    """

    def __init__(self):
        self.name = 'GPT3_5LongShortStrategy'
        self.description = 'GPT-3.5 long/short strategy.'
        self.signals = [
            'up',
            'down',
            'hold',
        ]
        self.gpt_client = GPTClient()
        self.gpt_client.build_assistant(name="biyond-stock-gpt3",
                                        instructions=GPT_PROMPT,
                                        model="gpt-3.5-turbo",
                                        max_tokens=5,
                                        temperature=0.5)
        self.assistant = self.gpt_client.get_assistant(name="biyond-stock-gpt3")

    def evaluate_symbol(self, date, symbol, dataframe: pd.DataFrame):
        message = f"""
            CURRENT DATE: {str(date)}
            SYMBOL: {symbol}
            DATAFRAME:
            {str(dataframe)}
        """
        response = self.assistant.ask(message)
        if response not in self.signals:
            return self.signals[2]
        return response

    def generate_signals(self, date, universe, portfolio, **kwargs):
        signals = {}
        count_hard_limit = 0
        lookback_limit = kwargs['lookback_limit']
        for symbol, dataframe in universe.items():
            cp = dataframe.iloc[-lookback_limit:]
            if count_hard_limit > kwargs['hard_limit']:
                break
            signal = self.evaluate_symbol(date, symbol, cp)
            signals[symbol] = signal
            count_hard_limit += 1
        return signals

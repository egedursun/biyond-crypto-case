from server.models.HyperParameters import HyperParameters


class Configuration:
    name: str
    description: str
    hyperparameters = HyperParameters()
    test_set: dict = {
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

    def __str__(self):
        return f"""Configuration:,name:{self.name},description:{self.description},hyperparameters:{self.hyperparameters},
        test_set:{self.test_set}"""

    @staticmethod
    def convert_to_object(configuration_str) -> object:
        configuration = Configuration()
        tokens = configuration_str.split(",")
        name = tokens[1].split(":")[1]
        description = tokens[2].split(":")[1]
        hyperparameters = tokens[3].split(":")[1]
        test_set = tokens[4].split(":")[1]
        configuration.name = name
        configuration.description = description
        configuration.hyperparameters = hyperparameters
        configuration.test_set = test_set
        return configuration

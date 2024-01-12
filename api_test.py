import json

import requests


if __name__ == '__main__':

    # request POST
    response = requests.post('http://0.0.0.0:5000/api/v1/strategies', json={
                     'name': 'test-1',
                     'description': 'test-1-desc',
                     'hyperparameters': {
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
                     },
                     'test_set': {
                         "randoms": False,
                         "naives": False,
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
                     })
    print(response.json())

    # request GET
    """
    response = requests.get('http://0.0.0.0:5000/api/v1/strategies/1')
    assert response.status_code == 200
    assert response.json()['message'] == 'Configuration retrieved successfully.'
    """

    # request GET / all
    response = requests.get('http://0.0.0.0:5000/api/v1/strategies')
    id_p = response.json()['data'][0]["id"]

    # request PATCH
    """
    response = requests.patch('http://0.0.0.0:5000/api/v1/strategies/1', json={
                        'name': 'test-2',
                        'description': 'test-2-desc',
                        'hyperparameters': {
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
                                },
                        'test_set': {
                                "randoms": False,
                                "naives": False,
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
                    })
    print(response)
    """

    """
    # request DELETE
    response = requests.delete('http://0.0.0.0:5000/api/v1/strategies/1')
    assert response.status_code == 200
    assert response.json()['message'] == 'Configuration deleted successfully.'
    """

    ##########################################
    # RUN SIMULATION
    ##########################################

    # request POST
    response = requests.post(f'http://0.0.0.0:5000/api/v1/simulations/with_configuration')
    print(response.json())
    print("All tests passed, success.")

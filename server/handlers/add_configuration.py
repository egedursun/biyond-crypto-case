import pickle
import sqlite3

from server.clients.DBClients import SQLiteClient
from server.models.HyperParameters import HyperParameters


def handle_add_configuration(request):
    """Handle the add configuration request.
    Args:
        request: The request dictionary.
    Returns:
        dict: The response dictionary.
    """
    if 'name' not in request.json:
        return {
            'message': 'Name is required.',
            'data': {}
        }
    if 'description' not in request.json:
        return {
            'message': 'Description is required.',
            'data': {}
        }
    if 'hyperparameters' not in request.json:
        return {
            'message': 'Hyperparameters is required.',
            'data': {}
        }
    if 'test_set' not in request.json:
        return {
            'message': 'Test set is required.',
            'data': {}
        }
    name = request.json['name']
    description = request.json['description']
    hyperparameters_dict = request.json['hyperparameters']
    test_set_dict = request.json['test_set']
    hyperparameters = HyperParameters()
    if 'initial_cash' not in hyperparameters_dict:
        return {
            'message': 'Initial cash is required.',
            'data': {}
        }
    if 'risk_free_rate' not in hyperparameters_dict:
        return {
            'message': 'Risk free rate is required.',
            'data': {}
        }
    if 'safety_margin' not in hyperparameters_dict:
        return {
            'message': 'Safety margin is required.',
            'data': {}
        }
    if 'transaction_volume' not in hyperparameters_dict:
        return {
            'message': 'Transaction volume is required.',
            'data': {}
        }
    if 'trade_frequency' not in hyperparameters_dict:
        return {
            'message': 'Trade frequency is required.',
            'data': {}
        }
    if 'gpt_trade_frequency' not in hyperparameters_dict:
        return {
            'message': 'GPT trade frequency is required.',
            'data': {}
        }
    if 'transaction_cost' not in hyperparameters_dict:
        return {
            'message': 'Transaction cost is required.',
            'data': {}
        }
    if 'transaction_volume_change_aggression' not in hyperparameters_dict:
        return {
            'message': 'Transaction volume change aggression is required.',
            'data': {}
        }
    if 'transaction_volume_adjustment_window' not in hyperparameters_dict:
        return {
            'message': 'Transaction volume adjustment window is required.',
            'data': {}
        }
    if 'transaction_volume_minimum' not in hyperparameters_dict:
        return {
            'message': 'Transaction volume minimum is required.',
            'data': {}
        }
    if 'transaction_volume_maximum' not in hyperparameters_dict:
        return {
            'message': 'Transaction volume maximum is required.',
            'data': {}
        }
    hyperparameters.Fund.initial_cash = hyperparameters_dict['initial_cash']
    hyperparameters.Fund.risk_free_rate = hyperparameters_dict['risk_free_rate']
    hyperparameters.Fund.safety_margin = hyperparameters_dict['safety_margin']
    hyperparameters.Fund.transaction_volume = hyperparameters_dict['transaction_volume']
    hyperparameters.Fund.trade_frequency = hyperparameters_dict['trade_frequency']
    hyperparameters.Fund.gpt_trade_frequency = hyperparameters_dict['gpt_trade_frequency']
    hyperparameters.Fund.transaction_cost = hyperparameters_dict['transaction_cost']
    hyperparameters.Fund.transaction_volume_change_aggression = \
        hyperparameters_dict['transaction_volume_change_aggression']
    hyperparameters.Fund.transaction_volume_adjustment_window = \
        hyperparameters_dict['transaction_volume_adjustment_window']
    hyperparameters.Fund.transaction_volume_minimum = hyperparameters_dict['transaction_volume_minimum']
    hyperparameters.Fund.transaction_volume_maximum = hyperparameters_dict['transaction_volume_maximum']

    hyperparameters_bytes = pickle.dumps(hyperparameters)
    test_set_bytes = pickle.dumps(test_set_dict)

    db = None
    try:
        db = SQLiteClient('db.sqlite3')
        db.Configurations.add_configuration(name, description, hyperparameters_bytes, test_set_bytes)
    except sqlite3.Error as e:
        raise e
    return {
        'message': 'Configuration added successfully.',
        "data": {
            'name': name,
            'description': description,
            'hyperparameters': hyperparameters_dict,
            'test_set': test_set_dict
        }
    }

import pickle
import sqlite3

from server.clients.DBClients import SQLiteClient


def handle_update_configuration(request, configuration_id):
    """Handle the update configuration request.

    Args:
        request: The request dictionary.
        configuration_id: The configuration ID.

    Returns:
        dict: The response dictionary.
    """
    name = None
    if 'name' in request.json:
        name = request.json['name']
    description = None
    if 'description' in request.json:
        description = request.json['description']
    hyperparameters_bytes = None
    if 'hyperparameters' in request.json:
        hyperparameters = request.json['hyperparameters']
        hyperparameters_bytes = pickle.dumps(hyperparameters)
    test_set_bytes = None
    if 'test_set' in request.json:
        test_set = request.json['test_set']
        test_set_bytes = pickle.dumps(test_set)
    try:
        db = SQLiteClient('db.sqlite3')
        db.Configurations.update_configuration(configuration_id, name, description, hyperparameters_bytes,
                                               test_set_bytes)
    except sqlite3.Error as e:
        raise e
    return {
        'message': 'Configuration updated successfully.',
        'data': {
            'id': configuration_id,
            'name': name,
            'description': description,
            'hyperparameters': hyperparameters_bytes,
            'test_set': test_set_bytes,
        }
    }

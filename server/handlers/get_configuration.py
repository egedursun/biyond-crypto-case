import pickle
import sqlite3

from server.clients.DBClients import SQLiteClient


def handle_get_configuration(request, configuration_id):
    """Handle the get configuration request.
    Args:
        request: The request dictionary.
        configuration_id: The configuration ID.
    Returns:
        dict: The response dictionary.
    """
    db = None
    try:
        db = SQLiteClient('db.sqlite3')
        data = db.Configurations.get_configuration(configuration_id)
    except sqlite3.Error as e:
        raise e
    if data:
        data = {
            'id': data[0],
            'name': data[1],
            'description': data[2],
            'hyperparameters': pickle.loads(data[3]),
            'test_set': pickle.loads(data[4])
        }
    else:
        data = {}
    return {
        'message': 'Configuration retrieved successfully.',
        'data': data
    }

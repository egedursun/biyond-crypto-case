import sqlite3

from server.clients.DBClients import SQLiteClient


def handle_delete_configuration(request, configuration_id):
    """Handle the delete configuration request.
    Args:
        request: The request dictionary.
        configuration_id: The configuration ID.
    Returns:
        dict: The response dictionary.
    """
    db = None
    try:
        db = SQLiteClient('db.sqlite3')
        db.Configurations.delete_configuration(configuration_id)
    except sqlite3.Error as e:
        raise e
    return {
        'message': 'Configuration deleted successfully.',
        'data': {
            'id': configuration_id
        }
    }

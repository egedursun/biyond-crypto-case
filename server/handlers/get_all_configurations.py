import pickle
import sqlite3

from server.clients.DBClients import SQLiteClient


def handle_get_all_configurations(request):
    """Handle the get all configurations request.

    Args:
        request: The request dictionary.

    Returns:
        dict: The response dictionary.
    """
    db = None
    try:
        db = SQLiteClient('db.sqlite3')
        data = db.Configurations.get_all_configurations()
    except sqlite3.Error as e:
        raise e
    if data:
        data = [
            {'id': row[0]} for row in data]
    else:
        data = []
    return {
        'message': 'Configurations retrieved successfully.',
        'data': data
    }

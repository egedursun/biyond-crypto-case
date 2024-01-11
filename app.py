import json

import flask
from flask import jsonify, request

from db_init import initialize_db
from server.handlers.add_configuration import handle_add_configuration
from server.handlers.delete_configuration import handle_delete_configuration
from server.handlers.get_all_configurations import handle_get_all_configurations
from server.handlers.get_configuration import handle_get_configuration
from server.handlers.update_configuration import handle_update_configuration
from strategy.strategy_interface import run

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'message': 'healthy'})


@app.post('/api/v1/strategies')
def strategies():
    return handle_add_configuration(request)


@app.get('/api/v1/strategies')
def strategies_list():
    return handle_get_all_configurations(request)


@app.get('/api/v1/strategies/<string:strategy_id>')
def strategies_get(strategy_id):
    return jsonify(handle_get_configuration(request, strategy_id))


@app.patch('/api/v1/strategies/<string:strategy_id>')
def strategies_update(strategy_id):
    return jsonify(handle_update_configuration(request, strategy_id))


@app.delete('/api/v1/strategies/<string:strategy_id>')
def strategies_delete(strategy_id):
    return jsonify(handle_delete_configuration(request, strategy_id))


###############################################################################
# RUN MODEL SIMULATION(S)
###############################################################################

@app.post('/api/v1/simulations/with_configuration/<string:strategy_id>')
def run_simulation(strategy_id):
    # retrieve the strategy
    strategy = handle_get_configuration(request, strategy_id)
    if strategy['data'] == {}:
        return jsonify({'message': 'Strategy not found.'}), 404
    # run the simulation
    hyperparameters = strategy['data']['hyperparameters']
    test_set = strategy['data']['test_set']
    run(hyperparameters, test_set)
    return jsonify({'message': 'Simulation completed successfully.'}), 200

###############################################################################
###############################################################################


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PATCH,POST,DELETE')
    return response


def run_server(delete_old=False):
    # init DB
    initialize_db(delete_existing_table=delete_old)
    app.run(host='localhost', port=5000, debug=True)


if __name__ == '__main__':
    run_server(delete_old=False)

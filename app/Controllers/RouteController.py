from flask import Flask, jsonify, request
from flask_request_validator import (
    JSON,
    FORM,
    Param,
    validate_params
)

import sys
import os

sys.path.append('app/Services')
import CsvService, ShortestPathService
sys.path.append('app/Transformers')
import RouteCsvTransformer


app= Flask(__name__)

@app.route('/')
def health():
    return jsonify('up')

@app.route("/routes/best-route", methods=["GET"])
@validate_params(
    Param('origin', JSON, str, required=True),
    Param('destination', JSON, str, required=True),
)
def best_route(origin, destination):

    data = request.get_json()
    origin = data['origin']
    destination = data['destination']

    graph = CsvService.csvToDict(os.getenv('CSV_INPUT_FILE', 'input_files/input-routes.csv'))
    [value, path] = ShortestPathService.dijkstraPath(graph, origin, destination)

    return jsonify({'path' : path, 'value' : value})

@app.route("/routes", methods=["POST"])
@validate_params(
    Param('origin', JSON, str, required=True),
    Param('destination', JSON, str, required=True),
    Param('cost', JSON, int, required=True),
)
def store(origin, destination, cost):

        csvFilename = os.getenv('CSV_INPUT_FILE', 'input_files/input-routes.csv')

        data = request.get_json()
        origin = data['origin']
        destination = data['destination']
        cost = data['cost']

        CsvService.write(csvFilename, ("{},{},{}\n").format(origin,destination,cost))
        return jsonify(RouteCsvTransformer.transform(csvFilename)[-1])

@app.route("/routes", methods=["GET"])
def index():

        csvFilename = os.getenv('CSV_INPUT_FILE', 'input_files/input-routes.csv')
        return jsonify(RouteCsvTransformer.transform(csvFilename))

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
import pytest
import json
import sys
from flask import Flask, jsonify, Blueprint
sys.path.append('app/Transformers')
import RouteCsvTransformer
sys.path.append('app/Services')
import CsvService, ShortestPathService

bp = Blueprint('myapp', __name__)

@bp.route('/')
def health():
    return jsonify('up')

@bp.route('/routes')
def index():
    return jsonify(RouteCsvTransformer.transform('tests/fixture/input.csv'))

@bp.route('/routes/best-route', methods=['GET'])
def best_route():
    with open('tests/fixture/bestRoutes.json', 'r') as graph:
        graph = json.loads(graph.read())
        [value, path] = ShortestPathService.dijkstraPath(graph, 'GRU', 'CDG')
    return jsonify({'path': path, 'value': value})

@bp.route('/routes', methods=['POST'])
def store():
    CsvService.write('tests/fixture/input.csv', ("{},{},{}\n").format('VIX', 'DRU', 22))
    return jsonify(RouteCsvTransformer.transform('tests/fixture/input.csv')[-1])

@pytest.fixture()
def test_client():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(bp)

    with open('tests/fixture/input.csv', 'w') as testCsv:
        testCsv.write("GRU,BRC,10\nBRC,SCL,5\nGRU,CDG,75\n")

    return flask_app.test_client()


def test_health(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'up' in response.data

def test_routes(test_client):
    response = test_client.get('/routes')
    responseJson = json.loads(response.data.decode("UTF-8"))

    expected = [
      {
        "cost": "10",
        "destination": "BRC",
        "origin": "GRU"
      },
      {
        "cost": "5",
        "destination": "SCL",
        "origin": "BRC"
      },
      {
        "cost": "75",
        "destination": "CDG",
        "origin": "GRU"
      }
    ]

    assert response.status_code == 200
    assert responseJson == expected

def test_best_route(test_client):
    response = test_client.get('/routes/best-route', data=dict(origin='GRU', destination='CDG'))
    responseJson = json.loads(response.data.decode("UTF-8"))

    expected = {
      "path": "GRU - CDG",
      "value": 75
    }

    assert response.status_code == 200
    assert responseJson == expected

def test_store_route(test_client):
    response = test_client.post('/routes', data=dict(origin='GRU', destination='CDG', cost=22))
    responseJson = json.loads(response.data.decode("UTF-8"))

    expected = {
      "cost": "22",
      "destination": "DRU",
      "origin": "VIX"
    }

    assert response.status_code == 200
    assert responseJson == expected

    with open('tests/fixture/input.csv', 'w') as testCsv:
        testCsv.write("GRU,BRC,10\nBRC,SCL,5\nGRU,CDG,75\n")
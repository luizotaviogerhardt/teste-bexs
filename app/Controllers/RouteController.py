from flask import Flask, jsonify, request
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
def bestRoute():

    data = request.get_json()
    origin = data['origin']
    destination = data['destination']

    try:
        graph = CsvService.csvToDict(os.getenv('CSV_INPUT_FILE', 'input_files/input-routes.csv'))
    except:
        print("ERROR : Could not read csv input file {}!".format(os.getenv('CSV_INPUT_FILE', 'input_files/input-routes.csv')))
        exit(0)

    [value, path] = ShortestPathService.dijkstraPath(graph, origin, destination)

    return jsonify({'path' : path, 'value' : value})

@app.route("/routes", methods=["POST"])
def store():

        csvFilename = os.getenv('CSV_INPUT_FILE', 'input_files/input-routes.csv')

        data = request.get_json()
        origin = data['origin']
        destination = data['destination']
        cost = data['cost']

        CsvService.write(csvFilename, ("{},{},{}\n").format(origin,destination,cost))
        return jsonify(RouteCsvTransformer.transform(csvFilename))

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
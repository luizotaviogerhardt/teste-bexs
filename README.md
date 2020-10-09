# Bexs Backend Exam 

Solution developed for Bexs backend exam. Writen in Python3 using [Flask](https://flask.palletsprojects.com/en/1.1.x/) for the REST API. The goal is to find the optimal route between two points, given a list of possible routes and costs.

## Dependencies
### Commmand Line App
- [Docker](https://www.docker.com/)

OR

- [Python3](https://www.python.org/)

### REST API
- [Docker](https://www.docker.com/)

## Running the Command Line App with Docker

After installing Docker you can run the app with

```./service up```

Then run the console command with docker exec, passing the CSV input file as an argument

```docker exec -it routes sh mysolution input_files/input-routes.csv```

You will be prompted to enter the origin and destination

```
Please enter the route in the format ORIGIN-DESTINATION : GRU-CDG
The best route is : GRU - BRC - SCL - ORL - CDG with total cost of $40.
```

You can type return to exit at any time

## Running the Command Line App without Docker


After installing Python3 run :

```./mysolution {input_file_location}```

I included the example CSV file provided in the project, you can run it with :

```./mysolution input_files/input-routes.csv```

You will be prompted to enter the origin and destination

```
Please enter the route in the format ORIGIN-DESTINATION : GRU-CDG
The best route is : GRU - BRC - SCL - ORL - CDG with total cost of $40.
```

You can type return to exit at any time

## Running the REST API

After installing Docker you can run the app with

```./service up```

## Endpoints

### Get all available routes

**GET /routes**


**Example Request:**
```
curl --location --request GET 'http://localhost:5001/routes' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw ''
```

### Get the best route.

**GET /routes/best-route**

**Arguments**


| Name     | Location | Type     | Example  |
| -------- | -------- | -------- | -------- |
| origin          | body     | string     | GRU|
| destination     | body     | string     | BRC|


**Example Request:**

```
curl --location --request GET 'http://localhost:5001/routes/best-route' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
	"origin" : "GRU",
	"destination" : "CDG"
}'
```

### Store a new route.

**POST /routes**

**Arguments**


| Name     | Location | Type     | Example  |
| -------- | -------- | -------- | -------- |
| origin          | body     | string     | VIX|
| destination     | body     | string     | DRU|
| cost     | body     | integer     | 22|


**Example Request:**

```
curl --location --request POST 'http://localhost:5001/routes' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
	"origin" : "VIX",
	"destination" : "DRU",
	"cost"	: 22
}'
```

## Tests

To run the tests you will need [pytest](https://docs.pytest.org/en/stable/getting-started.html)

```pip3 install pytest pytest-flask```

From the root directory run `pytest -v`

``` 
> pytest -v   

test session starts 
 
platform darwin -- Python 3.7.7, pytest-6.1.1, py-1.9.0, pluggy-0.13.1 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/luizotavio/teste-bexs
plugins: flask-1.0.0
collected 5 items

tests/functional/test_RouteController.py::test_health PASSED
tests/functional/test_RouteController.py::test_routes PASSED
tests/functional/test_RouteController.py::test_best_route PASSED
tests/functional/test_RouteController.py::test_store_route PASSED
tests/unit/test_RouteCsvTransformer.py::RouteCsvTransformerTest::test_should_transform_csv PASSED

5 passed in 0.06s
```


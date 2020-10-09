# code adapted from https://github.com/TamaWilson/dijkstra_python

def dijkstra(graph, origin):

    control = {}
    distance = {}
    actualNode = {}
    notVisited = []
    actual = origin
    actualNode[actual] = 0

    for vertex in graph.keys():
        notVisited.append(vertex)
        distance[vertex] = float('inf')

    distance[actual] = 0
    notVisited.remove(actual)

    while notVisited:
        for neighbor, weight in graph[actual].items():
            weightCalc = weight + actualNode[actual]
            if distance[neighbor] == float("inf") or distance[neighbor] > weightCalc:
                distance[neighbor] = weightCalc
                control[neighbor] = distance[neighbor]

        if control == {}: break
        minNeighbor = min(control.items(), key=lambda x: x[1])
        actual = minNeighbor[0]
        actualNode[actual] = minNeighbor[1]
        notVisited.remove(actual)
        del control[actual]

    #print(distance)

def dijkstraPath(graph, origin, destination):

    control = {}
    distance = {}
    actualNode = {}
    notVisited = []
    actual = origin
    actualNode[actual] = 0

    if not validOriginAndDestination(graph, origin, destination):
        raise ValueError('Invalid Origin or Destination!')

    for vertex in graph.keys():
        notVisited.append(vertex)  # inclui os vertexs nos não visitados
        distance[vertex] = float('inf')  # inicia os vertexs como infinito

    distance[actual] = [0, origin]

    notVisited.remove(actual)

    while notVisited:
        for neighbor, weight in graph[actual].items():
            weightCalc = weight + actualNode[actual]
            if distance[neighbor] == float("inf") or distance[neighbor][0] > weightCalc:
                distance[neighbor] = [weightCalc, actual]
                control[neighbor] = weightCalc
                #print(control)

        if control == {}: break
        minNeighbor = min(control.items(), key=lambda x: x[1])
        actual = minNeighbor[0]
        actualNode[actual] = minNeighbor[1]
        notVisited.remove(actual)
        del control[actual]

    return (distance[destination][0], printPath(distance, origin, destination))

def validOriginAndDestination(graph, origin, destination):
    return origin in graph.keys() and destination in graph.keys()

def printPath(distances, origin, destination):
    if destination != origin:
        return "%s - %s" % (printPath(distances, origin, distances[destination][1]), destination)
    else:
        return origin


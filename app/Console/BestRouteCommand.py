import sys
sys.path.append('app/Services')
import CsvService, ShortestPathService

try:
    filename = sys.argv[1]
    graph = CsvService.csvToDict(sys.argv[1])
except:
    print("ERROR : Could not read file {}".format(filename))
    exit(0)

while(True):
    route = input('Please enter the route in the format ORIGIN-DESTINATION : ')
    if not route:
        print("Exiting...")
        exit(0)
    [origin, destination] = route.split('-')

    [value, path] = ShortestPathService.dijkstraPath(graph, origin, destination)

    print('The best route is : {} with total cost of ${}.'.format(path, value))
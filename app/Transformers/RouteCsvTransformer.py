import sys
sys.path.append('app/Services')
import CsvService

def transform(csvFilename):
    response = []
    for line in CsvService.getLines(csvFilename):
        response.append({
            'origin'      : line[0],
            'destination' : line[1],
            'cost'        : line[2],
            })
    return response
import csv

def csvToDict(csvFilename):
    dict = {}
    with open(csvFilename, mode='r') as file:
        reader = csv.reader(file)
        for rows in reader:
            if rows[0] in dict.keys():
                dict[rows[0]][rows[1]] = int(rows[2])
            else:
                dict[rows[0]] = {rows[1] : int(rows[2])}
            if rows[1] not in dict.keys():
                dict[rows[1]] = {}

    return dict

def write(csvFilename, line):
    f = open(csvFilename, mode='a')
    f.write(line)

def getLines(csvFilename):
    lines = []
    with open(csvFilename, mode='r') as file:
        for line in csv.reader(file):
            lines.append(line)
        return lines
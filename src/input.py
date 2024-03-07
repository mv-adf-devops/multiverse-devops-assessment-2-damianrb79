import csv 
import os.path 
def read_csv():
    result = []
    with open(os.path.dirname(__file__) + '/../results.csv', newline='') as csvfile:
        resultsreader = csv.reader(csvfile)
        for row in resultsreader:
            result.append(row)
    return result 
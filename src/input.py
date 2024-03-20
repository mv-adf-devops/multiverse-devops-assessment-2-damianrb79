import csv 
import os.path 
def is_duplicate(row, result): 
    for r in result:
        if row[0] == r[0]:
            return True
    return False

def is_blank_line(row):
    if not all(row):    
        return True
    return False

def read_csv():
    result = []
    with open(os.path.dirname(__file__) + '/../results.csv', newline='') as csvfile:
        resultsreader = csv.reader(csvfile)
        next(resultsreader)
        for row in resultsreader:
            if is_duplicate(row, result):
                continue     
            if is_blank_line(row):
                continue        
            result.append(row)
    return result 
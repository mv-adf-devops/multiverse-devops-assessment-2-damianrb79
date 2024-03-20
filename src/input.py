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

def capitalise_user_name(row):
    row[1] = row[1].capitalize()
    row[2] = row[2].capitalize()

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
            capitalise_user_name(row) 

            result.append(row)
        

    return result 
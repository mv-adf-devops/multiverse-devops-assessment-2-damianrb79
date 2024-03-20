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

def is_invalid_last_answer(row):
    try:
        # if the last answer is not an integer between 1 and 10, then it is invalid
        if not (int(row[5]) >= 1 and int(row[5]) <= 10):
            return True
    except ValueError:
        # if the last answer is not an integer, then it is invalid
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
            capitalise_user_name(row)
            if is_invalid_last_answer(row):
                continue  
            result.append(row)
    
    return result

def write(result):
    with open(os.path.dirname(__file__) + '/../clean_results.csv', 'w', newline = '') as clean_file:
        writer = csv.writer(clean_file)
        header_row = ["user_id", "first_name", "last_name", "answer_1", "answer_2", "answer_3"]
        writer.writerow(header_row)
        writer.writerows(result)
 
if __name__ == "__main__":
    result = read_csv()
    write(result) 
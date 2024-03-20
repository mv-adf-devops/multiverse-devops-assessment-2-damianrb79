import csv
import os
 
with open(os.path.dirname(__file__) + '/../clean_results.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        # print each row with a width of 20 characters, left aligned - for the "stretch goal"
        print(f'{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<20} {row[5]:<20}')
""" 
take employee_census.txt and make other files for visualizing in d3
"""

import os
import ujson as json
from collections import defaultdict

DIR_NAME, _ = os.path.split(os.path.abspath(__file__))

data = []

def write_to_file(data,file_name):
    open(DIR_NAME + '/../data/' + file_name,'w').write(json.dumps(data)) 

def gather_birthdays():
    date = []
    date_counts = defaultdict(lambda: defaultdict(lambda: 0))

    for line in data[1:]:
        birthday = line.split(',')[-5].split('/')
        bday_dates = { "day": int(birthday[1]), "month": int(birthday[0])}
        date_counts[int(birthday[1])][int(birthday[0])] += 1

    # or could return just the counts per date
    date_json = []
    for day,month_data in date_counts.iteritems():
        for month, count in month_data.iteritems():
            date_json.append({"day": day, "month": month, "count": count})
    
    # want to keep info about position and color accordingly?
    write_to_file(date_json, 'birthday.json')

def open_original_file():
    global data

    with open(DIR_NAME + '/../employee_census.csv') as fh:
        for line in fh:
            data.append(line.strip())
       
if __name__ == "__main__":
    open_original_file()
    gather_birthdays()
    
import csv 

with open(r'OrangeProblem\book_dataset.csv','r',newline='\r\n') as f:

    r = csv.DictReader(f)

    for i in r:

        print(i)
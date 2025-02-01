
# ! File Handling

import csv

with open(r'Files\biopic.txt') as f: # ! default mode of open is r (read mode)
    print(f.read())

# ! These Functions below work only in r,r+, w+ and a+

# * read() returns all the things contained in the text file 

# * readline() reads one line with \n included

# * readlines() returns a list which contain each line as an element (with \n included at each line)

with open(r'Files\biopic.txt','w') as f: # ! w mode will create a new file if doesn't exist or overwrites(clears the file and starts from empty file)
    
    f.write('I am writing something new\n')

    f.write('If I don\'t add \\n this will be printed continuesly')

    f.write('Like so')

import csv

with open(r'Files\t.csv','r',newline='\r\n') as d: # ! newline='\r\n' removes any empty lines present in the csv file for a more presentable output

    a = csv.reader(d) # * This produces a readable object (which means loop through it to get the values)

    print(a) # * This prints the object representation

    for i in a:

        print(i) # * This prints each value (row) in the csv file (except the empty rows as specified by newline='\r\n')

with open(r'Files\t.csv','a',newline='') as d: # ! We just don't add any empty lines when adding new data by using newline = ''

    a=csv.writer(d) # * We created a writer object which will help us 

    a.writerow([1,2,3])

    a.writerow([10,11,12])
    
print('After Adding new things to the csv file:')

with open(r'Files\t.csv','r',newline='\r\n') as d: # ! look at line 404

    a = csv.reader(d)

    head = next(a) # * Skips the header row

    for i in a:

        print(i)

#TODO learn about Dictreader and Dictwriter functions for csv

with open(r'Files\t.csv','a',newline='') as d:

    a = {1:1,2:2,3:3}

    b = csv.DictWriter(d)

    b.writerow(a)

with open(r'Files\t.csv','r',newline='\r\n') as d:

    a = csv.DictReader(d)

    for i in a:

        print(i)

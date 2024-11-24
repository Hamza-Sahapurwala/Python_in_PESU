
# * Date: 13/11/2024

'''
Problem Statement:

Given the details of a Cricket Match in the CSV file containing columns - id, city, date, team1, team2, toss_winner, toss_decision, winner, player_of_match, and venue, find the solution for the following questions:

1. Find the total number of matches that happened in "M Chinnaswamy Stadium".

2. Insert a new match played between "Royal Challengers Bangalore" with "Kolkata Knight Riders" on May 25th, 2017, at Kolkata Eden Garden. Toss winner was "Kolkata Knight Riders", toss_decision was 'field', winner was "Royal Challengers Bangalore", and player_of_match was "Virat Kohli". ID of the match is "578".

3. Find the total number of matches played by each Cricket Team.

4. Display the details of the matches which are won by "Chennai Super Kings".

5. Find the total number of matches played at each city.

6. Display how many times Mumbai Indians won the toss.

7. Find the total number of matches "SR Watson" got player of the match.

8. Sort the matches based on the winner alphabetically and write in new CSV file named "maches_sorted.csv" 9. Store all the matches that happened in "Delhi" in new csv file.
'''

import csv

# * 1st

# c = 0

# with open('matches_banana.csv','r',newline='\r\n') as f:

#     a = csv.reader(f)

#     for i in a:

#         if i[9] == 'M Chinnaswamy Stadium':

#             c += 1

#     print('The no. of matches played in M Chinnaswamy Stadium is',c)

# * 2nd

# with open('matches_banana.csv','a',newline='') as f:

#     a = csv.writer(f)

#     a.writerow([578,'Kolkata','05/25/2017','Royal Challengers Bangalore','Kolkata Knight Riders','Kolkata Knight Riders','field','Royal Challengers Bangalore','Virat Kohli','Eden Gardens'])

# * 3rd

# a = []

# with open('matches_banana.csv','r',newline='\r\n') as f:

#     r = csv.reader(f)

#     h = next(r)

#     for i in r:

#         if i[3] not in a:

#             a.append(i[3])

#     f.seek(0)

#     c = 0

#     for i in range(len(a)):

#         for j in r:

#             # print(j)

#             if j[3] == a[i]:

#                 c += 1
        
        
#         print(f'The no. of times {a[i]} played is {c}.')

#         c = 0

#         f.seek(0)

# * 4th

# with open('matches_banana.csv','r',newline='\r\n') as f:

#     r = csv.reader(f)

#     for i in r:

#         if i[7] == 'Chennai Super Kings':

#             print(i)

# * 5th

# with open('matches_banana.csv','r',newline='\r\n') as f:

#     a = []
    
#     r = csv.reader(f)

#     h = next(r)

#     for i in r:

#         if i[1] not in a:

#             a.append(i[1])

#     f.seek(0)

#     c = 0

#     for i in a:

#         for j in r:

#             if j[1] == i:

#                 c += 1

#         print(f'The total no. of matches played in {i} is {c}.')

#         f.seek(0)

#         c = 0

# * 6th

# with open('matches_banana.csv','r',newline='\r\n') as f:

#     r = csv.reader(f)

#     c = 0

#     for i in r:

#         if i[5] == 'Mumbai Indians':

#             c += 1

#     print(f'The no. of times Mumbai Indians have won the toss is {c}.')

# * 7th

# with open('matches_banana.csv','r',newline='\r\n') as f:

#     r = csv.reader(f)

#     c = 0

#     for i in r:

#         if i[8] == 'SR Watson':

#             c += 1

#     print(f'The no. of times SR Watson has got player of the match is {c}.')

# * 8th

# with open('matches_banana.csv','r',newline='\r\n') as f:

#     r = csv.reader(f)

#     l = []

#     c = 0

#     for i in r:

#         l.append(i)

#     l.sort(key=lambda x:x[7])

#     for row in l:

#         print(row[7])

# * 9th

# with open('matches_banana.csv','r',newline = '\r\n') as f:

#     r = csv.reader(f)

#     a = []

#     for i in r:

#         if i[1] == 'Delhi':

#             a.append(i)

# with open('delhi_matches.csv','a',newline='') as d:

#     b = csv.writer(d)

#     b.writerows(a)

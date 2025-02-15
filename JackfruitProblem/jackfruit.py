import csv

print('Hello!!! How are you?\nAre you a current user?')

# for_asking = input()

# while for_asking in 'Yy':

#     a = input('Enter your name:')

#     with open('users.csv','r',newline='\r\n') as f:

with open(r'JackfruitProblem\restaurants.csv','r',newline='\r\n') as resti, open(r'JackfruitProblem\users.csv','+r',newline='\r\n') as usi, open(r'D:\Hamza\Python\Hackathon_Question\Hackathon_Question\bookings.csv', 'r', newline='\r\n') as bookie:

    restaurants = csv.reader(resti)

    next(restaurants)

    print('These are the restaurants we have right now available to book:')

    for i in restaurants:

        print(i[1])

    print('Where do you want to book?')

    questionaboutwhere = input()

    print('Which seater to do want to book?')

    questionaboutseater = int(input())

    